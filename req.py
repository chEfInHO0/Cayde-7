import requests as req

API_key = open('./tokens/BungieAPI_key.txt','r').read()
id = 11594260
url = f"https://www.bungie.net/Platform/User/GetBungieNetUserById/{id}"


headers = {
  'x-api-key': f'{API_key}',
  'Authorization': 'Basic NDU0NTc6'
}

response = req.request("GET", url, headers=headers)

print(response.text)
