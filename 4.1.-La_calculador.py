tipo_operacion = input("¿Que operacion quieres realizar sumar/restar/multiplicar/dividir?")
numero_1 = int(input("Dime el primer numero de tu operacion"))
numero_2 = int(input("Dime el segundo numero de tu operacion"))
print(tipo_operacion)
if tipo_operacion == "sumar":
    print("El resultado de tu suma es {}".format(int(numero_1 + numero_2)))
if tipo_operacion == "restar":
    print("El resultado de tu suma es {}".format(int(numero_1 - numero_2)))
if tipo_operacion == "multiplicar":
    print("El resultado de tu multiplicacion es {}".format(int(numero_1 * numero_2)))
if tipo_operacion == "dividir":
    print("El resultado de tu division es {}".format(int(numero_1 / numero_2)))