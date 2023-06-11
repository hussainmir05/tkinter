import json
import phonenumbers
from phonenumbers import geocoder
from urllib import response
from urllib.request import urlopen
x=input('enter your phone nbr')

phonenbr=phonenumbers.parse(x)
print(geocoder.description_for_number(phonenbr,'en'))
url='https://ipinfo.io/'
response=urlopen(url)
data=json.load(response)
print(data)