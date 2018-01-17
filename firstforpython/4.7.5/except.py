short_list = [1, 2, 3]

class UppercaseException(Exception):
    pass

words = ['apple', 'tomato', 'MO']

for word in words:
    if word.isupper():
        raise UppercaseException(words)

