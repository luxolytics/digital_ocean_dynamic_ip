from requests import get, post, put
import json
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

ip = get('https://api.ipify.org').text
print('Current ip is ', ip)

headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer YOUR_OAUTH_TOKEN'}
records = get('https://api.digitalocean.com/v2/domains/MYDOMAIN.COM/records', headers=headers).json()['domain_records']
for record in records:
    if record['type'] == 'A':
        id = record['id']
        url = 'https://api.digitalocean.com/v2/domains/MYDOMAIN.COM/records/' + str(id)
        data = json.dumps({'data': str(ip)})
        update = put(url, headers=headers, data=data).json()
        print(update)
