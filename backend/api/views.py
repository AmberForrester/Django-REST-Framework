from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

# Django REST Framework API VIEW - 
@api_view(['POST']) # POST method there to ingest data as secure as possible
def api_home(request, *args, **kwargs): 
    
    """ DRF API VIEW """
    
    # Makes sure the data being sent to API endpoint, matches hthe requirements of the serializer and the model. 
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        print(serializer.data)
        data = serializer.data
        return Response(serializer.data)
    return Response({'invalid': 'not good data'}, status=400)
    
    
    
    
    
    
    
    
    # Process of serialization: take a representation of model instance (model_data) -> we want to turn it into a Python Dict -> return JSON to my client
    # Take a manual approach to the JsonResponse: 
    # Convert Django Model instance to Dict 
    # import json
    # from django.http import JsonResponse
    """ def api_home(request, *args, **kwargs): 
    
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price']) # Clean and easy way to narrow down data from a Model Instance
    
    return JsonResponse(data) """

    
    # return JsonResponse(data): accepts a Dict as an argument
    
    #   json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={'content-type'}: 'application/json'): accepts a string 
    # Then error occurs with price, needing to change its serialization ... which is why manually doing things can be tricky, the solution = framework
    
    
   
    """ model_data = Product.objects.all().order_by('?').first()
    data = {}
    
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content 
        data['price'] = model_data.price 
        
        
    return JsonResponse(data) """
    


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