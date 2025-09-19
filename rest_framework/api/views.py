import json
from django.shortcuts import render
from django.http import JsonResponse
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

def get_product(request):
    product_model = Product.objects.all().order_by("?").first()
    
    product_data = {}
    if product_model:
        product_data['id'] = product_model.id
        product_data['title'] = product_model.title
        product_data['content'] = product_model.content
        product_data['price'] = product_model.price

    return JsonResponse(product_data)
