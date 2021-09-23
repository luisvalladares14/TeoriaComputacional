from prac1_1 import potencia, pot_mas, pot
import msvcrt

print("******Practica 1******")
print("Este programa calcula la potencia de un lenguaje. La entrada del alfabeto tiene que ser sin corchetes, separados por una coma y sin espacios")
print("Por ejemplo a,b || 0,1 || hola,adios,bye")
print("Y n que sera la potencia a la que se elevara este lenguaje, la entrada tiene que ser un numero mayor")
print("Por ejemplo 1 || 2 || 3 ")
print("")
print("")
print("****************************************************************************************************")
print("Ingrese el alfabeto: ")
alfabeto = input()
print('Ingrese n para la potencia:')
n = int(input())
print('El alfabeto ingresado es L^' + str(n) + '= [' + alfabeto + ']')
print('****************************************************************************************************')
alf = alfabeto.split(',')
print("El resultado es:")
if n == 1:
    pot(alf, n)
elif n>1 and n<3:
    print(potencia(alf))
elif n>2:
    pot_mas(potencia(alf), alf, n)

print("")    
print("Presiona enter para salir.")
msvcrt.getch()
