#method overloading does not work in python
class Shape:
    def area(self,radius):
        return 3.14 * radius*radius
    def area(self,l,b):
        return l*b
s = Shape()
s.area(2)
s.area(1,2) 

"this code will not run"    