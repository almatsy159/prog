import math
import pygame as pg

# need meta class to give id and name ...
class Point:
    id = 0
    def __init__(self,x=0.0,y=0.0,z=0.0,name=None):
        #if origin == None:
        #    origin = Point()
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.id_obj = Point.id
        Point.id += 1
    def __repr__(self) -> str:
        if self.name == None:
            self.name = "Point"
        return f"{self.name} : {self.x},{self.y},{self.z}"
    
    def pg_draw(self,screen,color="black"):
        #pg.draw.line(screen,color,(self.x-5,self.y-5),(self.x+5,self.y+5),2)
        pg.draw.circle(screen,color,(self.x,self.y),5)
        #pg.draw.line(screen,color,(self.x-5,self.y+5),(self.x-5,self.y+5),2)
        
    def rel(self,p):
        return Point(p.x+self.x,p.y+self.y,self.z+p.z)
        
        

class Droite:
    id = 0
    def __init__(self,a,b,name=None):
        self.name = name
        # a et b : Point 
        self.a = a
        self.b = b

        #self.k = self.coeff()
        #self.y0 = self.pos_y0()

        self.u = Vector(self.a.x-self.b.x,self.a.y-self.b.y,self.a.z-self.b.z)
        self.normal = self.ortho()
        self.d = self.find_d()

        self.id_obj = Droite.id
        Droite.id += 1

        if self.name == None:
            self.name = str(self.id_obj)
    """
    def coeff(self):
        k = (self.b.x -self.a.x) / (self.b.y - self.a.y)
        #self.k = k
        return k

    def pos_y0(self):
        res = self.a.x * self.k - self.a.y
        return res

    def calculate(self,x):
        return self.k * x + self.y0

    def contain(self,c):
        if c.x * self.k + self.y0 == c.y:
            return True

        else :
            return False
    """

    def contain(self,point):
        v = Vector(point.x - self.a.x, point.y - self.a.y, point.z - self.a.z)
        res = self.u.vect_prod(v)
        #print(res)
        if res.x == 0 and res.y == 0 and res.z == 0:
            return True

        else :
            return False

    def ortho(self,vector=None):
        if vector == None:
            vector = Vector(0,0,1)
        #norme = vector.normalize()
        norm_tmp = self.u.vect_prod(vector)
        self.normal = norm_tmp.normalize()
        #print(self.normal)
        return self.normal

    def find_d(self):
        d = -(self.normal.x * self.a.x + self.normal.y * self.a.y + self.normal.z + self.a.z)
        #print(f"coeff d dans l'equation de la forme ax+by+cz = -d : {d}")
        return d

    def __repr__(self):

        return f"{self.name} : {self.normal.x}x + {self.normal.y}y + {self.normal.z}z + {self.d} = 0"
    """
    def para(self,droite):
        if self.coeff == droite.coeff:
            return True
        else :
            return False
    """
class Segment:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.length = ((a.x-b.x)**2+(a.y-b.y)**2)**(1/2)
        
    def get_droite(self):
        self.droite = Droite(self.a,self.b)
        return self.droite
    
    def pg_draw(self,screen):
        pg.draw.line(screen,"black",(self.a.x,self.a.y),(self.b.x,self.b.y))
        
        
        

