apetece_helado = input("¿Te apetece helado? (Si/No): ")
tiene_dinero = input("Tienes dinero (Si/No): ")
esta_el_señor_de_los_helados = input("esta el señor de los helados (Si/No) ")
esta_tu_tia = input("¿Estás con tu tía? (Si/No)")

Te_apetece_helado = apetece_helado == "Si"
puedes_permitirtelo = tiene_dinero == "Si" or esta_tu_tia == "Si"
esta_el_señor = esta_el_señor_de_los_helados == "Si"

if Te_apetece_helado and puedes_permitirtelo and esta_el_señor:
    print("pues_comete_un_helado")
else:
    print("pues_nada")