def progreso_palabra(palabra, letras_adivinadas):
    progreso = [letra if letra in letras_adivinadas else '_' for letra in palabra] #Mostrar letras adivinadas en la palabra y '_' en las letras mo adivinadas
    return ' '.join(progreso) #Agrupar '_' dejando un espacio

def guardar_resultado(juego_info):
    with open("resultados_juego.txt", "a") as info:
        info.write(juego_info + "\n")  # Agregar una nueva línea con la información del juego


def juego_adivina_palabra():
    while True:
        while True:
            # ingreso de palabra y pasaje a mayuscula.
            palabra = input("||Para poder jugar, Ingresa la palabra a adivinar||:\n->  ").upper()
            if len(palabra) > 2 and palabra.isalpha():  # Comprobar que la palabra tenga más de 2 letras
                break
            else:
                print("-" * 75)
                print("Por favor, ingresa una palabra con más de 2 letras.(Numeros no Permitidos)")
                print("-" * 75)
        intentos = 5  # intentos para adivinar.
        letras_adivinadas = set()
        letras_erradas = set()
        print("\n" * 20)
        print("\n¡¡Comienza el juego, Adivinar la Palabra!! :D\n")
        # Mostrar en pantalla '_' en letras no adivinadas.
        print(progreso_palabra(palabra, letras_adivinadas))

        print("\n")

        while intentos > 0:  # Ejecutar mientras aun tenga intentos.
            print("*" * 25)
            print(f"||intentos restantes: {intentos}||")  # Mostrar intentos restantes.
            letra = input("Adivina una letra: -> ").upper()  # Pasaje de letra ingresada a mayuscula.
            print("-" * 30)
            print("\n" * 3)

            if letra in letras_adivinadas or letra in letras_erradas:  # Comprobar que la letra ingresada no fue ingresada anteriormente.
                print(f"◙◙ Ya a ingresado anteriormente la letra ║{letra}║, ingrese otra letra.◙◙")
                progreso_actializado = progreso_palabra(palabra, letras_adivinadas)
                print(progreso_actializado)
                continue

            if letra in palabra:  # comprobar si la letra ingresada esta en la palabra.
                letras_adivinadas.add(letra)  # Agregar la letra adivinada al conjunto 'letras_adivinadas'.
                print(f"◙◙¡Bien!, adivinaste la letra◙◙ ║{letra}║")
            else:
                intentos = intentos - 1  # Restar intentos.
                letras_erradas.add(letra)  # Agregar letra incorrecta al conjunto 'letras_erradas'.
                print(f"◙◙¡Incorrecto!, la letra ║{letra}║ no esta en la palabra◙◙")

            progreso_actializado = progreso_palabra(palabra, letras_adivinadas)
            print(progreso_actializado)  # Mostrar el progreso de letras adivinadas.

            if "_" not in progreso_actializado:  # Comprobar si ya adivinaron todas las letras de la palabra.
                print("\n" * 3)
                print("◙" * 30)
                print("☻☻¡Felesidades, adivinaste la palabra!☻☻")
                print("◙" * 30)
                resultado = f"Palabra: {palabra}, Resultado: Adivino"
                guardar_resultado(resultado)  # Guardar el resultado en el archivo
                break
        else:
            print("◙" * 40)
            print(f"◙◙¡Perdiste!◙◙ ◙◙La palabra a adivinar fue: ║{palabra}║◙◙ ")  # Mostrar que ya no hay intentos.
            print("◙" * 40)
            resultado = f"Palabra: {palabra}, Resultado: Perdio"
            guardar_resultado(resultado)  # Guardar el resultado en el archivo

        jugar_nuevamente = input("¿Quieres jugar nuevamente? \n'S/N'\nS = Si\nN = No\n-> ").upper()
        if jugar_nuevamente == 'N':
            print("¡Gracias por jugar! :)")
            break
        while jugar_nuevamente != "S" and jugar_nuevamente != "N":
            print("Valores permitidos: S/N")
            jugar_nuevamente = input("¿Quieres jugar nuevamente? \n'S/N'\nS = Si\nN = No\n-> ").upper()
        if jugar_nuevamente == 'N':
            print("¡Gracias por jugar! :)")
            break


juego_adivina_palabra()