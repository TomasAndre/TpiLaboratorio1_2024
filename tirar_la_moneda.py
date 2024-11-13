import random

def tira_la_moneda():
    print("¡Bienvenido al juego de cara o cruz!")  
   
    while True:
        try:
            eleccion = input("Elige: cara o cruz: ").lower()  
            if eleccion not in ["cara", "cruz"]:
                raise ValueError("Opción inválida. Por favor ingresa 'cara' o 'cruz'.")
        except ValueError as e:
            print(e)  
            continue  

        # Simula el lanzamiento de la moneda
        resultado = random.choice(["cara", "cruz"])
        print(f"La moneda cayó en: {resultado}")

        # verifica si el jugador ganó o perdió
        if eleccion == resultado:
            print("¡Ganaste!")
        else:
            print("Perdiste.")

        # pregunta al jugador si quiere jugar otra partida
        try:
            jugar_otra = input("¿Quieres jugar otra partida? (s/n): ").lower()
            if jugar_otra not in ['s', 'n']:
                raise ValueError("Opción inválida. Por favor ingresa 's' o 'n'.")
        except ValueError as e:
            print(e) 
            continue  

        # Si el jugador elige "n", se termina el juego
        if jugar_otra == 'n':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

# Ejecuta el juego
tira_la_moneda()
