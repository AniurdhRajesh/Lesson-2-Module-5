class Employee():
    def __init__(self):
        print("Hello My name is Bob")
    def bob(self,name):
        self.name=print("Hello my name is Bob")
    def __del__(self):
        print("Employee record of Bob is now deleted")
obj=Employee()
obj.bob()
del obj