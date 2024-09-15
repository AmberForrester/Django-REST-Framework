import requests

# We want to control the endpoint of what someone will see.
endpoint = 'http://localhost:8000/' # http://127.0.0.1:8000/

# HTTP Library for Python
get_response = requests.get(endpoint, json={'query':'Hello World'}) # HTTP Request
print(get_response.text)# print raw test response - data that your application can use.
print(get_response.status_code)



# API Application Programming Interface - (function) or Method that is built into it.
# Using this library is like using another form of an API.

# This command will run the Python script in the Terminal and display the responses from the requests library in the terminal: python 'file_name'.py

# REST API's : Web based API, using HTTP Request. 
# Web API allows your application to work with another application with some sort of internet request. 


# HTTP Request = HTML ouput for humans to look at. 
# REST API HTTP Request = JSON data or maybe (xml/other formats) - meant for software to communicate with eachother over the web.

""" endpoint = 'https://httpbin.org/status/200/'
endpoint = 'https://httpbin.org/anything'

# HTTP Library for Python
get_response = requests.get(endpoint) # HTTP Request
print(get_response.text) # print raw test response - data that your application can use.  """

# JSON = JavaScript Object Notation almost a Python Dict, but slightly different.
# This data pasted below is a valid Python Dict with the exception of the "json": null. 
""" {
  "args": {},
  "data": "",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.32.3",
    "X-Amzn-Trace-Id": "Root=1-66e618e0-06915ccd78dc43b81ee8e083"
  },
  "json": null, 
  "method": "GET",
  "origin": "99.228.197.87",
  "url": "https://httpbin.org/anything"
} """

""" # If it is JSON, you can run this:
endpoint = 'https://httpbin.org/status/200/'
endpoint = 'https://httpbin.org/anything'

get_response = requests.get(endpoint) # HTTP Request
get_response = print(get_response.json())# now able to print this out as a Python Dict seen below: """

""" {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-66e61c57-283844a80cae6e2145809fb3'}, 'json': None, 'method': 'GET', 'origin': '99.228.197.87', 'url': 'https://httpbin.org/anything'} """
# This time the 'json': is declared as None and no longer null. 


# Using the HTTP Library for Python: you can actually pass in your own json data:
""" endpoint = 'https://httpbin.org/status/200/'
endpoint = 'https://httpbin.org/anything'

get_response = requests.get(endpoint, json={'query':'Hello World'}) # HTTP Request
get_response = print(get_response.json()) """

# Now will echo back what was sent to it, as seen below:
""" {'args': {}, 'data': '{"query": "Hello World"}', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '24', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-66e61d64-4d90cf102c6670d51be1f21a'}, 'json': {'query': 'Hello World'}, 'method': 'GET', 'origin': '99.228.197.87', 'url': 'https://httpbin.org/anything'} """

# print(get_response.headers)
# print(get_response.status_code)