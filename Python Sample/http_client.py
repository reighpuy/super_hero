import http.client
import mimetypes

conn = http.client.HTTPSConnection("www.superheroapi.com")
payload = ''
headers = {
  'Cookie': '(cooki)'
}
conn.request("GET", "/api.php/(api_key_mu/(nomor_hero)/powerstats", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))