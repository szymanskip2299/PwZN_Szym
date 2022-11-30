

#run
#poetry run python .\proj2.py 100 -1 1 -1 20 
#poetry run python .\proj2.py 100 -1 1 -1 20 --density 0.3 --gif_name gif1.gif --magnetisation test.txt
#poetry run python .\proj2.py 100 -1 1 -1 4 --prefix image_

import numpy as np
import random
import math
from PIL import Image
from tqdm import tqdm
import argparse

class Ising:
    def __init__(self,N,J,beta,B,steps,density=None,prefix=None,gif_name=None,magnetisation=None):
        density = density if density else 0.5
        self.array = np.array(np.random.binomial(1,density,size=(N,N))*2-1,dtype="int8")
        self.N=N
        self.J=J
        self.beta=beta
        self.B=B
        self.steps=steps
        self.images=[Image.fromarray(np.uint8(self.array+1)*127)]
        self.gif_name=gif_name
        self.prefix=prefix
        self.magnetisation = magnetisation
        mi=np.sum(self.array)/self.N**2
        self.mi_array=[mi]
    
    def flip_deltaE(self,x,y):#zmiana energii przy odwroceniu danego elementu
        sum=2*self.J*self.array[x,y]*self.array[(x-1)%self.N,y]
        sum+=2*self.J*self.array[x,y]*self.array[(x+1)%self.N,y]
        sum+=2*self.J*self.array[x,y]*self.array[x,(y-1)%self.N]
        sum+=2*self.J*self.array[x,y]*self.array[x,(y+1)%self.N]
        return sum+2*self.B*self.array[x,y]

    def time_step(self):
        for i in range(self.N*self.N):
            x,y=random.randint(0,self.N-1),random.randint(0,self.N-1)
            deltaE=self.flip_deltaE(x,y)
            if deltaE<0 or random.random()<math.exp(-self.beta*deltaE):
                self.array[x,y]*=-1
        mi=np.sum(self.array)/self.N**2
        self.mi_array.append(mi)
        return(mi)

    def simulation(self):
        for i in range(self.steps):
            yield(self.time_step())
            self.images.append(Image.fromarray(np.uint8(self.array+1)*127))
            if self.prefix:
                self.images[-1].save(self.prefix+str(len(self.images)-1)+".png")
        if self.gif_name:
            self.images[0].save(self.gif_name, save_all=True, append_images=self.images[1:],loop=0)
        if self.magnetisation:
            f = open(self.magnetisation, "w")
            for i in range(len(self.mi_array)):
                f.write(f"{i}\t{self.mi_array[i]}\n")
            f.close()


parser = argparse.ArgumentParser()
parser.add_argument("n",type = int)
parser.add_argument("J",type = float)
parser.add_argument("beta", type = float)
parser.add_argument("B", type = float)
parser.add_argument("steps", type = int)
parser.add_argument("--density",type = float)
parser.add_argument("--prefix", type=str)
parser.add_argument("--gif_name", type = str)
parser.add_argument("--magnetisation",type = str)
args = parser.parse_args()



ising = Ising(args.n,args.J,args.beta,args.B,args.steps,args.density,prefix=args.prefix, gif_name=args.gif_name,magnetisation=args.magnetisation)
for i in tqdm(ising.simulation(),total=ising.steps):
    pass

