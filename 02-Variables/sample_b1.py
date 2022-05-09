#!/usr/bin/env python
#Creamos e imprimimos varios números con diferente formato entero, real y complejo

print("Introduce tres números")
n1=int(input())
n2=float(input())
n3=complex(input())
#Comprobamos que tipo de número es n1
while True:
  if (type(n1)==int):
    n1type="entero"
    break
  elif (type(n1==float)):
    n1type="real"
    break
  elif(type(n1==complex)):
    n1type="complejo"
    break
#Comprobamos que tipo de número es n2
while True:
  if (type(n2)==int):
    n2type="entero"
    break
  elif (type(n2==float)):
    n2type="real"
    break
  elif(type(n2==complex)):
    n2type="complejo"
    break
#Comprobamos que tipo de número es n3
while True:
  if (type(n3)==int):
    n3type="entero"
    break
  elif (type(n3==float)):
    n3type="real"
    break
  elif (type(n3==complex)):
    n3type="complejo"
    break

print(n1,"es un número de tipo:",n1type)
print(n2,"es un número de tipo:",n2type)
print(n3,"es un número de tipo:",n3type)

#//FIN
