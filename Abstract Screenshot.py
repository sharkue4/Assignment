import requests

url = "https://vat.abstractapi.com/v1/validate/?api_key=f7c1ba136f204d27848646142d496656&vat_number=SE556656688001"

payload={}
headers = {
  'Authorization': 'api_key f7c1ba136f204d27848646142d496656'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
