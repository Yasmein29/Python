class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calculate_addition(self):
        result = self.num1 + self.num2 + self.num3
        print(f"The addition of {self.num1}, {self.num2}, and {self.num3} is: {result}")