class Person:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        introduction = f"Hey I am {self.name}, I am {self.age} and I am a {self.gender}"
        return introduction
    
p1 = Person('Gary',12,'Male')

print(p1.introduce())