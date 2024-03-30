print('I am Client .....')

import json
import requests

IP = 'localhost'
port = '5001'
connect = IP+':'+port

headers = {'Content-Type': 'application/json'}

data_dict = {'first_name':'Muhammad Shoaib', 'last_name':'Sikander', 'age':32, 'height':177.8}
data_person = json.dumps(data_dict)

#r = requests.get('http://'+connect+'/Person_Info')
#print(r)

response = requests.get('http://'+connect+'/Person_Info', headers=headers, data=data_person)
print(response)
#response = response.json()
print(response)