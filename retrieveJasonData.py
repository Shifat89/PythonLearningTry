import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
totalSum=0
cnt=0
for item in js["comments"]:
    val = item["count"]
    number=int(val)
    totalSum=totalSum+number
    cnt=cnt+1

print("count: ", cnt)
print('Sum: ',totalSum)




