import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs): # This request being passed through is an HttpRequest instance from Django.
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
