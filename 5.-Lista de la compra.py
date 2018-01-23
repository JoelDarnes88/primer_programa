mi_lista = []
input_usuario = input("¿Qué necesitas comprar? (cuando hayas acabado escribe FIN):")

while input_usuario != "FIN":
    mi_lista.append(input_usuario)
    input_usuario = input("¿Qué necesitas comprar? (cuando hayas acabado escribe FIN):")
for item in mi_lista:
    print("Tengo que comprar {}".format(item))
#otra manera menos útil de hacer la parte de for item in...
largo_lista = len(mi_lista)
indice_actual = 0

while indice_actual < largo_lista:
    print("Tengo que comprar {}".format(mi_lista[indice_actual]))
    indice_actual += 1

print("Esta es la lista de la compra")

