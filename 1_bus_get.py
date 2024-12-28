import requests
import json
url = "https://ctumobileapi.amnex.com/ListofLocations/GetLocations_v1?lan=en"
header = {
    "User-Agent":"Nasa"
}
data = requests.get(url,headers=header)
print(data)
#print(data.text)
json_d = json.loads(data.text)
a = json.loads(json_d["data"])
print(a[0])

