class A:
    name ='shekhar'
# self >> self is like object that we used as parameter while declering any methods
# self can access all global level all param
# The self keyword is a reference to the current instance of the class and is used to access variables and methods that belong to the class.
# When you define a method within a class and use self as the first parameter,
# self allows that method to access and manipulate the instance attributes of the class. Here's a quick example of its use:
    
    def __init__(self,name=None):
        if name!=None:
            self.name = name

    def go(self):
        self.greet()
        print(f'Hi welcome {self.name}')

    def greet(self):
        print('--------Hello----------')

a= A('rohan')
a.go()

b= A()
b.go()