import matplotlib.pyplot as plt
from numpy import *
class PolynomialSolver:
    def __init__(self,l,a,b):
        self.l=l
        self.a=a
        self.b=b
    def f(self,x):
          func=0.0
          for i in range(len(self.l)):
              func+=self.l[i]*x**i
          return func
    def graph(self):
         fig=plt.figure()
         ax=fig.add_subplot(111)
         if(self.b>self.a):
             la,lb=[self.a],[self.b]
             x=arange(self.a,self.b+0.001,0.001)
             plt.plot(x,self.f(x))
             for i in range(50):
                     m=(self.a+self.b)/2
                     if(self.f(self.a)*self.f(m)<0.0):
                         self.b=m
                     elif(self.f(self.b)*self.f(m)<0.0):
                         self.a=m

                     la.append(self.a)
                     lb.append(self.b)
             fla=[self.f(i) for i in la]
             flb=[self.f(i) for i in lb]
             plt.plot(la,fla,'ro',lb,flb,'go')
             plt.plot(m,self.f(m),'y^')
             ax.annotate('root', xy=(m,self.f(m)), xytext=(self.b,self.f(self.b)),
                arrowprops={'facecolor':'black', 'shrink':0.05})
             plt.show()
             return (self.a,self.b)
        

l=[]
n=int(input())
for j in range(n):
    l.append(int(input()))
a=input()
b=input()
igr= PolynomialSolver(l,a,b)
print igr.graph()
