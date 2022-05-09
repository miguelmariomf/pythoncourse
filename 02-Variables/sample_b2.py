#Comprobamos que tipos de números son, esta vez mediante el uso de una función:

def comprueba(numero):

  while True:
    if (type(numero)==int):
     tipo="entero"
     break
    elif (type(numero)==complex):
     tipo="complejo"
     break
    elif (type(numero)==float):
     tipo="real"
     break
  
  return tipo

#Imprimimos en pantalla el número y el tipo de número que es:
print(n1,"es un número de tipo:",comprueba(n1))
print(n2,"es un número de tipo:",comprueba(n2))
print(n3,"es un número de tipo:",comprueba(n3))

#Podemos imprimir en pantalla el número y tipo sin escribir tres veces la función print:
for x in n1,n2,n3:
  print(x,"es un número de tipo:",comprueba(x))

#//FIN
