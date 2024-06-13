# class Student:
#     def __init__(self):
#         self._score: int = 0

#     @property
#     def score(self) -> int:
#         print("getting")
#         return self._score

#     @score.setter
#     def score(self, s: int) -> None:
#         if 0 <= s <= 100:
#             self._score = s
#         else:
#             raise ValueError('The score must be between 0 ~ 100!')

#     @score.deleter
#     def score(self) -> None:
#         print("Deleting")
#         del self._score

# Tom = Student()

# print(Tom.score)


# Tom.score = 15

# # ValueError: The score must be between 0 ~ 100!

# class C(object):

#     @property
#     def x(self):
#         return self._x

#     @x.setter
#     def x(self, value):
#         self._x = value

#     @x.deleter
#     def x(self):
#         del self._x

#     @property
#     def y(self):
#         return self._y

#     @y.setter
#     def y(self, value):
#         self._y = value

#     @y.deleter
#     def y(self):
#         del self._y

# test_class = C()
# C.x = 5
# print(C.x)

# C.y = 19

# print(C.y)


# class Student:
#     def __init__(self):
#         self._score = 0

#     @property
#     def score(self):
#         return self._score

#     @score.deleter
#     def score(self):
#         del self._score

# Mark = Student()
# text = "Hi"
# print(Mark.score)

# # Mark._score = 18 NENAUDOJAMAS

# print(Mark.score)



class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
 
    @property
    def celsius(self):
        return self._celsius 
   
    @celsius.setter
    def celsius(self, value):
        self._celsius = value # self.celsius = 15 ... aha man reikia nueiti i setteri  self.celsius = 15 ... aha man reikia nueiti i setteri  self.celsius = 15 ... aha man reikia nueiti i setteri self.celsius = 15 ... aha man reikia nueiti i setteri 
 
    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32
   
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._fahrenheit = (value -32) / 1.8
 
 
temp = Temperature(20)
text = "My text"
print(temp.celsius)

print(temp.fahrenheit)

temp.celsius = 15

my_list = [1,6,98,7,8]
print(my_list)


def sum(a,b):
    print("Hello")
    print("I am sum")
    return a + b

answer = sum(7,6)

print(sum(7,9))


for i in range(-5,20):
    print("Your number is nice and it is: ")
    print(i)



print("End")

import Paskaita_17

