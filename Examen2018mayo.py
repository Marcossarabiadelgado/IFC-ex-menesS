from numpy import*
import matplotlib.pyplot as plt

def Ffun(x,y,R,Q):
	r=sqrt(x**2+y**2)
	F= where(r<=R, Q**2/r**2, sqrt(Q)/r)
	return r,F

R=20.0
x=linspace(R,4*R,101)

y=arange(R,4*R,0.08*R)

x.shape=(1,len(x))
y.shape=(len(y),1)

Q = 2.0
R=20.0
r,F = Ffun(x,y,R,Q)

# Gráfico
plt.figure()

plt.subplot(1,2,1)
plt.plot(r[:,10],F[:,10])
plt.xlabel('r')
plt.ylabel('F')
plt.title('Columna de índice 10')

plt.subplot(1,2,2)
plt.plot(r[-1,:],F[-1,:])
plt.xlabel('r')
plt.ylabel('F')
plt.title('Última fila')

plt.show()
