"""
     ___________*--------*_________
   /___________/        /|________/
  /___________*--------* *_______/
 /____________|        |/_______/
/_____________*--------*_______/


"""




import tkinter as tk

import matrix as mtx

class Cube():

    def __init__(self,cote,cg_x,cg_y,state=None):

        self.cote = cote
        self.cg_x = cg_x
        self.cg_y = cg_y

        self.cg_z = self.cote / 2


        self.xmin = self.cg_x - self.cote
        self.xmax = self.cg_x + self.cote
        self.ymin = self.cg_y - self.cote
        self.ymax = self.cg_y + self.cote

        if state == 0:
            self.state = "full"
        if state == 1:
            self.state = "partial"


        data=[]
        for i in range(cote):
            data.append([])
            for j in range(cote):
                data[i].append(1)

        self.data=data
        """
        for i in range(len(data)):
            print(self.data[i])
        """
        #print(data)
        self.matrix=mtx.Matrix("c1",self.data)
        #print(self.matrix)




class Cube_View():
    pass


c1=Cube(5,10,10)