class Vector:
    id = 0
    def __init__(self,x=0.0,y=0.0,z=0.0):

        self.x = x
        self.y = y
        self.z = z

        if self.x == 0 and self.y == 0 and self.z == 0:
            self.nul = True
        else :
            self.nul = False

        if self.origin is not None:
            self.end_point = Point(self.x + self.origin.x,self.y + self.origin.y,self.z + self.origin.z)
        else:
            self.end_point = None

        if self.x == 0.0 and self.y==0.0 or self.y == 0.0 and self.z == 0.0 or self.x == 0.0 and self.z ==0.0:
            self.unit = True
        else :
            self.unit = False

        if self.x == 0.0 or self.y==0.0 or  self.z == 0.0:
            self.v_plan = True
        else:
            self.v_plan = False

        if not self.unit and not self.v_plan:
            self.k_xy = self.x/self.y
            self.k_yz = self.y/self.z
            self.k_xz = self.x/self.z
        elif not self.v_plan: # must define k_unit ...
            self.k_xy = None
            self.k_xz = None
            self.k_yz = None


        self.id_obj = Vector.id
        Vector.id += 1

    def colineaire(self,other):
        if other.nul == True:
            return True,0
        if other.x==0 or other.y==0 or other.z == 0:
            print("attetion coplanaire (,co espace ??)!")
            #raise "divzero ... l139"
            #si o.param == self.param == 0 => coplanaire
            if self.x == 0 or self.y == 0 or self.z == 0:
                return False
            return False
        k_x = self.x / other.x
        k_y = self.y / other.y
        k_z = self.z / other.z
        if k_x == k_z and k_x == k_y:
            return True,k_x
        else :
            return False,None

    def vect_prod(self,other):
        return Vector(
        self.y * other.z - self.z * other.y,
        self.z * other.x - self.x * other.z,
        self.x * other.y - self.y * other.x)

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def dot_product(self,other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def magnitude(self):
        return math.sqrt(self.dot_product(self))

    def normalize(self):
        if self.nul == False:
            return self/self.magnitude()
        else :
            return "This vector is nul !!!"

    def __add__(self,other):
        return Vector(self.x + other.x,self.y+other.y,self.z+other.z)

    def __sub__(self,other):
        return Vector(self.x -other.x,self.y-other.y,self.z-other.z)

    def __mul__(self,other):
        assert not isinstance(other,Vector)
        return Vector(self.x * other,self.y*other,self.z*other)

    def __rmul__(self,other):
        assert not isinstance(other,Vector)
        return Vector(self.x * other,self.y*other,self.z*other)

    def __truediv__(self,other):
        assert not isinstance(other,Vector)
        return Vector(self.x / other,self.y/other,self.z/other)
    
    def draw_pg(self,screen,p,k=1):
        pass
        #pg.draw.line(screen,"white",(p.x,p.y),(p.x+k*self.x,self.y*k+p.y))
        
        
    

class Plan:
    id = 0
    def __init__(self,a,b,c,name=None):
        self.id_obj = Plan.id
        Plan.id += 1
        if name == None:
            name = str(self.id_obj)
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        # need to check if ab.u et ac.u aren't colinear
        self.ab = Droite(self.a,self.b)
        self.ac = Droite(self.a,self.c)
        #if self.ab.u.colineaire(self.ac.u):
        #    raise
        #self.bc = Droite(self.b,self.c)
        self.normal = self.ab.u.vect_prod(self.ac.u)
        if self.normal.nul == True:
            print("Error Normal Nul ! Maybe AB and AC are colinear (actually not checked...)")
        self.k = -(self.normal.x * self.a.x + self.normal.y * self.a.y + self.normal.z * self.a.z)
        #print(self.k)
        # k1 = k2 = k3
        #self.k2 = -(self.normal.x * self.b.x + self.normal.y * self.b.y + self.normal.z * self.b.z)
        #self.k3 = -(self.normal.x * self.c.x + self.normal.y * self.c.y + self.normal.z * self.c.z)
        #print(self.k2,self.k3)
        print(self.normal)

    def contain(self,obj):
        if isinstance(obj,Point):
            point = obj
            #print(self.normal.x * point.x + self.normal.y * point.y + self.normal.z * point.z + self.k)
            if self.normal.x * point.x + self.normal.y * point.y + self.normal.z * point.z + self.k == 0:
                return True
            else :
                return False

        elif isinstance(obj,Droite):
            pass
        else:
            return f"Not Handling {obj.type}"

    def intersection(self,obj):
        if isinstance(obj,Droite):
            pass
        elif isinstance(obj,Plan):
            pass
"""
class Surface:
    def __init__(self,lst_point):
        self.points = lst_point
        if len(lst_point) >= 3:
            self.plan = None
            #self.points = []
            for i,p in enumerate(lst_point):
                if i <= 3:
                    exec(f"self.p{i}={p}")
                    #self.points.append(p)
                else:
                    if not self.plan.contain(p):
                        raise
                    #else :
                    #    self.points.append(p)
                if i == 3 :
                    self.plan = Plan(self.p1,self.p2,self.p3)
        else :
            raise ValueError

        x_min = None
        y_min = None
        z_min = None
        x_max = 0
        y_max = 0
        z_max = 0
        for p in self.points:
            if x_min == None or x_min > p.x:
                x_min = p.x
            if y_min == None or y_min > p.y:
                y_min = p.y
            if z_min == None or z_min > p.z:
                z_min = p.z
            if x_max < p.x:
                x_max = p.x
            if y_max < p.y:
                y_max = p.y
            if z_max < p.z:
                z_max = p.z

        self.x_max = x_max
        self.y_max = y_max
        self.z_max = z_max
        self.x_min = x_min
        self.y_min = y_min
        self.z_min = z_min
        self.lst_min_max = [self.x_min,self.y_min,self.z_min,self.x_max,self.y_max,self.z_max]

    def get_rect(self):

        return Surface()
        """

class Espave_v:
    # it has been made somewhere ...
    def __init__(self,origin,v1,v2,v3):
        self.origin = Point(0,0,0)
        self.v1 = v1
    def __mul__(self):
        pass

if __name__ == "__main__":

    v1 = Vector(0.0,0.0,1.0)
    v2 = Vector(1.0,0,1.0)
    v0 = Vector(0,0,0)
    # not null !
    v3 = Vector(1,1,1)
    v4 = Vector(2,2,2)
    v5 = Vector(2,4,5)

    print(v3.colineaire(v4))
    print(v4.colineaire(v3))
    print(v3.colineaire(v5))
    
    O = Point(0,0,0,"O")
    A = Point(1,1,0,"A")
    B = Point(2,2,0,"B")
    C = Point(3,3,0,"C")
    D = Point(4,3,0,"D")

    print(A)
    print(B)
    AB = Droite(A,B)

    print(AB.contain(A))
    print(AB.contain(B))
    print(AB.contain(C))
    print(AB.contain(D))
    #print(AB.calculate(4))

    A = Point(0,1,0,"A")
    B = Point(0,0,0,"B")
    C = Point(1,0,0,"C")
    AB = Droite(A,B,"AB")
    #print(AB)
    ABC = Plan(A,B,C)
    D = Point(5,0,0,"D")
    #print(ABC.contain(D))
    E = Point(2,2,2,"E")
    #print(ABC.contain(E))
    H = Point(0,0,2)
    F = Point(0,2,2)
    G = Point(2,0,2)
    HFG = Plan(H,F,G,"HFG")
    print(HFG.contain(D))
    print(HFG.contain(E))

