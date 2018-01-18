from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')

# 키워드 인자다
parts = {'bill': 'wide orange', 'tail' : 'long'}

duck2 = Duck(**parts)

print(duck2)