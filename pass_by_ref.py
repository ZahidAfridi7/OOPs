class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

def greet(person):
    print(id(person))
    print('hello ',person.name,'you are ',person.gender)

p = Person('ali','male')
print(id(p))
print(p.name)
greet(p)            