#!/usr/bin/env python

#En este Scrip probamos el uso de cadenas en Python

#Creamos para ello unas cuantas cadenas de texto:
cadena_0="Hola Mundo..."
cadena_1="Como te va?..."
cadena_2="Cambio y Corto"
cadena_4="Buenos días, hoy hace un clima fenomenal para ir a echar el dia en la playa.Qué me dices?...Pues si que tenemos buen clima...Te apuntas?...Claro que sí nos vemos a las 10 en el paseo maritimo...chao...adios"

#Vamos a imprimir la cadena_0 de diferentes formas:
print("Podemos imprimir cadenas completas, en este caso imprimimos la cadena_0=>\n",cadena_0,"\n")
print("Podemos imprimir un caracter concreto de la cadena, en este caso imprimimos el caracter primero de la cadena_0=>\n",cadena_0[0],"\n")
print("Podemos imprimir varios caracteres seguidos que pertenecen a una cadena, en este caso imprimimos desde el segundo caracter al cuarto caracter de la cadena_0=>\n",cadena_0[1:5],"\n")
print("Tambien podemos imprimir todos los caracteres del primero al que queramos, en este caso imprimimos desde el primer caracter al cuarto caracter de la cadena_0=>\n",cadena_0[:5],"\n")
print("Asi como tambien podemos imprimir todos los caracteres desde uno que elijamos al último caracter de la cadena, en este caso imprimimos desde el sexto caracter al ultimo caracter de la cadena_0=>\n",cadena_0[5:],"\n\n")

#Ahora vamos a probar otras operaciones que se le pueden aplicar a las cadenas:

#Sumar dos cadenas de texto e imprimir el resultado:
cadena_3=cadena_1+cadena_2
print("Imprimimos la cadena resultante de sumar la cadena_1+cadena_2, es decir la cadena_3=>\n",cadena_3,"\n")
#Tambien podemos sumar dos cadenas directamente en pantalla sin tener que guardar el resultado en una tercera variable mediante print:
print("Imprimimos la cadena resultante de sumar la cadena_0+cadena_2 directamente en el metodo print=>\n",cadena_0+cadena_2,"\n")
#Podemos sumar una parte de una cadena con otra cadena completa o parte de esta:
print("Imprimimos la cadena resultante de sumar desde el primer caracter de la cadena_0 hasta el cuarto caracter de la misma + la cadena_2 al completo directamente en el metodo print=>\n",cadena_0[:5]+cadena_2,"\n")
#Tambien podemos multiplicar una cadena, obviamente el resultado que nos dará será la simple repeticion de la cadena tantas veces como le pidamos que lo haga:
print("Por ejemplo vamos a imprimir la cadena_0 completa 5 veces con un salto de linea en cada una=>",(cadena_0+"\n")*5,"\n")

#Por otra parte podemos aplicar diferentes funciones a nuestras cadenas para recibir datos sobre ellas o para modificarlas:

#Longitud de una cadena dada:
print("La cadena_0 tiene",len(cadena_0),"caracteres")
print("La cadena_1 tiene",len(cadena_1),"caracteres")
print("La cadena_2 tiene",len(cadena_2),"caracteres")
print("La suma de las cadena_0+cadena_1 tiene",len(cadena_0+cadena_1),"caracteres\n\n")

#Encontrar coincidencias dentro de una cadena:
print("Si la coincidencia existe dentro de nuestra cadena nos devolverá el valor correspondiente a la posicion de su primera letra, por ejemplo si buscamos dentro de la cadena_0 la palabra Mundo, nos devolverá el valor de 5 porque la primera letra de la palabra Mundo es la M y su posición dentro de la cadena_0 es la sexta posición por tanto corresponde al índice 5=>\n\n",cadena_0.find("Mundo"),"\n")
print("En caso de que la coincidencia no exista en la cadena dada, nos devolverá el valor de -1, como señal de que no ha encontrado nada similar, vamos a probar con la palabra corto dentro de la cadena_1, quiza pensemos de primera que encontrará la coincidencia, pero dentro de dicha cadena tenemos el valor Corto y no corto, esta herramienta busca la coincidencia literal, contando por tanto mayusculas y minúsculas=>\n\n",cadena_1.find("corto"),"\n\n")

#Convertir toda la cadena en mayusculas o toda la cadena en minusculas:
print("Vamos a convertir la cadena_0 entera a mayusculas=>\n",cadena_0.upper(),"\n")
print("Vamos a convertir la cadena_0 entera a minusculas=>\n",cadena_0.lower(),"\n")
print("Ahora vamos a convertir parte de la cadena_0 a minusculas y parte en mayusculas=>\n",cadena_0[0:5].lower()+cadena_0[4:].upper(),"\n\n")

#Reemplazar parte de la cadena por otra cosa que prefiramos:
print("Imprimimos la cadena_4 original=>\n\n",cadena_4,"\n")
print("Vamos a remplazar la palabra clima de la cadena_4 por tiempo=>\n\n",cadena_4.replace("clima","tiempo"),"\n\n")
print("Como vemos la palabra clima que esta repetida en nuestra cadena dos veces ha sido cambiada en ambos casos por tiempo, ahora solo cambiaremos la primera y no la segunda=>\n\n",cadena_4.replace("clima","tiempo",1),"\n")
print("Pero que pasa si queremos cambiar la segunda palabra y no la primera, pues en este caso como solo se repite dos veces podemos apuntar a la segunda parte de la cadena contando la mitad como el espacio que hay justo después de la primera vez que vemos la palabra clima=>\n\n",cadena_4[:cadena_4.find("clima")+5],cadena_4[cadena_4.find("clima")+5:].replace("clima","tiempo"),"\n\n")

#//FIN
