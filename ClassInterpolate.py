##ques 4
from numpy import *
import matplotlib.pyplot as plt
class interpolate:
 def __init__(self,lx,fx):
     self.lx=lx
     self.fx=fx
 def lagrange(self):
     wx=poly1d(poly(self.lx))
     wxp=polyder(wx)
     list=[wxp(i) for i in self.lx]
     goa=poly1d([1])
     for j in range(0,len(self.lx)):
         a=self.lx[j]
         self.lx.remove(self.lx[j])
         goa=polyadd(goa,(poly1d(poly(self.lx)))*(self.fx[j]/list[j]))
         self.lx.insert(j,a)
     goa=goa-1
     return(goa)
 def Newton(self):
        n=len(self.lx)
        mat=[[0.0 for i in range(n)] for j in range(n)]
        for i in range(n):
            mat[i][0]=self.fx[i]
        for i in range(1,n):
            for j in range(n-i):
                mat[j][i]=(mat[j+1][i-1]-mat[j][i-1])/(self.lx[j+i]-self.fx[j])
        result=array((mat[0][0],))
        for i in range(1,n):
            prod=(-1*self.lx[0],1)

            for j in range(1,i):
                prod=polymul(prod,(-1*self.lx[j],1))
            result=polyadd(result,array(prod)*mat[0][i])
        return (list(result))
 def graph(self,a,b):
     x=arange(a,b,0.01)
     y=self.lagrange()
     plt.plot(x,y(x),'b-')
     plt.plot(self.lx,self.fx,'ro')
     plt.show()
