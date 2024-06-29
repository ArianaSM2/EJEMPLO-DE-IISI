#Ejercicio_7
ahorro = int(input("Ingrese sus ahorros: "))
año = int(input("Ingrese el año que quiere ver: "))
ahorro_1 = ahorro + (ahorro*0.04)
ahorro_2 = ahorro_1 + (ahorro_1*0.04)
ahorro_3 = ahorro_2 + (ahorro_2*0.04)
if año == 1:
    print(f"El ahorro el primer año es de: {round(ahorro_1,2)}")
elif año == 2:
    print(f"El ahorro el segundo año es de: {round(ahorro_2,2)}")
elif año == 3:
    print(f"El ahorro el tercer año es de: {round(ahorro_3,2)}")
else:
    print("Ingreso un número mayor a 3")
