# class MyLocator:
#     MY_ID="id"
#     MY_NAME = "name"

# mailId='john@gmail.com'
# print(mailId[0:2])

# class A:
#     def __init__(self,name):
#         self.name=name
#
# a1=A("john")
# a2=A("john")
#
# print(a1)
# print(a2)
#
# print(id(a1))
#
# print(id(a2))
# A()
# A()
# obj = A()

# str1="python language"
# str1.replace("python","p")
# print(str1)

class Program:
    def __init__(self, colors):
        self.colors = colors
        for color in self.colors:
            print(color)
            break


p=Program(['red', 'black', 'blue'])


class Teacher:
    def __init__(self, id, age):
        self.id = id
        self.age = age
        print(self.age)


tear = Teacher("John", 20)
tear.age = 50
print(tear.age)


class Program:
    def __init__(self, colors):
        self.colors = colors
        for color in self.colors:
            print(color)
            break


p = Program(['red', 'black', 'blue'])