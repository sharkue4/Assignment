import requests

url = "https://api.edamam.com/api/nutrition-data?app_id=bece273d&app_key=6e9272f774d84b8baec9c279ef212307&nutrition-type=cooking&ingr=Calcium"

payload={}
headers = {
  'Authorization': 'app_key 6e9272f774d84b8baec9c279ef212307'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
