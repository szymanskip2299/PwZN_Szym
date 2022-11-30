import time
import functools
import statistics
import random
import numpy as np

class _Timing:
    def __init__(self, func,silent=False):
        self._func = func
        self.memory=[]
        self.silent=silent
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        start=time.time()
        self._func(*args, **kwargs)
        duration=time.time()-start
        if not self.silent:
            print(f"Funkcja {self._func.__name__} wykonana w {duration} s")
        self.memory.append(duration)

    def stats(self):
        if len(self.memory)==0:
            print(f"Funkcja {self._func.__name__} nie została wykonana")
        else:
            print(f"Funkcja {self._func.__name__} została wykonana {len(self.memory)} razy")
            print("Czas wykonywania:")
            print(f"Średnia: {statistics.mean(self.memory)} s")
            print(f"Mediana: {statistics.median(self.memory)} s")
            print(f"Stdev: {statistics.stdev(self.memory)} s")
            print(f"Min: {min(self.memory)} s")
            print(f"max: {max(self.memory)} s")

    def clear_memory(self):
        self.memory=[]

def Timing(function=None, silent=False):
    if function:
        return _Timing(function)
    else:
        def wrapper(function):
            return _Timing(function,silent)

        return wrapper



@Timing(silent=True)
def my_function():
    p=0
    for i in range(100000):
       p+=random.random()**2 
    return p


for i in range(100):
    my_function()   
my_function.stats()
my_function.clear_memory()
for i in range(10):
    my_function()
my_function.stats() 


@Timing
def my_slow_function(n):
    return(np.random.rand(n,n)*np.random.rand(n,n))

my_slow_function(2*10**4)


