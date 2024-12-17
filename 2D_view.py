class point:
    def __init__(self,x,y):
        self.x_cord = x
        self.y_cord = y
        
    def __str__(self):
        return "<{},{}>".format(self.x_cord,self.y_cord)
    
    def distance(self,other):
        return ((self.x_cord - other.x_cord)**2 + (self.y_cord - other.y_cord)**2)**0.5
    
    def dist_from_origin(self):
        return self.distance(point(0,0))
    
class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
        
    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)
    
    def lie_on_line(line,point):
        if line.A*point.x_cord + line.B*point.y_cord + line.C == 0:
            return "point lies on line"
        else:
            return "point does not lie on line"
        
    def short_distance(line,point):
        return abs(line.A*point.x_cord + line.B*point.y_cord + line.C)/(line.A**2 + line.B**2)**0.5
             
    def line_intersection(l1,l2):
        #line intersction formula (x, y) = ((b1c2-b2c1)/(a1b2-a2b1), (c1a2-c2a1)/(a1b2-a2b1))
        return  ((l1.B*l2.C - l2.C*l1.C)/(l1.A*l2.B - l2.A*l1.B),(l1.C*l2.A - l2.C*l1.A)/(l1.A*l2.B - l2.A*l1.B))
     
         
l1 = Line(11,11,-22)
l2 = Line(1,2,3)
print(l1.line_intersection(l2))