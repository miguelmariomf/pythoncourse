#!/usr/bin/env python

#Creamos unas listas para trabajar con ellas=>
lista=[1,2,3,4,5,6,7,8,9]
lista1=lista
lista2=[10,11,12,13,14,15]
lista5=[-10,-55,456,3,78,45,8,3,1,0,2,2]
lista6=lista5
lista_0=[2,9,9,4,7,0,4,7,7,9,4,2,1,"Azul",0,5,"Amarillo",7,"Rojo","Amarillo",0,3,"Rojo","Amarillo",1,"Rojo","Amarillo",9,"Azul"]

#Creamos una tupla para trabajar con ella=>
tupla=(1,2,3,4,5,"Negro","Gris","Blanco")

#Sumar dos listas=>
lista3=lista1+lista2
lista4=lista2+lista1
print("La lista 1 es:\n",lista1,"\n")
print("La lista 2 es:\n",lista2,"\n")
print("En la lista3 se han añadido los elementos de ambas listas=>\n",lista3,"\n")
print("En la lista4 se han añadido los elementos de ambas listas=>\n",lista4,"\n")

#Leer parte de la lista, la sintaxis a utilizar es nombredelalista[primera posicion que se quiere leer:última posicion que se quiere leer +1]...es decir si queremos leer hasta la posición 5 tendremos que poner 6, si queremos leer de la posicion 2 a la 6 pondremos nombredelalista[1:7]=>
print(lista[0:6],"\n",lista[5:10],"\n",lista[3:8],"\n")

#Ahora vamos a comprobar que ciertos valores esten en la lista=>
numero=int(input("Introduce un número para comprobar si esta en la lista:"))
if (numero in lista):
  print("El número",numero,"está en la lista\n\n")
else:
  print("El número",numero,"NO está en la lista\n\n")

#Con esto vamos a buscar el valor del indice donde se encuentra un dato que estemos buscando dentro de nuestra lista de datos, por ejemplo vamos a buscar en que posicion se encuentran los numeros 3,7,9, para ello=>
print("La posición del número 3 es:",lista.index(3),"\n","La posición del número 7 es:",lista.index(7),"\n","La posición del número 9 es:",lista.index(9),"\n\n")

#Ahora vamos a realizar un conteo del número de elementos que se repiten en una lista, por ejemplo la lista_0. Realizamos un conteo de varios elementos, por ejemplo vamos a comprobar cuantas veces esta repetido el número 0, el número 7 y la cadena de texto "Amarillo"=>
print("El número 0 está repetido:",lista_0.count(0),"veces\n")
print("El número 7 está repetido:",lista_0.count(7),"veces\n")
print("La palabra Amarillo está repetida:",lista_0.count(0),"veces\n\n")

#Vamos a comprobar el tamaño de una de nuestras listas, por ejemplo la lista_0:
print("El tamaño de la lista_0 es:",len(lista_0),"\n\n")

#Vamos a darle la vuelta a los elementos de una lista:
lista.reverse()
print("Lista invertida:\n",lista,"\n")
#Los devolvemos a su orden inicial:
lista.reverse()
print("Lista en orden original:\n",lista,"\n\n")

#Vamos a ordenar de menor a mayor los elementos de una lista:
lista5.sort()
print("Lista en orden de menor a mayor:\n",lista5,"\n")
#Vamos a ordenar de mayor a menor los elementos de una lista:
lista6.sort(reverse=True)
print("Lista en orden de mayor a menor:\n",lista6,"\n\n")

#Si intentamos ordenar una tupla, el sistema nos reporta un mensaje de error, porque las tuplas no se pueden modificar, ni sus elementos, ni el número de ellos, ni el orden de los mismos, solo podemos leer la información que hay en ellas, copiarlas etc. Así que si queremos hacer una modificación del tipo que sea en una tupla tendremos que hacer un clon de la misma con formato de lista y con esta podremos hacer las modificaciones que queramos=>
print("Los elementos de nuestra tupla son:\n",tupla,"\n")
#Vamos a convertir una tupla en lista=>
lista_de_tupla=list(tupla)
#Imprimimos los elementos de la lista que hemos utilizado para guardar la tupla:
print("Los elementos de la lista clonada son:\n",lista_de_tupla,"\n")
#Ahora si intentamos hacer por ejemplo un reverse de los elementos de esta copia de nuestra tupla inicial, veremos que podemos perfectamente, porque estamos trabajando con una lista y estas son modificables por completo:
lista_de_tupla.reverse()
print("Los elementos de la lista clonada invertidos mediante reverse son:\n",lista_de_tupla,"\n")

#//FIN
