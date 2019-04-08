import requests

URL = 'http://path-routing-test.appspot.com/'

status_codes = 0
status_codes += requests.get(URL + 'hello').status_code
status_codes += requests.get(URL + 'world').status_code

print "status_codes value is ", status_codes

if status_codes != 400:
    exit(-1)
else:
    exit(0)