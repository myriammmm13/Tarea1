"""
Escriba un programa en Python que permita guardar y 
recuperar de un archivo binario, una lista de diccionarios 
(ustedes son libres de crear la estructura y agregar los datos 
que quieran, siempre y cuando sea una lista de diccionarios). 
"""
import pickle
list_dic=[]
list_dic.append({"Nombre":"Myriam", "Apodo":"Gemela", "Edad": "19", "Residencia":"Liberia"})
list_dic.append({"Nombre":"Mariam", "Apodo":"Gemela", "Edad": "19", "Residencia":"San Jose"})
list_dic.append({"Nombre":"Sara", "Apodo":"Ma", "Edad": "54", "Residencia":"Bijagua"})
list_dic.append({"Nombre":"Tiana", "Apodo":"Titi", "Edad": "31", "Residencia":"Heredia"})

def lectura(archivo):
    with open(archivo, "wb") as AB:
        pickle.dump(list_dic, AB)

def esritura(archivo):
    pass



lectura("archivo.bin")

