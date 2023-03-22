import csv
#===========================================
#============= READ DATA() =================




def read_data(fichero):
    data = {}
    with open(fichero, "r") as f:
        reader = csv.reader(f)
        atributos = next(reader)
        for i, row in enumerate(reader):
            if row[0] != "":
                data["dato"+str(i+1)] = {}
                for j, atributo in enumerate(atributos):
                    data["dato"+str(i+1)][atributo] = row[j]
    return data


def split(data, atributo):
    white = {}
    red = {}
    for i in data:
        if atributo in data[i]:
            if data[i][atributo] == "white":
                white[i] = data[i]
                del white[i][atributo]
            elif data[i][atributo] == "red":
                red[i] = data[i]
                del red[i][atributo]
            else:
                raise ValueError("Este atributo no existe")
        else:
            raise ValueError("Este atributo no existe")
    return white, red


def reduce(data, atributo):
    lista = []
    for i in data:
        if atributo in data[i]:
            lista.append(data[i][atributo])
        else:
            raise ValueError("El atributo no existe")
    return lista





