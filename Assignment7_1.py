class Demo:
    Value = 121

    def __init__(self,no1,no2):
        self.A = no1
        self.B = no2

    def Fun(self):
        print("Inside Instance Fun Method")
        print("The value of instance variable is :",self.A)
        print("The Value of instance variable is :", self.B)
        print("The Value of class Variable:",Demo.Value)
    def Gun (self):
        print("Inside Instance Fun Method")
        print("The value of instance variable is :",self.A)
        print("The Value of instance variable :", self.B ) 
        print("The Value of class Variable:",Demo.Value)
def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()