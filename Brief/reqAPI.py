import requests
import json


def doGet(_url, _params, _headers={}):
    r = requests.get(url=_url, params=_params, headers=_headers) 
    # extracting data in json format 
    data = r.json() 
    return data


def doPost(_url, _payload, _headers={}):
    r = requests.post(url=_url, data=json.dumps(_payload), headers=_headers) 
    data = r.text 
    return data


# end_point = "http://localhost:3500/api/v1/pricing"
end_point = "http://localhost:3500/api/v1/order"
data = {"user": "Dryan", "amt": 1, "cost": 999}
headers = {"Token": "name", "Content-Type": "application/json"}

print(doGet(end_point, data, headers))
print(doPost(end_point, data, headers))