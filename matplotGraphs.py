import matplotlib.pyplot as plt

from data.dataPandas import moyennes, consommation_televiseurs, consommation_totale

# --------------------------- Figure 1 : Les téléviseurs :

# Subplots permet de créer différents graphique dans un tableau ex: (1, 2) -> découpe la scène en 1 de largeur et 2 de longueur.
figureTeleviseurs, axes = plt.subplots(1, 2)

# Permet de mettre la figure à la bonne largeur.
figureTeleviseurs.set_figwidth(11)

# Permet de mettre un titre à la fonction.
figureTeleviseurs.suptitle("Consommation Electrique des Téléviseurs dans les Foyers")

# Je distingue tous les graphiques
scatterData = axes[0]
boxPlotData = axes[1]

# Impératif d'avoir le même nombre d'entrées pour l'axe des abscisses que pour l'axe des ordonnés.
# L'argument marker désigne le symbole utilisé pour dessiner les points.
scatterData.scatter([x for x in range(len(consommation_televiseurs))],
                    consommation_televiseurs["Consommation des téléviseurs"], marker=".", color="k")

# Je nomme l'axe des abscisses et l'axe des ordonnés.
scatterData.set_xlabel("Nombre de Foyers")
scatterData.set_ylabel("Consommation Electrique - kW/h")

# L'argument sym est spécifique aux valeurs extrêmes.
boxPlotData.boxplot(x=consommation_televiseurs["Consommation des téléviseurs"], sym="k.")
boxPlotData.set_xlabel("Téléviseurs")
boxPlotData.set_ylabel("Consommation Electrique - kW/h")

# --------------------------- Figure 2 : Comparaison d'Appareils :

# Je n'ai cette fois ci pas besoin de plusieurs graphiques.
figureComparaison = plt.figure()
figureComparaison.suptitle("Comparaison d'Appareils Electroniques en fonction de la Consommation")
axes = figureComparaison.add_subplot()
axes.bar("Audio TV", moyennes["Audio TV"])
axes.bar("Eclairage", moyennes["éclairage"])
axes.bar("Chauffage Electrique", moyennes["chauffage_électrique"])
axes.set_xlabel("Appareils")
axes.set_ylabel("Consommation Electrique - kW/h")

# --------------------------- Figure 3 : Consommation Totale :

figureConsommation, axes = plt.subplots(2, 1)

# Je change cette fois ci la hauteur du graphique.
figureConsommation.set_figheight(7)

figureConsommation.suptitle("Consommation Totale des Différents Appareils dans les Foyers")
boxPlot_With_OutliersData = axes[0]
boxPlot_Without_OutliersData = axes[1]

# L'argument vert désigne l'inclinison du graphique en boîte à moustache. Ici je le mets horizontalement.
# De plus, quand sym est atttribué à aucune valeur, les valeurs extrêmes ne sont pas prises en compte.
boxPlot_Without_OutliersData.boxplot(x=consommation_totale["Consommation totale"], vert=False, sym="")

boxPlot_Without_OutliersData.set_xlabel("Consommation Electrique")
boxPlot_Without_OutliersData.set_ylabel("Appareils")

boxPlot_With_OutliersData.boxplot(x=consommation_totale["Consommation totale"], vert=False, sym="k.")
boxPlot_With_OutliersData.set_xlabel("Consommation Electrique")
boxPlot_With_OutliersData.set_ylabel("Appareils")

# Affiche l'ensemble des figures et des graphiques.
# plt.show()
