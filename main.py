
'''Cuando Tom come un ratón, su energía aumenta en (12 joules + el peso del ratón en
gramos).
- La velocidad de Tom es 5 metros x segundo + (energía medida en joules / 10).
- Cuando Tom corre, su energía disminuye en (0.5 x cantidad de metros que corrió).'''

joules=12
energiaTom=100
#la velocidad es 5m x 1 segundo + energia en joules dividido 10

print('---------- Bienvenidos a play with Tom -------')

opc =1
while opc ==1:
    print("La energía inicial de Tom es:", energiaTom)
    pesoRaton = int(input("\nIngrese el peso del ratón que se comerá tom: "))
    nombreRaton = str(input("¿Como se llama el ratón?: "))
    print(nombreRaton, "ha sido entregado como trubuto a Tom (╥﹏╥) ")

    energiaTom = energiaTom + pesoRaton + joules
    energiaGanada = pesoRaton + joules
    print("La energía de Tom ahora es de:", energiaTom)

    segundos = int(input(f"Ingrese la cantidad de segundos que correrá Tom para atrapar a {nombreRaton}: "))

    velocidad = (5 * segundos) + (energiaTom / 10)
    print("La velocidad a la que correrá Tom es de: ", velocidad, " m/s")

    metros = (5 * segundos)
    energiafinal = energiaTom - (0.5 * metros)
    energiaPerdida = energiaTom - energiafinal

    if energiaGanada > energiaPerdida:
        energiaTom = energiafinal
        print(f"\nTom ganó energía al comerse a {nombreRaton}  \nEnergía final: {energiafinal}\n")
    else:
        energiaTom = energiafinal + energiaPerdida
        print("\nTom pierde", (energiaPerdida), "de energía al correr tantos metros, no comerá a",nombreRaton )
        print(nombreRaton,  "resucitó entre los muertos (っ◕‿◕)っ ♥\n")

    opc = int(input("Si desea entregar a otro ratón como tributo para Tom ingrese 1, si desea salir ingrese cualquier numero:"))

else:
    print("\nAdios!! Tom te extrañará y necesita comer, así que no te tardes mucho en volver!!")













'''print("Primero ingrese 1 para ingresar el peso del raton que se comera tom \nLuego presione 2 para indicar la "
      "cantidad de segundos que correra Tom para atrapar el raton \nSi desea salir presione 0")
opc=int(input('Ingrese una opcion: '))

while opc !=0:
    if opc == 1:
        ratonUsuario = int(input('\nPor favor ingrese el peso en gramos del raton que se comera Tom:'))


        for energiaActual

        print(energiaActual)

        if opc ==2:
            velocidadUsuario = int(input("Ingrese la cantidad de segundos que correra tom para atrapar al raton"))

            for i in velocidadUsuario:

                velocidadUsuario= velocidadUsuario *5 + i

    else:
        print("Debe ingresar una opcion correcta.")

        print("\nPrimero ingrese 1 para ingresar el peso del raton que se comera tom \n Luego presione 2 para indicar la "
          "cantidad de segundos que correra Tom para atrapar el raton \nSi desea salir presione 0")
        opc = int(input('Ingrese una opcion: '))

print("Adios!! Tom te extrañara y necesita comer, asi que no te tardes mucho en volver!!")'''


