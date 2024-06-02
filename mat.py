import math

e_alpha = ["4","5"]
e_bin = ["0","1"]
e_trin = e_bin + ["2"]



def full_join(set1,set2,link="*"):
    res =[]
    for e1 in set1:
        for e2 in set2:
            res.append(f"{e1}{link}{e2}")
    return res
            
if __name__ == "__main__":
    e_alpha_second_deg = full_join(e_alpha,e_alpha) 
    print(e_alpha_second_deg)
    e_alpha_third_deg = full_join(e_alpha_second_deg,e_alpha)
    print(e_alpha_third_deg)          
        
def eval_lst(lst):
    res =[]
    for i in lst:
        print(f"{i} = {eval(i)}")
    return res

eval_lst_res = eval_lst(e_alpha_third_deg)

def sum(lst):
    res = 0
    for i in lst:
        res += i
    return res

class Objet:
    def __init__(self,props_name,vals):
        self.props = props_name
        self.vals = vals
    
    def gen_prop(self):
        # vals et props length must be equal
        for name in self.props:
            for v in self.vals :
                tmp = f"self.{name} = {v}"
                exec(tmp)
                
            
            

def lst_of_pow(n,p=3) : 
    res = [n**p for n in range(1,n)]
    #print(res)
    return res


#lst_of_pow(10,4)*

def tbl_of_pow(n,p=3):
    table = [lst_of_pow(n,r) for r in range(1,p)]
    #print(table)
    return table

if __name__ == "__main__":
    res = tbl_of_pow(10,4)

    for i in res:
        print(i)
    
    
def base(val=0,n=10,m=2):
    
    pass