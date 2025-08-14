with open("large_text.txt", "w") as f:
    for _ in range(240000):  # ~10MB total
        f.write("The quick brown fox jumps over the lazy dog.\n")

import time
import os

def apertura_por_caracter(nomArchivo):
    tiempoDuracion=time.time()
    with open(nomArchivo, "r") as a: #la r era para lectura de archivos
        while(True):#la únicaa forma de salir del ciclo es por medio del break, así se lee todo el archivo sin error :)
            lectura=a.read(1) # el 1 es para poder hacer caracter x caracter 
            if not lectura:
                break #para poder salirme del ciclo cuando termine de leer
    finalTiempo=time.time()

    print(f"La lectura del archivo caracter por caracter fue de {finalTiempo-tiempoDuracion} segundos")  


def apertura_por_linea(nomArchivo):
    tiempoDuracion=time.time()
    with open(nomArchivo, "r") as a: #la r era para lectura de archivos
        for line in a:
            pass #la instrucción no pide guardarlos en ninguna área, por eso solo se pasa a la siguiente :p
    finalTiempo=time.time()
    print(f"La lectura del archivo linea por linea fue de {finalTiempo-tiempoDuracion} segundos")  


def apertura_por_bytes(nomArchivo):
    tiempoDuracion=time.time()
    tamLectura=4096 #cant bytes solicitados por el profesor
    with open(nomArchivo, "rb") as a: 
         while(True):
            lectura=a.read(tamLectura)  
            if not lectura:
                break
    finalTiempo=time.time()
    print(f"La lectura del archivo 4096 por 4096 fue de {finalTiempo-tiempoDuracion} segundos")  

print(apertura_por_caracter("large_text.txt"))
print(apertura_por_linea("large_text.txt"))
print(apertura_por_bytes("large_text.txt"))


ruta_archivo = 'large_text.txt'
tamaño = os.path.getsize(ruta_archivo)
print(f"El tamaño del archivo es {tamaño} bytes")