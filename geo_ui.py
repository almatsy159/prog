import pygame as pg
import geo


class Frame(pg.sprite.Sprite):
    # add_item add x and y from center of frame ...
    
    def __init__(self,master,x=100,y=100,w=500,h=500,color="grey",vis=True,border=0):
        super().__init__()
        self.master = master
        self.visibility = True
        
        #self.u_x = 1
        #self.u_y = 1
        self.x=x
        self.y=y
        self.w = w
        self.h = h
        self.cg = geo.Point(self.x + self.w/2,self.y + self.h/2)
        self.color = color
        self.img()
        #self.items = []
        self.border = border
        self.group = pg.sprite.Group()
        #self.all_frame()
        self.running = False
        
        
        
    def img(self):
        #print("image of frame")
        self.image = pg.Surface((self.w,self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        #self.rect.center = self.cg.pos
        #self.rect = pg.Rect(self.x,self.y,self.w,self.h)
        
    def all_frame(self):
        #print(self.group)
        #self.b_quit = Button(self,self.x,self.y,50,50)
        self.add_item(self.b_quit)
        #print(self.group)
        
    def add_item(self,item):
        #self.items.append(item)
        
        item.x = self.x + item.x
        item.y = self.y + item.y
        item.img()
        #item.ima
        #print(f"adding {item} in self.groups")
        self.group.add(item)
        #print(self.group)
        

    def draw(self,screen):
        #print(f"drawing on {screen}")
        pg.draw.rect(screen,self.color,self.rect)
        #print("drawing frame")
        #for i in self.items:
            #i.u_x = self.u_x
            #i.u_y = self.u_y
        #   i.draw(screen)
        #pg.display.flip()
        #print(self.group)
        self.group.draw(screen)
        
    def remove_item(self,item):
        self.group.remove(item)


pg.init()
screen=pg.display.set_mode((0,0))
w,h = res = screen.get_size()
print(res)
wf = 500
hf = 500
u_x = 25
u_y = 20
k_x = 3
k_y = 4
k_z = 5
border_x =  (w - wf)//2
border_y = (h - hf)//2

center_frame = geo.Point(w//2,h//2)

origin = geo.Point(center_frame.x-wf//2+u_x,center_frame.y+hf//2-u_y,0)
center_screen = geo.Point(w//2,h//2)
print(center_frame)
main = Frame(screen,center_frame.x,center_frame.y,wf,hf)
#main.add_item(bot_left_frame)
o = origin
a = geo.Point(o.x+k_x*u_x,o.y)
b = geo.Point(o.x,o.y-u_y*k_y)
#oa = geo.Vector(o,a)
#ob = geo.Vector(o,b)
#ab = geo.Vector(a,b)
oa = geo.Segment(o,a)
ob = geo.Segment(o,b)
v1 = geo.Vector(a.x,a.y,a.z)
v2 = geo.Vector(b.x,b.y,b.z)
print(o.x,o.y)
print(v1.magnitude())
c = geo.Point(o.x+k_x*u_x,o.y-k_y*u_y,1)
#c = geo.Point(o.x+a.x+k_z*5,o.y-b.y,1)
oc = geo.Segment(o,c)
print(oc.length)
v3 = geo.Vector(c.x,c.y,c.z)

print()

running = True
while running:
    # while scene 0 : !!!
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
    
    screen.fill("black")
    
    main.draw(screen)
    center_frame.pg_draw(screen)
    origin.pg_draw(screen,"red")
    a.pg_draw(screen)
    b.pg_draw(screen)
    c.pg_draw(screen,"blue")
    #sab.pg_draw(screen)
    oa.pg_draw(screen)
    ob.pg_draw(screen)
    oc.pg_draw(screen)
    

    pg.display.flip()
            


pg.quit()

