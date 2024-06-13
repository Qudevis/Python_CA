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


class Student:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.deleter
    def score(self):
        del self._score

Mark = Student()
text = "Hi"
print(Mark.score)

# Mark._score = 18 NENAUDOJAMAS

print(Mark.score)

