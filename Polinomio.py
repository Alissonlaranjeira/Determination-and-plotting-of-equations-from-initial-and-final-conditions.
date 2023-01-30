import math
import numpy
import pandas
import matplotlib.pyplot as plt


#Tempo:
t0=0 #tempo inicial
tf=3 #tempo final
t = [t0,tf]

#posições:
theta0=0
thetaf=45
theta = [theta0,thetaf]

#velocidades:
v_theta0=0  #velocidade inicial
v_thetaf=0  #velocidade final
v_theta = [v_theta0,v_thetaf]

#acelerações:
a_theta0=0 #aceleração inicial
a_thetaf=0 #aceleração inicial
a_theta = [a_theta0,a_thetaf]

#Matrizes:
M=[[1,(t[0]),(t[0]**2), (t[0]**3), (t[0])**4, (t[0]**5)],
   [1,t[1],(t[1]**2), (t[1]**3), (t[1]**4), (t[1]**5)],
   [0, 1,  2*t[0], 3*(t[0]**2), 4*(t[0]**3), 5*(t[0]**4)],
   [0, 1,  2*t[1], 3*(t[1]**2), 4*(t[1]**3), 5*(t[1]**4)],
   [0, 0,  2,      2*3*t[0],   3*4*(t[0]**2), 4*5*(t[0]**3)],
   [0, 0,  2,      2*3*t[1],   3*4*(t[1]**2), 4*5*(t[1]**3)]]
print('\nM: ')
print(numpy.array(M))

Minv=numpy.linalg.inv(M)
print('\nM^-1: ')
print(numpy.array(Minv))

R=[[theta[0]],
   [theta[1]],
   [v_theta[0]],
   [v_theta[1]],
   [a_theta[0]],
   [a_theta[1]]]
print('\nR: ')
print(numpy.array(R))

a=numpy.dot(Minv,R)
print('\na: ')
print(numpy.array(a))

print('\ntheta(t)={} + {}t + {}t^2 +{}t^3 +{}t^4 +{}t^5'.format(round(a[0][0],3),round(a[1][0],3),round(a[2][0],3),round(a[3][0],3),round(a[4][0],3),round(a[5][0],3)))

print('\nvelocidade(t)={} + {}t + {}t^2 +{}t^3 +{}t^4 '.format(round(a[1][0],3),2*round(a[2][0],3),3*round(a[3][0],3),4*round(a[4][0],3),5*round(a[5][0],3)))

print('\naceleração(t)={} + {}t + {}t^2 +{}t^3  '.format(2*round(a[2][0],3),2*3*round(a[3][0],3),3*4*round(a[4][0],2),4*5*round(a[5][0],3)))

#provas reais:


def tragetoria(th,a):

    a0=round(a[0][0],3)
    a1=round(a[1][0],3)
    a2=round(a[2][0],3)
    a3=round(a[3][0],3)
    a4=round(a[4][0],3)
    a5=round(a[5][0],3)
    t1 = a0+(a1*th)+(a2*(th**2))+(a3*(th**3))+(a4*(th**4))+(a5*(th**5))
    return t1

t1=t0
tg1=tragetoria(t1,a)
print('\n theta = {}° para t = {}s'.format(tg1,t1))

t2=tf
tg2=tragetoria(t2,a)
print('\n theta = {}° para t = {}s'.format(tg2,t2))

def velocidade(th,a):
    a0 = round(a[0][0], 3)
    a1 = round(a[1][0], 3)
    a2 = round(a[2][0], 3)
    a3 = round(a[3][0], 3)
    a4 = round(a[4][0], 3)
    a5 = round(a[5][0], 3)
    t1=a1+(2*a2*th)+(3*a3*(th**2))+(4*a4*(th**3))+(5*a5*(th**4))
    return t1

t3=t0
vl1= velocidade(t3, a)
print('\n velocidade = {}°/s para t = {}s'.format(vl1,t3))

t4=tf
vl2= velocidade(t4, a)
print('\n velocidade = {}°/s para t = {}s'.format(vl2,t4))

def aceleracao(th,a):
    a0 = round(a[0][0], 3)
    a1 = round(a[1][0], 3)
    a2 = round(a[2][0], 3)
    a3 = round(a[3][0], 3)
    a4 = round(a[4][0], 3)
    a5 = round(a[5][0], 3)
    t=2*a2+(6*a3*th)+(12*a4*(th**2))+(20*a5*(th**3))
    return t

t5=t0
ac1= aceleracao(t5, a)
print('\n aceleração = {}°/s² para t = {}s'.format(ac1,t5))

t6=tf
ac2= aceleracao(t6, a)
print('\n aceleração = {}°/s² para t = {}s'.format(ac2,t6))



#plotagem das curvas:

x=numpy.linspace(t0,tf,1000)

plt.figure(1)
plt.plot(x,tragetoria(x,a))
plt.title('Posição')
plt.ylabel("Theta[°]")
plt.xlabel("Tempo[s]")
plt.grid()


plt.figure(2)
plt.plot(x,velocidade(x,a))
plt.ylabel("V_Theta[°/s]")
plt.xlabel("Tempo[s]")
plt.title('Velocidade')
plt.grid()

plt.figure(3)
plt.plot(x,aceleracao(x,a))
plt.title('Aceleração')
plt.ylabel("a_Theta[°/s²]")
plt.xlabel("Tempo[s]")
plt.grid()

fig,axs = plt.subplots(3,1)

axs[0].plot(x,tragetoria(x,a))
axs[0].set_title('Posição')
axs[0].grid()

axs[1].plot(x,velocidade(x,a))
axs[1].set_title('Velocidade')
axs[1].grid()

axs[2].plot(x,aceleracao(x,a))
axs[2].set_title('Aceleração')
axs[2].grid()

plt.show()
