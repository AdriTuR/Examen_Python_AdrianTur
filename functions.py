import csv
#===========================================
#============= READ DATA() =================

def read_data(fichero_csv):
    datos = {}
    with open(fichero_csv, "r") as f:
        reader = csv.reader(f)
        atributos = next(reader)
        for i, row in enumerate(reader):
            if row[0] != "":
                datos["dato"+str(i+1)] = {}
                for j, atributo in enumerate(atributos):
                    datos["dato"+str(i+1)][atributo] = row[j]
    return datos

#===========================================
#=============== SLPLIT() ==================

def split(dicionario, atributo):
    diccionario_white = {}
    diccionario_red = {}
    for i in dicionario:
        if atributo in dicionario[i]:
            if dicionario[i][atributo] == "white":
                diccionario_white[i] = dicionario[i]
                del diccionario_white[i][atributo]
            elif dicionario[i][atributo] == "red":
                diccionario_red[i] = dicionario[i]
                del diccionario_red[i][atributo]
            else:
                raise ValueError("El atributo seleccionado no existe")
        else:
            raise ValueError("El atributo seleccionado no existe")
    return diccionario_white, diccionario_red

#===========================================
#=============== REDUCE() ==================

def reduce(diccionario, atributo):
    lista_reduce = []
    for i in diccionario:
        if atributo in diccionario[i]:
            lista_reduce.append(diccionario[i][atributo])
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
        




