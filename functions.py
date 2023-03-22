import csv
#===========================================
#============= READ DATA() =================

def read_data(nombrearchivo):
    data = {}
    with open(nombrearchivo, newline='') as csvfile:
        text = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in text:
            data[row[0]] = row[1]
    return data

def reduce(data, atributo):
    lista = []
    for i in data:
        if atributo in data[i]:
            lista.append(data[i][atributo])
        else:
            raise ValueError("El atributo no existe")
    return lista
