number_to_guess = 13
max_attempts = 5
user_attempts = 0
print("numero maximo de intentos = 5")
number = int(input("adivina un numero entre 0 y 20"))
if number == int(number_to_guess):
    print("menudo crack has acertado a la primera!")
else:
    print("has fallado el 1r intento!")
    number = int(input("intentalo de nuevo, tu puedes"))

    if number == int(number_to_guess):
        print("has acetado a la segunda eres toodo un pro")
    else:
        print("has fallado el 2n intento!")
        number = int(input("intentalo de nuevo craaack, solo llevas 2 intentos"))
        if number == number_to_guess:
            print("bastante bien has acertado despues de 3 intentos campeeon")
        else:
            print("has fallado el 3r intento!")
            number = int(input("intentalo de nuevo, te quedas 2 intentoos!!"))
            if number == number_to_guess:
                print("has acertdo al cuarto intento, fucking boss")
            else:
                print("has fallado el 4t intento!")
                number = int(input("venga va, solo te queda 1 intento chavaaal!!"))
                if number == number_to_guess:
                    print("que suerte campeon has acertado a la ultima")
                else:
                    print("has fallado el ultimo intento!")
                    number = int(input("eres un poco bastante muy malo, has perdido, otra vez sera craaack xd"))