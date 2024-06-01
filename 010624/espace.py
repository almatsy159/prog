"""
import matplotlib.pyplot as plt
z = []
def coeff(x=3):
    y = None
    if x == 4:
        y = 3
    elif x == 3:
        y = 4
    return y

def somme(a,b):
    return a+b

kx= 3
ky = coeff(kx)

max = 5
x = [3*i for i in range(max)]
y = [4*i for i in range(max)]
print(x)
print(y)
#z = [3*i for i in range(max)]

def pyth(a,b):
    return (a*a+b*b)**(1/2)

z1 = [pyth(x[i],y[i]) for i in range(max)]
print(z1)
plt.xlabel("x")
plt.ylabel("y")

plt.axis((3,4,12,12))
plt.plot(z)
#plt.scatter(xx)
plt.grid()

plt.title("3x*4y")
plt.show()

plt.savefig("fig.png")
"""