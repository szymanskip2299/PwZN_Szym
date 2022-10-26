
import numpy as np
import random
import math

class Ising:
    def __init__(self,N,J,beta,B):
        self.array = np.array(np.random.randint(low=0,high=2,size=(N,N))*2-1)
        self.N=N
        self.J=J
        self.beta=beta
        self.B=B
    
    def time_step(self):
        for i in range(self.N*self.N):
            x,y=random.randint(0,self.N-1),random.randint(0,self.N-1)
            deltaE=self.flip_deltaE(x,y)
            if deltaE<0 or random.random()<math.exp(-self.beta*deltaE):
                self.array[x,y]*=-1
        

    def flip_deltaE(self,x,y):#zmiana energii przy odwroceniu danego elementu
        sum=2*self.J*self.array[x,y]*self.array[(x-1)%self.N,y]
        sum+=2*self.J*self.array[x,y]*self.array[(x+1)%self.N,y]
        sum+=2*self.J*self.array[x,y]*self.array[x,(y-1)%self.N]
        sum+=2*self.J*self.array[x,y]*self.array[x,(y+1)%self.N]
        return sum+2*self.B*self.array[x,y]

ising = Ising(1000,1,1,1)
# for i in range(100):
#     print(i)
#     ising.time_step()
print(range(10))