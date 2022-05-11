#!/usr/bin/env python

#Voy a crear una variable para guardar colores y usarlos en las impresiones por pantalla para darle un toque estético:

#Paleta de colores sin efectos:
color_blanco="\x1b[0;37m"
color_cian="\x1b[0;36m"
color_morado="\x1b[0;35m"
color_azul="\x1b[0;34m"
color_amarillo="\x1b[0;33m"
color_verde="\x1b[0;32m"
color_rojo="\x1b[0;31m"
color_negro="\x1b[0;30m"

#Paleta de colores con efecto negrita:
color_blanco_negrita="\x1b[1;37m"
color_cian_negrita="\x1b[1;36m"
color_morado_negrita="\x1b[1;35m"
color_azul_negrita="\x1b[1;34m"
color_amarillo_negrita="\x1b[1;33m"
color_verde_negrita="\x1b[1;32m"
color_rojo_negrita="\x1b[1;31m"
color_negro_negrita="\x1b[1;30m"

#Creamos una lista y la rellenamos con texto (en este caso los dias de la semana por ejemplo):

lista=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

#Imprimimos todos los elementos de nuestra lista:
print(color_amarillo_negrita,"\nTodos los elementos dentro de la lista=>\n")
print(color_blanco,lista,"\n\n")

#Imprimimos el primero y el último elemento de nuestra lista:
print(color_verde_negrita,"El primero y el último elemento de la lista=>\n")
print(color_blanco,lista[0],lista[6],"\n\n")

#Ahora Imprimimos cada elemento de la lista por separado y su posición en la lista:
print(color_rojo_negrita,"Todos los elementos de la lista iterando dentro de ella=>\n")
for x in range (0,len(lista)):
  print(color_blanco,x,"-",lista[x])
  
print("\n")

#Traducimos el primero y el último día de la semana:
lista[0]="Lunes"
lista[6]="Domingo"
print(color_cian_negrita,"Traduciendo el primero y último de la lista=>\n")
print(color_blanco,lista,"\n\n")

#Ahora vamos a eliminar dias de la semana de nuestra lista, por ejemplo vamos a eliminar el Lunes, el Domingo y uno intermedio como el Jueves:

#Eliminación del Lunes por índice:
lista.pop(0)
print(color_morado_negrita,"Eliminamos el Lunes mediante el indice con .pop(0)=>\n")
print(color_blanco,lista,"\n\n")

#Eliminación del Domingo por valor:
lista.remove("Domingo")
print(color_amarillo_negrita,"Eliminamos el Domingo mediante el valor con .remove(Domingo)=>\n")
print(color_blanco,lista,"\n\n")

#Eliminación del Jueves por valor:
lista.remove("Thursday")
print(color_verde_negrita,"Eliminamos el Jueves mediante el valor con .remove(Thursday)=>\n")
print(color_blanco,lista,"\n\n")

#Ahora vamos añadir el Domingo al final de la lista para mantener el orden inicial:
lista.append("Sunday")
print(color_rojo_negrita,"Añadimos el Domingo al final de la lista con .append(Sunday)=>\n")
print(color_blanco,lista,"\n\n")

#Ahora vamos añadir el Lunes y Jueves que son los días que nos faltan en la lista, mediante el metodo .insert(posicion,valor):
lista.insert(0,"Monday")
lista.insert(3,"Thursday")
print(color_cian_negrita,"Añadimos el Lunes y el Jueves a la lista mediante el método.insert(posicion,valor)=>\n")
print(color_blanco,lista,"\n\n")

#Ahora vamos a eliminar los 3 últimos días de la semana de la lista y luego los vamos añadir de nuevo mediante .extend([valor,valor,valor]):
print(color_morado_negrita,"Eliminamos los tres últimos elementos de la lista y luego los añadimos mediante el método\n.extend([valor,valor,valor])=>\n")
lista.pop(-1)
lista.pop(-2)
lista.pop(-3)
print(color_blanco,lista,"\n")
lista.extend(["Friday","Saturday","Sunday"])
print(color_blanco,lista,"\n\n")

#//FIN
