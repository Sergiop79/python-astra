import re
from urllib2 import urlopen
request = urlopen('http://cualesmiip.com/')
busqueda = re.search('Tu IP real es ([\d.]+)', request.read())
print busqueda.groups()[0]
