class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def add(self):
        print(self.address.city,self.address.pin,self.address.state)    
class Address:
    def __init__(self,city,pin,state):
        self.city = city
        self.pin = pin
        self.state = state

ad1 = Address('peshawar',1122,'KPK')
c1 = Customer('ali','male',ad1)  
c1.add()          