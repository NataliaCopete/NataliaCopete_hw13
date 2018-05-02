import numpy as np
import matplotlib.pyplot as plt
import random


def sort_doors():
  lista=['goat','goat','car']
  random.shuffle(lista)
  return lista

## a lista de posibles valores de eleccion
def choose_door():
  a=[0,1,2]
  numalea=np.random.choice(a)
  return numalea

##booleano se vuelve true cuando ya se ha realizado un primer cambio a GOAT_MONTY

def reveal_door(lista,choice):
  booleano=False
  for i in range(len(lista)):
    if(i!=choice and booleano==False):
      if(lista[i]=='goat'):
        lista[i]='GOAT_MONTY'
        booleano=True
  return lista


def finish_game(lista,choice,change):
  
  if change ==True:
    for i in range(len(lista)):
      if (lista[i] !='GOAT_MONTY' and i != choice):
        return lista[i]
    
  else:
    return lista[choice]

cambio=0
nocambio=0

N=100

for i in range(N):
  eleccion=choose_door()
  resultado=finish_game(reveal_door(sort_doors(),eleccion),eleccion,True)
  if (resultado =='car'):
    cambio +=1
for j in range(N):
  eleccion=choose_door()
  resultado=finish_game(reveal_door(sort_doors(),eleccion),eleccion,False)
  if (resultado =='car'):
    nocambio +=1
      
probacambio=cambio/(float(N))
probanocambio= nocambio/(float(N))

print(probacambio)
print(probanocambio)  
  
    
  
