import requests

def doGet(url, params):
    r = requests.get(url, params) 
    # extracting data in json format 
    data = r.json() 
    return data


def doPost(url, params):
    r = requests.post(url, params) 
    data = r.text 
    return data

end_point = "http://maps.googleapis.com/maps/api/geocode/json"
data = {'api_dev_key': "API_KEY", 
        'api_option':'paste', 
        'api_paste_code': "", 
        'api_paste_format':'python'} 

print(doGet(end_point, data))
print(doPost(end_point, data))

