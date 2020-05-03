import requests

url = "https://www.superheroapi.com/api.php/(api_key_mu)/(nomor_hero)/powerstats"
payload = {}
headers = {
  'Cookie': '(cookie)'
}
response = requests.request("GET", url, headers=headers, data = payload)
print(response.text.encode('utf8'))