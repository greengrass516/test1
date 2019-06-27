import random

print(random.randint(1,5))

a = 10

def add(x,y):
    print(x+y)

class Father():
    def __init__(self,name):
        print("__init__",id(self))
        # self代表当前对象
        self.name = name

    def __del__(self):
        print("__del__")

    def show(self):
        print("name:",self.name)

class Son(Father,object):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"name:{self.name}age:{self.age}")

#print(__name__)
if __name__ == "__main__":
    s = Son("AAA",18)
    s.show()