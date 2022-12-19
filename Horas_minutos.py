#ip address locator python?     

import re
import json
from urllib2 import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

print('Your IP detail\n ')
print('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'
.format(org,region,country,city,IP))






# tiempo = float(input("Digite el tiempo en segundos: "))

# minutos = tiempo/60
# horas = tiempo/3600

# print(f"{tiempo} segundos en minutos: {minutos:.2f} y {tiempo} segundos en horas: {horas:.2f}")