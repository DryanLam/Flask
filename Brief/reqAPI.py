import requests
import json


def doGet(_url, _params, _headers={}):
    r = requests.get(url=_url, params=_params, headers=_headers) 
    # extracting data in json format 
    data = r.json() 
    return data


def doPost(_url, _payload, _headers={}):
    r = requests.post(url=_url, data=json.dumps(_payload), headers=_headers) 
    data = r.json()
    return data


end_point_01 = "http://localhost:3500/api/v1/pricing"
end_point_02 = "http://localhost:3500/api/v1/order"
# query={}
# data = {"user": "Dryan", "amt": 1, "cost": 999}
# headers = {"Token": "name", "Content-Type": "application/json"}

# rs = doGet(end_point_01, query, headers)

# print(rs['cost'])
# print(doPost(end_point_02, data, headers))


data = {'user': 'abc@gmail.com', 'amt': 1, 'cost': 999}
headers = {'Token': 'BEFB-4A5DB5813D03657676653343C675C06E', 'Content-Type': 'application/json'}

print(doPost(end_point_02, data, headers))
