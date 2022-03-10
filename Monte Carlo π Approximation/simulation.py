import math as m
import random
def function(x):
   return m.sqrt(1-(x**2))
def is_in_circle(x,y):
    if y <= function(x):
        return True
    else:
        return False
def simulation(number_of_runs):
    inside = 0
    for i in range(number_of_runs):
        x = random.random()
        y = random.random()        
        if is_in_circle(x,y):
            inside+=1
    return inside/number_of_runs*4
  simulation(100000) # 100,000 Simulations -> Call function
  
