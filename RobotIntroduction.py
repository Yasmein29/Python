class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hello, I am {self.name}."  

tom = Robot("Tom")
jerry = Robot("Jerry")

print(tom.introduce())
print(jerry.introduce())