'''
In this assignment you will write a Python program somewhat similar to
http://www.pythonlearn.com/code/geoxml.py.
The program will prompt for a URL, read the XML data from that URL using urllib
and then parse and extract the comment counts from the XML data,
compute the sum of the numbers in the file.

Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_353536.xml (Sum ends with 90)
'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
uh = urllib.request.urlopen(url, context=ctx)
print('Retrieving', url)
data = uh.read()

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
sum = 0
for item in results:
    m = int(item.find('count').text)
    sum += m

print('sum', sum)
