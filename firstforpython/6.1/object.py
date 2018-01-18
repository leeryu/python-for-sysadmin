class Person():
    def __init__(self, name):
        self.name = name        

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

sanguck = EmailPerson('sanguck', 'sexyuck@gmail.com')
# print(sanguck.name)
# print(sanguck.email)

class Car():
    def exclaim(self):
        print("I'm a Car!")

# 상속, 메서드 재정의
class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo")
    def need_a_push(self):
        print("A little help here?")

# give_me_a_car = Car()
# give_me_a_yugo = Yugo()

# give_me_a_yugo.exclaim()
# give_me_a_yugo.need_a_push()

# 6.8 get/set 속성값과 프로퍼티
# class Duck():
#     def __init__(self, hidden_name):
#         self.hidden_name = hidden_name
#     @property
#     def name(self):
#         print('inside the getter')
#         return self.hidden_name
#     @name.setter
#     def name(self, hidden_name):
#         print('inside the setter')
#         self.hidden_name = hidden_name    

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

# circle = Circle(20)    
# print(circle.diameter)
# circle.radius = 30
# print(circle.diameter)
# circle.diameter = 30

# 6.9 private 네임 맹글링
class Ori():
    def __init__(self, input_name):
        self.__name = input_name
    @property 
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


# 6.10 메서드 타입
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects")

class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')

# CoyoteWeapon.commercial()

# 6.11 덕 타이핑
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'
class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

# hunter = QuestionQuote("sanguck", "who are you")
# answer = ExclamationQuote("answer", "me")

# brook = BabblingBrook()

# def who_says(obj):
#     print(obj.who(), 'says', obj.says())

# who_says(hunter)
# who_says(answer)

# 특수 메서드
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return "Word('" + self.text + "')"

# first = Word('ha')
# second = Word('HA')
# third = Word('eh')

# first
# print(first)

# 6.13 컴포지션

class Bill():
    def __init__(self, description):
        self.description = description;
class Tail():
    def __init__(self, length):
        self.length = length
class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', 
            self.tail.length, 'tail')
        
tail = Tail('long')
bill = Bill('wide orange')

duck = Duck(bill, tail)
duck.about()