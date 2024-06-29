#85Ejercicio_4
peso = int(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))
IMC = peso/(estatura**2)
if IMC==0:
    print("ERROR")
else:
    print(f"Su indice de masa corporal es: {round(IMC,2)}")
    
                     
