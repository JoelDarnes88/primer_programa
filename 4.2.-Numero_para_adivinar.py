numero_para_adivinar = input("Di el numero que quieres que tu compañero adivine")
intento_numero = input("Di el numero que ha escrito tu compañero")
if intento_numero == numero_para_adivinar:
    print("has encertado el numero de tu compañero a la primera")
while intento_numero != numero_para_adivinar:
    print("Vuelvelo a intentar")
    input("Di el numero que ha escrito tu compañero")
