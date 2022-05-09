#!/usr/bin/env python

#Pedimos por pantalla que se introduzcan 3 números:

print("Introduce tres números")
n1=int(input())
n2=float(input())
n3=complex(input())

#Comprobamos que tipos de números son, esta vez mediante el uso de una función:

def comprueba(numero):

  while True:
    if (type(numero)==int):
     tipo="entero"
     break
    
    if (type(numero)==complex):
     tipo="complejo"
     break
    
    if (type(numero)==float):
     tipo="real"
     break
  
  return tipo

#Ahora usamos una función para imprimir en pantalla, lo interesante es ver como podemos usar una funcion dentro de otra, obviamente sería más rapido hacerlo sin crear una funcion para imprimir, pero cuando tenemos un gran número de datos esto podría llegar a ahorrarnos código y por tanto optimizar el script:
  
def imprime(numero):
 
  print(numero,"es un número de tipo:",comprueba(numero))

pass

for x in n1,n2,n3:
  imprime(x)


#//FIN
