#!/usr/bin/env python

#Los conjuntos son muy parecidos a las listas, solo que con ciertas restricciones respecto a estas, los conjuntos no pueden almacenar datos repetidos, es decir si le introducimos dos veces un numero o cadena de texto, solo lo almacenará una vez, para crear un nuevo conjunto VACIO hay que usar la funcion set, sin embargo si queremos crear un conjunto con elementos dentro del mismo desde el inicio del conjunto no necesitamos esta funcion:

#Creamos el conjunto_0 y le añadimos elementos:
conjunto_0={"Hola","Hola","2","2","0","Pegasus"}

#Creamos dos conjuntos puramente numericos:
conjunto_2={1,2,3,4,6,5,11}
conjunto_3={6,7,8,9,10,4,3}

#Creamos varios conjuntos vacios:
conjunto_1=set()
conjunto_4=set()

#Añadimos elementos al conjunto_1 que inicialmente estaba vacío:
conjunto_1.add("mi")
conjunto_1.add("carro")
conjunto_1.add("me")
conjunto_1.add("lo")
conjunto_1.add("robaron")


print (conjunto_0,"\n")
print("Como vemos solo se ha guardado una vez la cadena de texto Hola y el número 2\n")
print("Como vemos el conjunto_1 fue declarado como conjunto vacio al principio y luego hemos ido añadiendo elementos dentro del mismo=>\n",conjunto_1,"\n")

#Otra gran diferencia de los conjuntos respecto a las listas es que los conjuntos no pueden guardar otras listas o conjuntos dentro;

#Los conjuntos además son colecciones desordenadas de datos, es decir que no podemos ordenarlos a nuestro gusto;

#Entonces la pregunta es que podemos hacerle a los conjuntos:

#Podemos agregar más elementos de los inicialmente agregados:
print("Agregamos los elementos Pi y 3.141 y como vemos inserta los nuevos elementos de manera aleatoria y tambien cambia el orden de los que ya estaban, tambien aleatoriamente=>\n")
conjunto_0.add(3.141)
conjunto_0.add("Pi")
print(conjunto_0,"\n")

#Tambien podemos eliminar elementos de un conjunto:
conjunto_0.discard("Pegasus")
print("Como vemos Pegasus ya no pertenece al conjunto_0=>\n")
print(conjunto_0,"\n")

#Por otro lado podemos eliminar conjuntos enteros:
print("Vamos a imprimir el estado actual de conjunto_1, antes de borrarlo por completo=>\n\n",conjunto_1,"\n")
conjunto_1.clear()
print("Vemos como se ha borrado el conjunto completamente=>\n\n", conjunto_1,"\n")
print("Pero el conjunto como tal no se elimina como variable en el script, tan solo los datos que tiene dentro, veamos que pasa si añadimos un elemento=>\n")
conjunto_1.add("HOLA MUNDO")
print(conjunto_1,"\n")

#Ahora vamos a comprobar si ciertos elementos estan dentro de nuestro conjunto:
print("Vamos a imprimir en pantalla el resultado de la funcion que nos devuelve True si un elemento esta dentro del conjunto y False si no pertenece al conjunto=>\n")
print("Comprobamos si el numero 3.141 esta dentro del conjunto_0=>\n\n",3.141 in conjunto_0,"\n")
print("Comprobamos si el numero 25 esta dentro del conjunto_0=>\n\n",25 in conjunto_0,"\n")

#Tambien podemos hacerlo al reves preguntar si un elemento no esta dentro:
print("Vamos a comprobar si el valor 25 no esta dentro de nuestro conjunto_0=>\n")
print(25 not in conjunto_0,":\tComo vemos devuelve el valor True porque es cierta la condicion dada, que 25 no pertenece al conjunto_0\n\n")

