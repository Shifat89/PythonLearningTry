import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print ("Retrieving " + url)
xml = urllib.request.urlopen(url).read()
print ("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)
counts = tree.findall('.//count')
print("Count: " + str(len(counts)))
Totalsum = 0
for count in counts:
     no = int(count.text)
     Totalsum=Totalsum+no

print('Sum: ', Totalsum)
