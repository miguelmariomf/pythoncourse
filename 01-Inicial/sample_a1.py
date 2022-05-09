#!/usr/bin/env python


#Script 1=> Pedimos por consola que nos den un nombre y posteriormente imprimimos un Hola mi amigo y el nombre introducido por pantalla
def scp_1():
    print("Type your name:")
    nombre = input()
    print("Hello my friend", nombre)


#Script 2=> Pedimos por pantalla que nos den una palabra y posteriormente un número luego imprimimos la palabra introducida por pantalla el numero de veces que nos ha introducido tambien el usuario, por ejemplo si introduce run y 3 nos imprimirá run run run, el uso de \t es para generar un espacio entre repetición, ya que sin este la impresión sería: runrunrun
def scp_2():
    print("Send me a word that u like:")
    palabra = input()
    print("Send me a number that u like:")
    numero = input()
    print((palabra + "\t") * int(numero))

scp_2()
scp_1()

#//FIN
