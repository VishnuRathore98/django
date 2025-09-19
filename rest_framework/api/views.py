import json
from django.shortcuts import render
from django.http import JsonResponse

def api_home(request, *args, **kwarg):
    # JSON data -> request.body
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # converting byte data to json
    except:
        pass

    data['params']=dict(request.GET) # Getting the query params
    data['headers']=dict(request.headers) # Getting the headers
    data['content_type']=request.content_type # Getting the content_type

    return JsonResponse(data)
