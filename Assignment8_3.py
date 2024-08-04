class Numbers:
    def __init__(self):
        self.Value = 0
        print('Enter number')
        self.Value = int(input())

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, self.Value,1):
            if ((self.Value % i) == 0):
                return False
        else:
            return True

    def ChkPerfect(self):
        sum_factors = 0
        for i in range(1, self.Value,1):
            if ((self.Value % i) == 0):
               sum_factors = sum_factors + i
        return sum_factors == self.Value

    def Factors(self):
        factors = []
        for i in range(1, self.Value,1):
            if ((self.Value % i) == 0):
                factors.append(i)
        return factors

    def SumFactors(self):
        sum_factors = 0
        for i in range(1, self.Value, 1):
            if ((self.Value % i) == 0):
                sum_factors = sum_factors + i
        return sum_factors

def main():
    obj = Numbers()
    print("Is Prime:", obj.ChkPrime())
    print("Is Perfect:", obj.ChkPerfect())
    print("Factors:", obj.Factors())
    print("Sum of Factors:", obj.SumFactors())

if __name__ == "__main__":
    main()