#Podemos realizar uniones de conjuntos, q es similar a la suma de dos listas, en el caso de los conjuntos la operacion suma no se puede realizar, asi que en detrimento de esta tenemos la operacion union que se realiza mediante el operador |:
conjunto_4=conjunto_2|conjunto_3
print("Realizamos la union de los conjuntos 2 y 3=>\n\n",conjunto_4,"\n\n")

#Tambien existe la operacion interseccion que aplicada a dos conjuntos nos devuelve los elementos que coinciden en ambos conjuntos:
print("Imprimimos la intersección entre los conjuntos 2 y 3=>\n\n",conjunto_2&conjunto_3,"\n\n")

#Por otra parte podemos calcular la diferencia entre dos conjuntos, que nos devuelve todos los elementos que estan en un conjunto pero que no estan en el otro:
print("Vamos a calcular la diferencia entre el conjunto_2 y el conjunto_3, el orden es importante en este caso=>\n\n",conjunto_2-conjunto_3,"\n")
print("Vamos a calcular la diferencia entre el conjunto_3 y el conjunto_2, esta vez invirtiendo el orden=>\n\n",conjunto_3-conjunto_2,"\n")
print("Como vemos lo que ocurre es que en el primer caso nos imprime todos los elementos que pertenecen al conjunto_2 pero solo los que NO pertenecen tambien al conjunto_3, en el segundo caso es al reves, nos imprime los elementos que pertenecen al conjunto_3 pero que NO pertenecen tmabien al conjunto_2, en resumen seria seleccionar los elementos que pertenecen a un conjunto pero que no coinciden con ninguno de los elementos de otro conjunto...\n\n")

#Otra de las operaciones que podemos aplicar a los conjuntos es la diferencia simétrica, esta selecciona todos los valores de ambos conjuntos excepto los que coinciden en ambos, es decir el total de ellos menos la interseccion de ambos:
print("Imprimimos ahora la diferencia geometrica entre el conjunto 2 y 3=>\n\n",conjunto_2^conjunto_3,"\n\n")

#Para terminar veamos los subconjuntos, superconjuntos, disconexos e inmutables :

#Subconjuntos:
print("¿Es el conjunto_2 un subconjunto del conjunto_4?=>\n\n",conjunto_2.issubset(conjunto_4),": como vemos nos devuelve el valor True ya que todos los valores del conjunto_2 estan dentro del conjunto_4\n\n")
print("¿Es el conjunto_2 un subconjunto del conjunto_3?=>\n\n",conjunto_2.issubset(conjunto_3),": como vemos nos devuelve el valor False ya que NO todos los valores del conjunto_2 estan dentro del conjunto_3\n\n")

#Superconjuntos:
print("¿Es el conjunto_4 un superconjunto del conjunto_2?=>\n",conjunto_4.issuperset(conjunto_2),":como vemos nos devuelve el valor True debido a que el conjunto_4 engloba todos los valores del conjunto_2\n\n")

#Disconexos:
print("¿Es el conjunto_2 disconexo del conjunto_3?=>\n",conjunto_2.isdisjoint(conjunto_3),":como vemos nos devuelve el valor False, debido a que ambos conjunto tienen elementos en comun\n")
print("¿Es el conjunto_3 disconexo del conjunto_0?=>\n",conjunto_3.isdisjoint(conjunto_0),":como vemos nos devuelve el valor True, debido a que ambos conjunto NO tienen ni un solo elemento en comun\n")
print("Si dos conjuntos son disconexos entonces su interseccion no existe=>\n",conjunto_0&conjunto_3,", como vemos NO existe la interseccion de ambos conjuntos porque son disconexos\n\n")

#Inmutables:
conjunto_5=frozenset({1,2,3,4})
print("Por ultimo tenemos los conjuntos inmutables, los cuales basicamente son como su nombre indica invariables, no se les puede añadir ningun elemento, ni modificar o eliminar los elementos existentes=>\n\n",conjunto_5,":el formato frozenset() indica que este conjunto es inmutable\n\n")

#//FIN
