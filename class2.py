class student:
    grade = 10
    name = "Yasmein"

    def intro(self):
        print("Hey, I'm a student")
    def detail(self):
        print("My name is ", self.name)
        print("I' in grade", self.grade)
ob = student()
ob.intro()
ob.detail()