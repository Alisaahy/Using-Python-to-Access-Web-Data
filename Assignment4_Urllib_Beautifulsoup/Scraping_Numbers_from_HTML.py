'''
Scraping Numbers from HTML using BeautifulSoup
In this assignment you will write a Python program
similar to http://www.pythonlearn.com/code/urllink2.py.
The program will use urllib to read the HTML from the data files below,
and parse the data, extracting numbers and compute the
sum of the numbers in the file.
We provide two files for this assignment.

Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_353539.html (Sum ends with 63)

You do not need to save these files to your folder since your program
will read the data directly from the URL. Note: Each student will have a
distinct data url for the assignment - so only use your own data url for analysis.
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html = urlopen('http://py4e-data.dr-chuck.net/comments_511303.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
sum = 0
coun = 0
for tag in tags:
    coun += 1
    sum += int(tag.contents[0])
print('Count', coun, '\nSum', sum)
