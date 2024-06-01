
"""
def full_join(set1,set2,link="*"):
    res = []
    for e1 in set1:
        for e2 in set2:
            res.append(f"{e1}{link}{e2}")
    return res
"""

def full_join(set1,set2,set3):
    res = []
    for e1 in set1:
        for e2 in set2:
            for e3 in set3:
                tmp = (e1,e2,e3)
                res.append(tmp)
    return res

set = [-1,1]
tmp = full_join(set,set,set)
#res = full_join(tmp,set)

print(tmp)

class Point:
    def __init__(self,coords):
        self.point = coords
        self.x,self.y,self.z = coords[0],coords[1],coords[2]
        