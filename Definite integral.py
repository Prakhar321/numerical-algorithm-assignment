##ques 5
class integrate:
    import matplotlib.pyplot as plt
    from numpy import *
    def __init__(self,l,a,b):
         self.a=a
         self.b=b
         self.l=l
    def f(self,x):
         func=0.0
         for i in range(len(self.l)):
             func+=self.l[i]*x**i
         return func
    def graph(self):
         fig=plt.figure()
         ax=fig.add_subplot(111)
         x=arange(self.a,self.b,0.001)
         plt.plot(x,self.f(x),'r')
         ax.bar(x,self.f(x),0.001)
         plt.show()
    def trapezoidal(self):
        i=self.a+0.001
        result=0
        while(i<self.b):
          result=result+self.f(i)
          i+=0.001
        result=(self.f(self.a)+self.f(self.b)+2*result)*0.001/2.0
        return result
    def simpson(self):
       n=(self.b-self.a)/0.0001
       result=self.f(self.a)+self.f(self.b)
       for i in arange(1,n,2):
           result+=4*self.f(self.a+0.0001*i)
       for i in arange(2,n,2):
           result+=2*self.f(self.a+0.0001*i)
       return result*0.0001/3.0
l=[]
n=int(input())
for j in range(n):
    l.append(int(input()))
a=int(input())
b=int(input())
igr= integrate(l,a,b)
print (igr.simpson(),igr.trapezoidal())
igr.graph()
















