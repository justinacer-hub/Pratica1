import random



categories = {
    "programacion": ["python","programa", "variable", "funcion", "bucle"],
    "tipos de datos": ["cadena", "entero", "lista"],
}


print("Categorias disponibles: ")
for categoria in categories:
    print(f"- {categoria}")

categoria_elegida = input("Elegi una categoria: ")

while categoria_elegida not in categories:
    print("Categoria invalida, intenta otra.")
    categoria_elegida = input("Elegi categoria: ")

#Lista mezclada de todas las palabras de la categoria
sampled_word = random.sample(categories[categoria_elegida], len(categories[categoria_elegida]))

puntaje_total = 0 #acumulado de puntaje

for word in sampled_word:
    guessed = []
    attempts = 6
    puntos = 0

    print("¡Bienvenido al Ahorcado!")
    print()

    while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            puntos += 6
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")
    
        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no valida")
            continue

        if letter in guessed:
          print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
             guessed.append(letter)
             attempts -= 1
             puntos -= 1 
             print("Esa letra no está en la palabra.")
        print()
    else:
        puntos = 0
        print(f"¡Perdiste! La palabra era: {word}")

        # Preguntar si quiere seguir jugando (solo si no es la última palabra)
    if word != sampled_word[-1]:
         keep_going = input("¿Querés seguir jugando? Responder NO para terminar\n")
         if keep_going.lower() == "no":
             break

    puntaje_total += puntos
    print(f"Tu puntaje es: {puntos}")
    print(f"Puntaje acumulado: {puntaje_total}")

print("juego terminado.")
print(f"Puntaje acumulado: {puntaje_total}")
