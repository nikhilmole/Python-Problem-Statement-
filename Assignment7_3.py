class Arithematic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter first value :")
        self.Value1 = int(input())
        print("Enter second number :")
        self.Value2 = int(input())

    def Addition(self):
        self.Result = self.Value1 + self.Value2
        return self.Result

    def Substraction(self):    
        self.Result = self.Value1 - self.Value2
        return self.Result

    def Multiplication(self):
        self.Result = self.Value1 * self.Value2
        return self.Result

    def Division(self):   
        try:     
            self.Result = self.Value1 / self.Value2
            return self.Result

        except ZeroDivisionError as zobj:
            print("")
        

def main():
    aobj = Arithematic()

    aobj.Accept()
    Ad_Result = aobj.Addition()
    Sub_Result = aobj.Substraction()
    Multi_Result = aobj.Multiplication()
    Div_Result = aobj.Division()

    print("Addition is :",Ad_Result)
    print("Substraction is :",Sub_Result)
    print("Multiplication is :",Multi_Result)
    print("Division is :",Div_Result)

if __name__ == "__main__":
    main()