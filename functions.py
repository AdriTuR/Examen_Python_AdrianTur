#===========================================
#================== IMPORTS ================
import csv
#===========================================
#============= READ DATA() =================

def read_data(fichero_csv):
    diccionario = {}
    with open(fichero_csv, "r") as f:
        reader = csv.reader(f)
        atributos = next(reader)
        for i, row in enumerate(reader):
            if row[0] != "":
                diccionario["dato"+str(i+1)] = {}
                for j, atributo in enumerate(atributos):
                    diccionario["dato"+str(i+1)][atributo] = row[j]
    if len(diccionario) < 10:
        raise ValueError("El fichero tiene menos de 10 lineas con valor en todos los atributos")
    return diccionario

#===========================================
#=============== SLPLIT() ==================

def split(dicionario_split, atributo):
    diccionario_white = {}
    diccionario_red = {}
    for i in dicionario_split:
        if atributo in dicionario_split[i]:
            if dicionario_split[i][atributo] == "white":
                diccionario_white[i] = dicionario_split[i]
                del diccionario_white[i][atributo]
            elif dicionario_split[i][atributo] == "red":
                diccionario_red[i] = dicionario_split[i]
                del diccionario_red[i][atributo]
            else:
                raise ValueError("El atributo seleccionado no existe")
        else:
            raise ValueError("El atributo seleccionado no existe")
    return diccionario_white, diccionario_red

#===========================================
#=============== REDUCE() ==================

def reduce(diccionario_reduce, atributo):
    lista_reduce = []
    for i in diccionario_reduce:
        if atributo in diccionario_reduce[i]:
            lista_reduce.append(diccionario_reduce[i][atributo])
        else:
            raise ValueError("El atributo seleccionado no existe")
    return lista_reduce

#===========================================
#============= SILHOUETTE() ================

def silhouette(lista1, lista2):
    a = 0
    b = 0
    for i in lista1:
        for j in lista1:
            if i != j:
                a += (abs(float(i) - float(j)))**2
        a = a / (len(lista1) - 1)
        for k in lista2:
            b += (abs(float(i) - float(k)))**2
        b = b / len(lista2)

        if a > b:
            s = (b - a) / a
        else:
            s = (b - a) / b
    return s




