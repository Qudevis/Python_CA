numbers = [3.14159, 2.71828, 1.41421, 0.57721, 1.61803]

# Define the width for each column
width = 10

# Print the header
print(f'{"Number":>{width}}')

# Print each number with specified precision and alignment
for number in numbers:
    print(f'{number:>{width}.2f}')
    
with open("test.txt", 'w+') as f:
    f.write("Hello")

def hello_name(name):
  return f"Hello {name}!"


print(hello_name("Justas"))


def myfunc(word):
    result = str()
    for index,letter in enumerate(word):
        if index % 2 == 0:
            result += letter.upper()
        else:
            result += letter.lower()
    return result
print(myfunc("Hello"))

def paper_doll(word):
    return ''.join([letter*3 for letter in word])

print(paper_doll("Hello"))

print('007' in '14075')

import os
os.system('cls')

class TestAC():
    def __init__(self) -> None:
        self.test = "Hi"
        self.test2 = "OK"
    def say(self):
        print(self.test)
    def __len__(self):
        return 5

my_class = TestAC()

print(len(my_class))