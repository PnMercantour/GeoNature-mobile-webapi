import logging
from operator import itemgetter
import uuid

from django.db import connections, transaction, IntegrityError
from django.conf import settings
from django.utils.translation import ugettext as _

logger = logging.getLogger(__name__)


class QueryBuildError(Exception):
    pass

class SynchronizeError(Exception):
    pass


def query_db(sqlquery, commit=False):
    """
    Executes a single query on the Faune database defined in project settings.
    Returns a `cursor`
    
    sqlquery -- a SQL statement
    commit -- whether to commit after running the query
    """
    # Connect to Faune DB
    cursor = connections[settings.DATABASE_ID].cursor()
    # Execute SQL
    logger.debug(_("Faune SQL: %s") % sqlquery)
    cursor.execute(sqlquery)
    if commit:
        logger.debug(_("Faune SQL: COMMIT"))
        transaction.commit_unless_managed(using=settings.DATABASE_ID)
    return cursor


def sync_db(objects, atomic=True):
    """
    From a specified list of objects, executes equivalent insert or update
    statements on the gr@ce database.
    
    objects -- a list of dicts, as used in ``build_sync_query()``
    atomic -- whether to commit between each query (Default: True)
    """
    logger.info(_("Synchronize %s objects") % len(objects))
    sid = transaction.savepoint()
    try:
        for feature in objects:
            q = build_sync_query(feature)
            query_db(q, commit=atomic)
        if not atomic:
            if len(objects) > 0:
                logger.debug(_("Faune SQL: COMMIT %s operation(s)") % len(objects))
                transaction.commit_unless_managed(using=settings.DATABASE_ID)
    except IntegrityError, e:
        logger.error(e)
        logger.info(_("ROLLBACK"))
        transaction.savepoint_rollback(sid)
        raise SynchronizeError(str(e))


def build_sync_query(datafields, table_name=None):
    """
    Builds a SQL statement from a dict of (fields, values).

    datafields -- a dict with field names and related values.
    table_name -- the SQL table name (Default: check if `datafields` has an item `table_name`)
    """
    if table_name is None:
        if 'table_name' in datafields:
            table_name = datafields.pop('table_name')
        else:
            raise QueryBuildError(_("Table name cannot be determined"))

    # Lower-case
    table_name = table_name.lower()
    datafields = dict((k.lower(), v) for k, v in datafields.iteritems())

    # Get column ID for the current table
    id_col = settings.FAUNE_TABLE_INFOS.get(table_name).get('id_col')

    # Remove the column ID if present in the datafields
    #obj_id = None
    #if id_col in datafields:
    #    obj_id = datafields.pop(id_col)
    #if 'fid' in datafields:
    #    obj_id = datafields.pop('fid')
    # If table is specified in object id, remove it !
    #if obj_id and obj_id.startswith(table_name + '.'):
    #    obj_id = obj_id.replace(table_name + '.', '')

    updates = []
    for field, value in datafields.items():
        if value != None:
            value = unicode(value).replace("`", "'")   # Single quotes
            if "ST_" not in value:  # Do not escape PostGIS functions
                value = unicode(value).replace("'", "''")  # Double quotes
                value = "'%s'" % value
        else:
            value = "NULL_VALUE"
        updates.append((field, value))

    sql_string = ""

    #if obj_id is None:
    # We have to retreive a new ID from the table
    # TODO
    newid = gen_id()
    updates.append((id_col, newid))
    #else:
    #    # If not quoted, quote !
    #    if obj_id.replace("'", '') == obj_id:
    #        obj_id = "'%s'" % obj_id
    #    updates.append((id_col, obj_id))
    
    sql_string = u"INSERT INTO %s (%s) VALUES (%s)" % (table_name, 
                                                ', '.join(map(itemgetter(0), updates)),
                                                ', '.join(map(itemgetter(1), updates)))
    # Manage null values
    sql_string = sql_string.replace("'NULL_VALUE'","Null")
    sql_string = sql_string.replace("NULL_VALUE","Null")
    return sql_string


def gen_id():
    """
    Generate a new ID base
    Returns the newid.
    
    """
    newid = "'%s'" % (uuid.uuid4())
    return newid
