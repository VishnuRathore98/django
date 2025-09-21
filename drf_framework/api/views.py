import json
from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Product

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

@api_view(["GET"])
def get_product(request):
    product_model = Product.objects.all().order_by("?").first()
    
    product_data = {}
    if product_model:
        # Converting the model directly into dict and sending as JsonResponse
        product_data = model_to_dict(product_model, fields=['id','title','price'])


    return Response(product_data)

