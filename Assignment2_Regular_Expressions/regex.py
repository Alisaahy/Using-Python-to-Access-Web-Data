'''
In this assignment you will read through and parse a file with text and numbers.
You will extractall the numbers in the file and compute the sum of the numbers.
'''

import re
file = open('regex_sum_511301.txt')
sum = 0
for line in file:
    number = re.findall('[0-9]+', line)
    for n in number:
        sum += int(n)
print(sum)
