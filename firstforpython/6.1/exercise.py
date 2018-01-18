import collections

class Thing():
    pass
class Thing2():
    def __init__(self, letters):
       self.letters = letters 
class Thing3():
    def __init__(self, letters):
        self.letters = letters
    @property
    def letters(self):
        return self.letters
    @letters.setter
    def letters(self, letters):
        return self.letters

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def to_string(self):
        print('name : ', self.name, 'symbol : ', self.symbol,
            'number : ', self.number)

el_dict = {
    'name': 'Hydrogen',
    'symbol': 'H',
    'number': 1
}

element = collections.namedtuple("Element", el_dict)

print(element.number)


