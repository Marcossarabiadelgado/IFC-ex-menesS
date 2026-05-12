from numpy import*
import matplotlib.pyplot as plt

#Parámetros
v=20 # m/s
g=9.81 # m/s²

# Apartado 1
def parabolico(a,t,b,v,g):
	ar=radians(a)
	x=v*cos(ar)/b * (1-exp(-b*t))
	y=1/b*(g/b + v*sin(ar))*(1-exp(-b*t))-g/b * t
	return array([x,y])

# Apartado 2
def trayectoria(x,y):
	xpos=where(x>=0)
	xp=x[xpos]
	ypos=where(y>=0)
	yp=y[ypos]
	return(xp,yp)

# Apartado 3
a=arange(30,61,5)
a_1D=a.copy()
a.shape=(1,1,1,7)
a=repeat(a,2,axis=0)


b=arange(0.02,0.11,0.02)
b_1D=b.copy()
b.shape=(1,5,1,1)
b=repeat(b,2,axis=0)

t=linspace(0,10,500)
t_1D=t.copy()
t.shape=(1,1,500,1)
t=repeat(t,2,axis=0)

# Apartado 4
b.shape=(2,5,1,1)
t.shape=(2,1,500,1)
a.shape=(2,1,1,7)

x,y=parabolico(a,t,b,v,g)

# Apartado 5
xp,yp=trayectoria(x,y)

# Gráfica
plt.figure()
plt.plot(xp[:,:,0,:],yp[:,:,0,:])

plt.show()
