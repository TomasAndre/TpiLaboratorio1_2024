import random  # se importa random para poder crear numero randoms


def juego_adivinar_numero():  # funcion donde se encuentra el juego
    numero_para_adivinar = random.randint(1, 20)  # se crea un numero al azar del 1 al 20 y se guarda en una variable
    intentos = 0
    print("¡¡¡Descubre el numero del 1 al 20!!!")
    while True:
        try:  # el juego se encuentra en un bloque try para asegurar que el juego funcione si ingresa un valor que no es un numero
            numero = int(input("Ingrese un numero: "))
            intentos += 1
            if numero < numero_para_adivinar:
                print("-" * 45)
                print("-> EL numero", numero,"es menor al numero secreto.")
                print("-" * 45)
            elif numero > numero_para_adivinar:
                print("-" * 45)
                print("-> EL numero", numero,"es mayor al numero secreto.")
                print("-" * 45)
            else:
                print("◙" * 30)
                print(f"¡¡Felicidades adivinaste el numero!!\nNumero de intentos: {intentos} ")
                print("◙" * 30)
                break
        except ValueError:
            print("Ingrese un valor numerico valido:")


def jugar_devuelta():  # funcion para saber si el jugador quiere jugar de vuelta
    while True:
        try:
            print("Ingrese:\n1- Si quiere jugar de nuevamente \n2- Si no quiere jugar nuevamente")
            jugar = int(input("¿Desea jugar de vuelta?: "))

            if jugar == 1:
                juego_adivinar_numero()
            elif jugar == 2:
                break
            else:
                print("☼" * 20)
                print("Ingrese solamente 1 o 2 ")
                print("☼" * 20)
        except ValueError:
            print("☼" * 20)
            print("Ingrese solamente 1 o 2 ")
            print("☼" * 20)


def tira_la_moneda():
    while True:
        try:
            print("-" * 60)
            eleccion = input("Elige una de las caras de la moneda: ||Cara|| o ||Cruz||\n->  ").lower()
            print("-" * 20)
            if eleccion not in ["cara", "cruz"]:
                raise ValueError("Opción inválida. Por favor ingresa 'cara' o 'cruz'.")
        except ValueError as e:
            print(e)
            continue

        # Simula el lanzamiento de la moneda
        resultado = random.choice(["cara", "cruz"])

        print("*" * 25)
        print(f"La moneda cayó en: {resultado}")
        print("*" * 25)

        # Verifica si el jugador ganó o perdió
        if eleccion == resultado:
            print("◙" * 20)
            print("¡Bien, Ganaste! ☻☻")
            print("◙" * 20)
        else:
            print("◙" * 20)
            print("¡Qué pena, Perdiste! ☹☹")
            print("◙" * 20)

        # Pregunta al jugador si quiere jugar otra partida
        while True:
            try:
                jugar_otra = input("¿Quieres jugar otra partida? (s/n):\nS = SI\nN = NO\n->  ").lower()
                if jugar_otra not in ['s', 'n']:
                    raise ValueError("Opción inválida. Por favor ingresa 's' o 'n'.")
                break  # Sale del bucle si la respuesta es válida
            except ValueError as e:
                print(e)
                continue

        # Si el jugador elige "n", se termina el juego
        if jugar_otra == 'n':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

def piedra_papel_tijera():
    while True:  # Bucle para jugar nuevamente
        vida_usuario = 3
        vida_pc = 3

        while vida_usuario != 0 and vida_pc != 0:
            aleatorio = random.randrange(0, 3)
            pc = ""
            print("-" * 40)
            print("Vidas restantes de 'Jugador':", vida_usuario, "♥")
            print("Vidas restantes de 'PC':", vida_pc, "♥")
            print("-" * 40)

            # Comprobar la entrada de datos.
            while True:
                try:
                    opcion = int(input("¿Qué eliges? \n1) Piedra \n2) Papel \n3) Tijera\n->  "))
                    if opcion == 1 or opcion == 2 or opcion == 3:
                        break
                    else:
                        print("Por favor, ingresa un número entre 1 y 3.")
                except ValueError:
                    print("Entrada no válida. Por favor, ingresa un número.")

            if opcion == 1:
                usuario = "piedra"
            elif opcion == 2:
                usuario = "papel"
            elif opcion == 3:
                usuario = "tijera"
            print("Jugador eligio: ->", usuario)

            if aleatorio == 0:
                pc = "piedra"
            elif aleatorio == 1:
                pc = "papel"
            elif aleatorio == 2:
                pc = "tijera"
            print("PC eligió: ->", pc)

            print("*" * 40)

            if pc == "piedra" and usuario == "papel":
                print("¡¡GANASTE!!, ||Papel 'envuelve' Piedra||")
                vida_pc -= 1
            elif pc == "papel" and usuario == "tijera":
                print("¡¡GANASTE!!, ||Tijera 'corta' Papel||")
                vida_pc -= 1
            elif pc == "tijera" and usuario == "piedra":
                print("¡¡GANASTE!!, ||Piedra 'pisa' Tijera||")
                vida_pc -= 1

            if pc == "papel" and usuario == "piedra":
                print("¡¡PERDISTE!!, Papel 'envuelve' Piedra")
                vida_usuario -= 1
            elif pc == "tijera" and usuario == "papel":
                print("¡¡PERDISTE!!, Tijera 'corta' Papel")
                vida_usuario -= 1
            elif pc == "piedra" and usuario == "tijera":
                print("¡¡PERDISTE!!, Piedra 'pisa' Tijera")
                vida_usuario -= 1
            elif pc == usuario:
                print("EMPATE")

            print("*" * 40)

            if vida_usuario == 0 or vida_pc == 0:
                if vida_usuario == 0:
                    print("◙" * 30)
                    print("JUEGO TERMINADO!! GANA PC")
                    print("◙" * 30)
                    break
                if vida_pc == 0:
                    print("◙" * 30)
                    print("JUEGO TERMINADO!! ¡GANASTE!")
                    print("◙" * 30)
                    break

        # Rejugar
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
            print(f"||intentos restantes: {intentos} ♥||")  # Mostrar intentos restantes.
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


lista_juegos = ["PIEDRA PAPEL O TIJERA", "ADIVINA EL NUMERO", "TIRAR LA MONEDA", "ADIVINA LA PALABRA ☻☻"]
while True:
    try:
        print("Lista de juegos disponibles: \n 1-PIEDRA PAPEL O TIJERA \n 2-ADIVINA EL NUMERO \n 3-TIRAR LA MONEDA \n 4-ADIVINA LA PALABRA \n 5-Salir")
        menu = int(input("Seleccione un juego (1-4) o (5) para salir:\n->  "))
        if menu < 1 or menu > 5:
            print("Opción no válida. Por favor, elija un número entre 1 y 5.")
            continue  # Vuelve a pedir la opción si está fuera del rango
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        continue  # Vuelve a pedir la opción si el input no es un número

    if menu == 1:
        print("BIENVENIDO A", lista_juegos[0])
        piedra_papel_tijera()
    elif menu == 2:
        print("BIENVENIDO A", lista_juegos[1])
        juego_adivinar_numero()
        jugar_devuelta()
    elif menu == 3:
        print("BIENVENIDO A", lista_juegos[2])
        tira_la_moneda()
    elif menu == 4:
        print("BIENVENIDO A", lista_juegos[3])
        juego_adivina_palabra()
    elif menu == 5:
        print("Gracias por jugar. ¡Hasta la próxima!")
        break