from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils import simplejson
from django.utils.datastructures import SortedDict
from django.conf import settings

from faune.utils import sync_db, query_db

import json
import time

@csrf_exempt
def import_data(request):
    """
    Import data from json to DataBase
    """

    params = request.POST
    data = params['data']
    
    if not check_token(request):
        print "You're not allowed to retreive information from this webservice"
        return HttpResponse()

    json_data = simplejson.loads(data)
        
        
    # TODO: insert TABLE_SHEET, then TABLE_STATEMENT, then TABLE_SHEET_ROLE
    
    # Insert into TABLE_SHEET
    objects = []
    new_feature = {}
    new_feature['table_name'] = settings.TABLE_SHEET
    new_feature['supprime'] = 'False'
    #new_feature['fid'] = feature.get('fid')
    #objects[key] = new_feature    
    objects.append(new_feature)
    sync_db(objects)
    
    #for key, feature in enumerate(objects): 
    #    
    #    table_name = feature.get('table_name')
    
    # Insert into TABLE_STATEMENT
    
    # Insert into TABLE_SHEET_ROLE
    
    print json_data['taxon']['id']
    for key in json_data['taxon']['counting']:
        print key
        print json_data['taxon']['counting'][key]
    for key in json_data['taxon']['observation']:
        print key
        print json_data['taxon']['observation'][key]
    for key in json_data['taxon']['mortality']:
        print key
        print json_data['taxon']['mortality'][key]
    print json_data['taxon']['comment']
    
    # TODO: ne pas oublier de remplir certains champs (par exemple: supprimer = false) automatiquement
    taxa
    response_content = []
    response_content.append({
        'status' : 'import'
    })

    response = HttpResponse()
    simplejson.dump(response_content, response,
                ensure_ascii=False, separators=(',', ':'))
                
    return response
    

def export_taxon(request):
    """
    Export taxon table from DataBase to mobile
    """
    return export_data(request, settings.TABLE_TAXON)
    
    
def export_family(request):
    """
    Export family table from DataBase to mobile
    """
    return export_data(request, settings.TABLE_FAMILY)

    
def export_unity(request):
    """
    Export unity table from DataBase to mobile
    """
    return export_data(request, settings.TABLE_UNITY)

    
def export_taxon_unity(request):
    """
    Export crossed taxon / unity table from DataBase to mobile
    """
    return export_data(request, settings.TABLE_TAXON_UNITY)


def export_criterion(request):
    """
    Export criterion table from DataBase to mobile
    """
    return export_data(request, settings.TABLE_CRITERION)

    
def export_user(request):
    """
    Export user table from DataBase to mobile
    """
    return export_data(request, settings.TABLE_USER)

      
def export_data(request, table_name):
    """
    Export table_name data from DataBase to JSON
    """
    if not check_token(request):
        print "You're not allowed to retreive information from this webservice"
        return HttpResponse()
    
    # Get infos 
    response_objects = []
    json_table_name = settings.FAUNE_TABLE_INFOS.get(table_name).get('json_name')
    response_content = {json_table_name: []}
    
    get_data_object(response_objects, table_name)

    response_content[json_table_name] = response_objects
    
    response = HttpResponse()
    simplejson.dump(response_content, response,
                ensure_ascii=False, separators=(',', ':'))
                
    # get a string with JSON encoding the list
    s = simplejson.dumps(response_content, ensure_ascii=True, encoding='utf-8')
    f = open('/home/sbe/tmp/'+table_name+".json", 'w')
    f.write(s + "\n")
    f.close()
                
    return response


def check_token(request):
    """
    Check the validity of the token
    """
    
    # TODO : uncomment this code
    return True
    #if request.method == 'POST':
    #    if request.POST['token']:
    #        if request.POST['token'] == settings.TOKEN :
    #            return True
    #return False

        
    
def get_data_object(response_content, table_name):
    """
    Perform a SELECT on the DB to retreive infos on associated object
    Param: table_name : name of the table
    """

    select_columns = settings.FAUNE_TABLE_INFOS.get(table_name).get('select_col')
    select_string = "SELECT %s FROM %s" \
                    % (select_columns, table_name)

    cursor = query_db(select_string)
    for row in cursor.fetchall():
        data = zip([ column[0] for column in cursor.description], row)
        feat_dict = SortedDict({})
        fid = ""
        for attr in data:
            key = attr[0]
            val = attr[1]
            if type(val).__name__ == "date":
                val = val.strftime("%d/%m/%Y")

            new_key = settings.FAUNE_TABLE_INFOS.get(table_name).get('db_to_json_columns').get(key)
            
            feat_dict[new_key] = val

        response_content.append(feat_dict)

    