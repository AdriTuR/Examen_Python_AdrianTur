#===========================================
#================== IMPORTS ================
import functions
#===========================================
#================= MAIN ===================

#read_data()
ruta = ".\Examen_Python_AdrianTur\winequality.csv"
try:
    data = functions.read_data(ruta)
except ValueError as e:
    print("Ha ocurrido la excepcion", e)


#split()
try:
    diccionario_white, diccionario_red = functions.split(data, "type")
except ValueError as e:
    print("Ha ocurrido la excepcion", e)


#reduce()
try:
    lista_alcohol = functions.reduce(data, "alcohol")
    lista_density = functions.reduce(data, "density")
except ValueError as e:
    print("Ha ocurrido la excepcion", e)


#silhouette()
try:
    silhouette = functions.silhouette(lista_alcohol, lista_density)
except ValueError as e:
    print("Ha ocurrido la excepcion", e)



