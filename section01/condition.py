# if文
if 1 == 1:
    print("True")
else:
    print("False")


# for
for i in range(5):
    print(i)

# function

def say_hello(message: str) -> str:
    print("Hello!")
    return message + "!"

say_hello("Hello")

# class

class Animal:
    def __init__(self, name: str):
        self.name = name

    def say_hello(self):
        print("Hello, " + self.name)


animal = Animal("Taro")
animal.say_hello()

# import