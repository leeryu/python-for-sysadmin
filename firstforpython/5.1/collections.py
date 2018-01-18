import sys

# 5.5.4 스택 + 큐 == 테크
# 


# 5.5.5 : itertools
import itertools

for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

# for item in itertools.cycle([1, 2]):
#     print(item)

for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

# 5.5.6 : pprint()
import pprint

quotes = {
    'Moe': 1, 
    'A wise guy,': 2, 
    'Larry':3 
}

