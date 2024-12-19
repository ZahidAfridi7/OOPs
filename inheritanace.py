# class User:
#     def __init__(self):
#         self.name = 'ali'
        
#     def login(self):
#         print('login')

# class Student(User):
#     # def __init__(self):
#     #     self.rollno = 100
    
#     def enroll(self):
#         print('enroll into the course')


# st = Student()
# u = User()
# print(st.name)
# st.login
# st.enroll
# # st.rollno            
            
# class Parent:
#     def __init__(self,num):
#         self.__num = num
        
#     def get__num(self):
#         return self.__num
    
# class Child(Parent):
#     def show(self):
#         print("this is child class")

# c = Child(100)
# print(c.get__num()) 
# c.show()       
          
class Parent:
    def __init__(self,num):
        self.__num = num
    
    def get_num(self):
        return self.__num   

class Child(Parent):
    def __init__(self, num,val):
        super().__init__(num)
        self.__val = val
    def get_val(self):
        return self.__val
    
c = Child(100,200)
print(c.get_num())
print(c.get_val())            