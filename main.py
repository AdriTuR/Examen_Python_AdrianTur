#===========================================
#================== IMPORTS ================
import functions
#===========================================
#================= MAIN ===================

#read_data()
ruta = ".\Examen_Python_AdrianTur\winequality.csv"
data = functions.read_data(ruta)

#split()
dictwhite = {}
dictred = {}
dictwhite, dictred = functions.split(data, "type")

#reduce()
lista_alcohol = []
lista_density = []
lista_alcohol = functions.reduce(data, "alcohol")
lista_density = functions.reduce(data, "density")
