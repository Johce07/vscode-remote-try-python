#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
# write 'hello world' to the console
print("hello world")

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

def jugar_ronda(opcion_jugador):
    opciones = ['rock', 'paper', 'scissors']
    opcion_oponente = random.choice(opciones)

    print(f"\nTu elección: {opcion_jugador}")
    print(f"Elección del oponente: {opcion_oponente}")

    if opcion_jugador == opcion_oponente:
        return "Empate"
    elif (opcion_jugador == 'rock' and opcion_oponente == 'scissors') or \
         (opcion_jugador == 'scissors' and opcion_oponente == 'paper') or \
         (opcion_jugador == 'paper' and opcion_oponente == 'rock'):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"

def main():
    victorias = 0
    rondas = 0

    while True:
        opcion_jugador = input("\nElige rock, paper o scissors: ").lower()

        if opcion_jugador in ['rock', 'paper', 'scissors']:
            resultado = jugar_ronda(opcion_jugador)
            print(resultado)

            if resultado == "¡Ganaste!":
                victorias += 1

            rondas += 1
        else:
            print("Opción no válida. Por favor, elige rock, paper o scissors.")

        seguir_jugando = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if seguir_jugando != 's':
            break

    print(f"\n¡Juego terminado!\nNúmero de victorias: {victorias}\nNúmero de rondas jugadas: {rondas}")

if __name__ == "__main__":
    main()
