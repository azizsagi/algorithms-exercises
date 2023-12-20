class Calculator:

    @staticmethod
    def add(a: int, b:int)->int:
        return a + b
    

cal = Calculator()

print(cal.add(5,5))