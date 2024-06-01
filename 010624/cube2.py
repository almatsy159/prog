import tkinter as tk


class view_of_line():
    id = 0
    def __init__(self,parent,line,color="white",top=0):
        self.id=view_of_line.id
        view_of_line.id+=1
        self.top = top
        if self.top != 0:
            print("drawing a line")
        self.parent = parent
        self.line = line
        print(parent)
        self.parent.create_line(self.line.xmin,self.line.ymin,self.line.xmax,self.line.ymax,fill=color)
#intersection, appartenance
class Point():

    def __init__(self,x,y,z):

        self.x = x
        self.y = y
        self.z = z

class Line():

    def __init__(self,xmin,ymin,xmax,ymax,top=0):
        if top != 0:
            print("making a line !")
            print(xmin,ymin,xmax,ymax)

        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        print(xmin,ymin,xmax,ymax)
        #self.f_ligne()
"""
    def f_ligne(self):
        #y=ax+b
        #y-b=ax
        #Y=(a/2)x²+bx+C
        #y'=a

        # need repere

        #k_x=(self.ymin-self.ymax)/(self.xmin-self.xmax)
        #print(f"f(x) : y = {k_x}*x")
    # 2 points
"""
class Surface():
    def __init__(self,points=[],parent=None,color="white"):
        self.points=points
        print("points param :",self.points)
        #screen size
        self.xmin=size_x
        self.xmax=0
        self.ymax=0
        self.ymin=size_y
        for x in self.points :
            for i in x:
                if i < self.xmin :
                    self.xmin = i
                elif i > self.xmax :
                    self.xmax= i
        for y in self.points :
            for i in y:
                if i < self.ymin :
                    self.ymin = i
                elif i > self.ymax :
                    self.ymax= i
        print("points xmax,ymax,xmin,ymin :", self.xmax,self.ymax,self.xmin,self.ymin)
        self.parent=parent
        if self.parent != None:
            self.parent.create_rectangle(self.xmin,self.ymin,self.xmax,self.ymax,fill=color)

class Volume():
    # dim de volume (min surface = dim +1)
    id = 0
    def __init__(self,name,size=[],surfaces=[],parent=None,links=None):
        # si creation de lien sans parent => env lié
        self.parent=parent
        self.parent.__init__()
        self.id = Volume.id
        Volume.id += 1
        self.links = links

        #if isinstance(coords,list):

def map_lines(list,parent=None,color="black",top=0):
    list_of_object = []
    if top !=0:
        print(f"list :",list)

    for line in list :
        if top !=0:
            print(f"{top} :mapping a line : {line} ")
        x_min = line[0]
        y_min = line[1]
        x_max = line[2]
        y_max = line[3]
        print(f"{x_min},{y_min};{x_max},{y_max}")
        line = Line(x_min,y_min,x_max,y_max,top)

        if parent != None :
            #print(parent)
            view_of_line(parent,line,color,1)
        list_of_object.append(line)

    print("mapped list : ",list_of_object)
    return list_of_object

if __name__ == "__main__" :

    cube1=[111,111,111],[111,101,111],[111,111,111]
    env = [00000,000000,0000,00000]
    p1_s1=(25,25)
    p2_s1=(225,225)
    size_x = 1000
    size_y  = 500

    app=tk.Tk()
    main=tk.Frame(app)

    env_can=tk.Canvas(width=size_x,height=size_y,bg="green")
    s1=Surface([[50,25],[75,150]],env_can,"blue")

    l1_coord=[0,250,1000,250]
    l2_coord=[500,0,500,500]
    list_map=[l2_coord]

    mapped_list = map_lines(list_map,env_can,"red",1)

    #print("mapped_list : ",mapped_list)
    #l2 = map_line(l2_coord,"map2 => l2")
    #view= view_of_line(env_can,mapped_list,"magenta",1)
    #view0= view_of_line(env_can,list_view0,"red",1)

    env_can.pack()
    main.pack()
    app.mainloop()
