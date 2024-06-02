data1=[[1,2,3],[4,5,6]]
data2=[[1,2],[3,4],[5,6]]
data3=[[7,8,9],[10,11,12]]
#data1 =

# TO DO : Dans Matrix_Operator creation d'une matrice vide !!! et revoir l'init de Matrix
# Pour recup la dimension des data si dim data =1 mais que rows > 1 => a decouper et meme condition row ou col ==None => erreur
# revoir la repr des matrices avec repr_of_m (name , index , sum (et avg ?) = 1 par default)
"""
Name(n,m) :
            00 | 01 | 02  sum by row
           _____________
            01 | x1 | x2 = x1+x2
            02 | x3 | x4 = x3+x4
                 ||   ||
Sum by col      x1+x3 x2+x4
"""
"""
class Matrix():
    def __init__(self,name,r,c,data):
        self.rows=r
        self.columun=c
        self.data=data
        self.type=None
        if isinstance(self.data,str):
            self.type=str()
        elif isinstance(self.data,list):
            self.type=list()
"""
class Matrix():
    def __init__(self,name,data=[],rows=None,cols=None):
        """
        if (rows == None and cols == None) and data ==[]:
            return "error"
        if rows != None:
            self.rows=rows
        if cols != None:
            self.cols=cols
        """
        self.name=name

        if data != []:
            self.data=data
            #print(self.data)
            for i in range(len(self.data)) :
                #print(i)
                if i == len(self.data)-1:
                    self.rows=i+1
                for j in range(len(self.data[i])):
                    #print(j)
                    if j == len(self.data[i])-1:
                        self.cols=j+1

        self.full_name=f"{self.name}({self.rows},{self.cols}):"
        self.len_of_name=len(self.full_name)
        self.data_to_dict()
        #self.print_matrix()
        self.max_length()
        #self.repr_of_m(self.data)
        self.sum_by_rows(self.data)
        self.data_to_cols()
        self.repr_of_m(self.data_cols)
        self.sum_by_rows(self.data_cols,"c")

    def sum_by_rows(self,list,by="r"):

        flag=0
        for i in range(len(list)):

            if by=="r":
                name="r"+str(i+1)
                if flag ==0:
                    self.dict_sum_by_rows={}
                    actual_dict=self.dict_sum_by_rows
                    flag=1
            else:
                name="c"+str(i+1)
                if flag == 0:
                    self.dict_sum_by_cols={}
                    actual_dict=self.dict_sum_by_cols
                    flag=1
            x=0
            for j in range(len(list[i])):
                x+=list[i][j]
            actual_dict[name]=x
        #print(actual_dict)

    def data_to_cols(self):
        self.data_cols=[]
        for i in range(self.cols):
            self.data_cols.append([])
            for j in range(self.rows):
                self.data_cols[i].append(self.data[j][i])
        #print(self.data_cols)

    def data_to_dict(self):
        self.data_dict={}
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                name=f"{str(i+1)},{str(j+1)}"
                self.data_dict[name]=self.data[i][j]
        #print(self.data_dict)
    """
    def print_matrix(self):
        print(f"{self.name}({self.rows},{self.cols}):")
        str=""
        format_str=""
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                #print("self.data[i]",self.data[i])
                print("self.data[i][j]",self.data[i][j])
    """
    def max_length(self):
        self.max=0
        for i in self.data:
            for j in i:
                if len(str(j))>self.max:
                    self.max=len(str(j))

    def repr_of_m(self,list):
        print(self.full_name)
        my_str=""
        my_format=".format("
        decalage1=f":>{self.len_of_name+self.max}"
        decalage2=f":>{self.max+1}"

        for i in list:
            for j in i:
                if j != i[0]:
                    my_str += "{"+decalage2+"}"
                else :
                    my_str += "{"+decalage1+"}"
                if j != i[-1] or i!=list[-1] :
                    my_format += str(j)+","
                else:
                    my_format +=str(j)
            my_str+="\n"
        my_format += ")"

        #print("my_str :\n",my_str)
        #print("my_format :\n",my_format)
        formated_str=f"\"\"\"{my_str}\"\"\"{my_format}"
        print(eval(formated_str))


# each fct deserve a class ? => allow to repr the calculus easily
class Matrix_Operator():
    def null_matrix(x,y):
        data=[]
        for i in range(x):
            data.append([])
            for j in range(y):
                data[i].append(0)
        return data
    def scalar_product(scalar,matrix):
        res_data=matrix.data
        for i in range(len(res_data)):
            for j in range(len(res_data[i])):
                #print(i,j)
                res_data[i][j]=(res_data[i][j])*scalar
        print(res_data)
        res_m=Matrix("res_m",res_data)
        return res_m
    def scalar_product(name,scalar,matrix):
        data=Matrix_Operator.null_matrix(matrix.rows,matrix.cols)
        for i in range(len(matrix.data)):
            for j in range(len(matrix.data[i])):
                data[i][j]=matrix.data[i][j]*scalar
        res_m=Matrix(name,data)
        return res_m
    def common_product(name,m1,m2):
        if m1.cols != m2.rows :
            res="error : not calculable"
            return res
        else :
            res_data=[]
            for i in range(m1.rows):
                res_data.append([])
                for j in range(m2.cols):
                    key1="r"+str(i+1)
                    x1=m1.dict_sum_by_rows[key1]
                    key2="c"+str(j+1)
                    x2=m2.dict_sum_by_cols[key2]
                    res_data[i].append(x1*x2)
            res_m=Matrix(name,res_data)
            """
            def get_data_line(matrix):
                data_line=[]
                #m_rows=matrix.rows
                #m_cols=matrix.cols
                for i in matrix.data :
                    for j in i :
                        data_line.append(j)
                print(f"data_line of {matrix.name} :{data_line}")
                return data_line

            data_line1=get_data_line(m1)
            data_line2=get_data_line(m2)
            """

            print(res_data)
            return res_m
    def produit_hadamard(name,m1,m2):
        if m1.rows != m2.rows or m1.cols != m2.cols:
            return "error both matrix aren't the same size !"
        else :
            data=Matrix_Operator.null_matrix(m1.rows,m1.cols)
            #print(data)
            for i in range(len(data)):
                for j in range(len(data[i])):
                    key=f"{i+1},{j+1}"
                    x1=m1.data_dict[key]
                    x2=m2.data_dict[key]
                    data[i][j]=x1*x2
                    #print(f"{x1}+{x2}={data[i][j]}")
            res_m=Matrix(name,data)
            return res_m

if __name__ == "__main__":
    
    m1=Matrix("m1",data1)
    #print("data by rows :",m1.data)
    #print("data by cols :",m1.data_cols)
    m2=Matrix("m2",data2)

    # !!! scalar_product modify the initial matrix !!!
    m3=Matrix_Operator.scalar_product("m3",2,m1)

    m4=Matrix_Operator.common_product("m4",m1,m2)
    m5=Matrix_Operator.common_product("m5",m2,m1)

    m7=Matrix("m7",data3)
    m6=Matrix_Operator.produit_hadamard("m6",m1,m7)
    
