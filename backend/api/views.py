import json
from django.http import JsonResponse

from products.models import Product

def api_home(request, *args, **kwargs): 
    
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content 
        data['price'] = model_data.price 
        # Process of serialization: take a representation of model instance (model_data) -> we want to turn it into a Python Dict -> return JSON to my client
        
        # Take a manual approach to the JsonResponse: 
           
    return JsonResponse(data)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """ # This request being passed through is an HttpRequest instance from Django.
    # print(dir(request))
    # request.body
    
    #Json data from request.body
    print(request.GET) # get your url query params 
    # print(request.POST)
    body = request.body # byte string of JSON data
    data = {}
    try: # try block added because the body could not have any JSON data.
        data = json.loads(body) # takes in string of JSON data and turns it into Python Dict.
    except:
        pass
    print(data)
    
    data['headers'] = dict(request.headers) # include headers
    data['params'] = dict(request.GET)
    data['content_type'] = request.content_type
    
    return JsonResponse(data)

# Highlight what to know on any given View on Django, using JSON responses
# For examples the data ['headers'] could not be converted to JSON data, so we need to manually input the dict(request.headers)
 """