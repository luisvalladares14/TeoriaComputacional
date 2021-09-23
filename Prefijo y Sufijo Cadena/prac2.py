import msvcrt

print("******Practica 2******")
print("Este programa calcula el prefijo y subfijo de una cadena.")
print("Simplemente tienes que poner el valor de tu cadena. Por ejemplo abcd || dcba || 1234")
print("")
print("")

print("Introduce la cadena: ")
cadena = input()
print('w= '+ cadena)
print("")
print('***********************************************************************************')
i=0
prefijos = []
pref = ['Ɛ']
print('El prefijo de la cadena ['+ cadena + '] son: ')
for i in cadena:
    prefijos.append(i)
    x = "".join(prefijos)
    pref.append(x)
y = ",".join(pref)
print('['+ y + ']') 
print("")
print('************************************************************************************')

sufijos = []
cadena2 = cadena[::-1]
suf=['Ɛ']
j = 0
print('El subfijo de la cadena ['+ cadena + '] son: ')
for j in cadena2:
    sufijos.append(j)
    z = "".join(sufijos)
    suf.append(z)
a = ",".join(suf)
print('[' + a + ']')
print("")
print("Presiona enter para salir.")
msvcrt.getch()
