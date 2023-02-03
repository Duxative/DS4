import random

def leer_archivo(archivo):
    data = []
    with open(archivo,"r",encoding="utf-8") as a:
        data = a.readlines()
        data = [cadena.strip("\n") for cadena in data]
    return data

def leer_tablero(n: int)->dict:
    d = {}
    for i in range(0,n+1):
        d[i] = leer_archivo(f"ahorcado-{i}.txt")
    return d

def despliega_tablero(tablero:list)->None:
    for renglon in tablero:
        print(renglon)

def adivina(lista_palabras:list, tableros:dict)->None:
    palabra = random.choice(lista_palabras)
    palabra = palabra.upper()
    lista_letras = [[x,False] for x in palabra]
    abecedario = {chr(x):chr(x) for x in range(ord('A'),ord('z'))+1}
    strikes = 0
    en_juego = True
    while en_juego == True:
        despliega_palabra(lista_letras)
        despliega_abc(abecedario)
        despliega_tablero(tableros[strikes])
        for lista in lista_letras:
            if lista[1] == "_":
                completo = False
        if completo == True:
            en_juego = False
            continue
        else:
            if strikes == 6:
                en_juego = False
                break
        letra = input("Selecciona una letra")
        letra = letra.upper()

        if len(letra) != 1:
            continue
        else:
            intento = False
            for lista in lista_letras:
                if letra == lista[0]:
                    lista[1]
                    intento = True
        if intento == False:
            strikes +=1
        if letra in abecedario:
            abecedario[letra] = "*"
        en_juego = False

def despliega_palabra(lista_letras:list):
    lista = [x[1]for x in lista_letras]
    palabra = " ".join(lista)
    print(palabra)

def despliega_abc(diccionario:dict)->None:
    abc= [value for key,value in diccionario.item()]
    abc = "".join(abc)
    print(abc)

def main(archivo):
    lista_palabras = leer_archivo(archivo)
    palabra = random.choice(lista_palabras)
    print(palabra)
    tableros = leer_tablero(7)
    despliega_tablero(tableros[0])
    adivina(lista_palabras,tableros)

if __name__ =="__main__":
    archivo = "palabras.txt"
    main(archivo)