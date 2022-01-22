import re


text = 'UPPER, PYTHON, lower python, Mixed Python'
print(re.findall('python', text, re.I))
print(re.findall('python', text, re.IGNORECASE))