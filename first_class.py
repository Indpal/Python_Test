class Person:
    def __init__(self,first_name,last_name,age):
        #instance variable
        print("init method called")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Indranil','palit','24')
p2 = Person('Random2','Random2','12')


print(p1.first_name)
