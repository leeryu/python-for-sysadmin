import re
source = 'Young Frankenstein'
m = re.match('You', source)

if m:
    print(m.group())

m = re.match('^You', source)

if m:
    print(m.group())
