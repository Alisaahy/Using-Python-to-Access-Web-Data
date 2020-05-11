'''
In this assignment you will write a Python program that expands on
http://www.pythonlearn.com/code/urllinks.py.
The program will use urllib to read the HTML from the data files below,
extract the href= vaues from the anchor tags,
scan for a tag that is in a particular position relative to the first name in the list,
follow that link and repeat the process
a number of times and report the last name you find.

Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1).
Follow that link. Repeat this process 4 times.
The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah

Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Blanka.html
Find the link at position 18 (the first name is 1).
Follow that link. Repeat this process 7 times.
The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: L
'''

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('url: http://py4e-data.dr-chuck.net/known_by_Marcia.html')
print('count: 7')
print('position: 18')
url = input('Enter - ')
count = int(input('Enter count - '))
position = int(input('Enter position - '))
print('Retrieving: ', url)

# Retrieve all of the anchor tags
for times in range(int(count)):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    # Retrieve anchor tags
    tags = soup('a')
    print('Retrieving: ', tags[position-1].get('href', None))
    url = tags[position-1].get('href', None)
