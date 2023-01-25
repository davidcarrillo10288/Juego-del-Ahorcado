import os
import random
import numpy as np
import pandas as pd
from time import sleep

##Quizás pida instalar lo siguiente, para que reconozca el archivo excel - pip install openpyxl

def bienvenida():
        print("BIENVENIDO A ESTE JUEGO")
        print("""                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | |_| | | | | |_| | | | | | | |_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     """
        )
        
def instrucciones():
    print("""
          El juego del ahorcado, se basa en descubrir la palabra oculta.
          Debes escoger entre el grupo de palabras con el que te gustaria jugar, Tenemos los siguientes:
          1 - Lista de deportes olimpicos
          2 - Lista de frutas
          3 - Lista de animales
          4 - Lista de paises
          """)

def grupo_de_palabras():
    
    df = pd.read_excel("JUEGO DEL AHORCADO.xlsx")
    deportes = df["DEPORTES"].values
    deportes = [x for x in deportes if pd.isnull(x) == False]
    frutas = df["FRUTAS"].values
    frutas = [x for x in frutas if pd.isnull(x) == False]
    animales = df["ANIMALES"].values
    animales = [x for x in animales if pd.isnull(x) == False]
    paises = df["PAISES"].values
    paises = [x for x in paises if pd.isnull(x) == False]

    grupo_de_palabras = [deportes,frutas,animales,paises]

    return grupo_de_palabras
    

def datos1(deportes):
    deportes_corregido = [x.upper().replace(" ","") for x in deportes]
    return deportes_corregido

def datos2(frutas):
    frutas_corregidas = [x.upper().replace(" ","") for x in frutas] 
    return frutas_corregidas

def datos3(animales):
    animales_corregidos = [x.upper().replace(" ","") for x in animales] 
    return animales_corregidos

def datos4(paises):
    paises_corregidos = [x.upper().replace(" ","") for x in paises]      
    return paises_corregidos
     
             
def run():               
    
    IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']
       
    word = random.choice(basededatos)
    spaces = ["_"]*len(word)
    intentos = 0
    
    while True:       
        os.system("cls")
        bienvenida()
        for character in spaces:
            print(character, end="  ")
        print()
        print(IMAGES[intentos])
        print()
        letra = input("Escoge una letra: ").upper()

        found = False
        for idx,character in enumerate(word):
            if character == letra:
                spaces[idx] = letra
                found = True
        
        if not found:
            intentos += 1
        
            if intentos == 4:
                print("Estás próximo a perder, te daré una pista")
                word_new = ""
                for i in range(round(len(word)/2)):
                    word_new += word[i]
                print(f"la mitad de la palabra a adivinar es {word_new}")
                sleep(10)
        
        if "_" not in spaces:
            os.system("cls")
            print("Ganaste")
            break
            input()
        
        if intentos == 6:
            os.system("cls")
            print("Perdiste")
            break
            input()

if __name__ == '__main__':
    instrucciones()
    a = int(input("Escribe el grupo de palabras con el que te gustaria jugar, escoge del 1 al 4: "))
    if a == 1:
        basededatos = datos1(grupo_de_palabras()[0])
        #basededatos_mayu = list(map(str.upper(),basededatos))
    elif a == 2:
        basededatos = datos2(grupo_de_palabras()[1])
        #basededatos_mayu = list(map(str.upper(),basededatos))
    elif a == 3:
        basededatos = datos3(grupo_de_palabras()[2])
        #basededatos_mayu = list(map(str.upper(),basededatos))
    elif a == 4:
        basededatos = datos4(grupo_de_palabras()[3])
        #basededatos_mayu = list(map(str.upper(),basededatos))
    else:
        print("Deberias escoger una opcion, nos vemos a la proxima")
    run()
    