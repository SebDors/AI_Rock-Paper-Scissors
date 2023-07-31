from sklearn.neighbors import KNeighborsClassifier
import openpyxl
import numpy as np

#Wich ai model are we using
model = KNeighborsClassifier()

Classeur = openpyxl.load_workbook("Projet-PFC/ResultatParties.xlsx")
Feuille = Classeur.active

donnees_excel = []
for ligne in Feuille.iter_rows(values_only=True):
    donnees_excel.append(list(ligne))
    tableau_numpy = np.array(donnees_excel)


tableau_numpy = np.delete(tableau_numpy,[0,1,2],0)
print(tableau_numpy)