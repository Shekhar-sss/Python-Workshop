class Calculator:
    def __init__(self):
        self.number1 = float(input('Enter 1st Number '))
        self.number2 = float(input('Enter 2nd Number '))
        self.choice = float(input('Select operation to perform:\n1] Addition \n2] Subtraction \n3] Multiplication \n4] Division \n'))

    def calc(self):
        if self.choice==1:
            print(f'Addtion of provided number is : {self.number1+self.number2}')
        elif self.choice==2:
            print(f'Subtraction of provided number is : {self.number1-self.number2}')
        elif self.choice==3:
            print(f'Multiplication of provided number is : {self.number1*self.number2}')
        elif self.choice==4:
            try:print(f'Division of provided number is : {self.number1/self.number2}')
            except: print('ZeroDivisionError: float division by zero')

            
        else: print('XXXXX----- You Selected Wrong Input ----XXXXX')
    
if __name__=='__main__':
    c = Calculator()
    c.calc()