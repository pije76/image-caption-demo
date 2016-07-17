from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import subprocess
import json 
import os
import sys


def parse_json(json_path):
    sentences = []
    json_file = open(json_path) 
    for line in json_file:
        json_obj = json.loads(line)
        for i in range(len(json_obj)):
            sentences.append(json_obj[i]['caption'])
            
    return sentences
    
def index(request):
	return render_to_response('index.html')	

def demo(request):
    sentences = "" 
    imgs_saved_path = 'video_cap/static/imgs/liqing/images/'
    json_path = 'vis/vis.json'
    try: 
        os.remove(json_path)
    except:
        pass
    #upload file to images saved directory.
    if request.method == "POST":
        f = request.FILES['tmp_image'] 
        with open(imgs_saved_path + 'tmp.jpg', 'wb+') as dest:
            for chunk in f.chunks():
                dest.write(chunk)
    
        try:
            result = subprocess.call(['bash', 'run_test.sh']) 
        except:
            a = sys.exc_info()[0]
            assert False
        if result == 0:
            print('all_ok')
            sentences = parse_json(json_path) 
        else:
            assert False
    
    return render_to_response('demo.html', {'sentences':sentences}, context_instance=RequestContext(request))
    
    #parse json file,get stenences
    

def theory(request):
	return render_to_response('theory.html')	

def about(request):
	return render_to_response('about.html')	

