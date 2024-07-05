
# class A:
#     def __init__(self,name):
#         self.name = name

# a1=A("john")

# a2=A("john")

# print(a1)

class Book:
    def __init__(self,author):
        self.author=author
book1=Book("V.M.Shah")

book2=book1

print(book2,book1)






class Student:



    def __init__(self,name,id):



        self.name=name



        self.id=id



        print(self.id)



std=Student("Simon",1)



std.id=2



print(std.id)



class A():



    def __init__(self,count=100):



        self.count=count







obj1=A()



obj2=A(102)



print(obj1.count)



print(obj2.count)


class test:

    def __init__(self,a):

        self.a=a

    def display(self):

        print(self.a)

obj=test()

obj.display()