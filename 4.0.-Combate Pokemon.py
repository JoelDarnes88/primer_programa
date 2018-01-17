pokemon_elegido = input("¿Contra qué Pokemon quieres luchar? (Squirtle / Charmander / Bulbasaur) :")

vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    ataque_squirtle = 8
    nombre_pokemon = "Squirtle"
elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    ataque_charmander = 7
    nombre_pokemon = "Charmander"
elif pokemon_elegido == "Bulbasaur":
    vida_enemigo = 80
    ataque_bulbasaur = 10
    nombre_pokemon = "Bulbasaur"

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Qué ataque vamos a usar? (Chispazo / Bola voltio) ")

    if ataque_elegido == "Chispazo":
        vida_enemigo -= 10
    elif ataque_elegido == "Bola voltio":
        vida_enemigo -= 12
    print("La vida del enemigo ahora es de {}".format(vida_enemigo))
    if pokemon_elegido == "Squirtle":
        print("{} te ha quitado 8 de vida".format(nombre_pokemon))
        vida_pikachu -= ataque_squirtle
    elif pokemon_elegido == "Charmander":
        print("{} te ha quitado 7 de vida".format(nombre_pokemon))
        vida_pikachu -= ataque_charmander
    elif pokemon_elegido == "Bulbasaur":
        print("{} te ha quitado 10 de vida".format(nombre_pokemon))
        vida_pikachu -= ataque_bulbasaur
    print("La vida de pikachu es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("¡Has ganado!")
if vida_pikachu <= 0:
    print("¡Has perdido!")
print("El combate ha terminado")