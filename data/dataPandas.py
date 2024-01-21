import pandas

# Importation du fichier csv et tri des colonnes:
consommation = pandas.read_csv(r"data/fichierDATA-CONSO.csv")
consommation_appareils_kWh = consommation[["Appareil suivi", "Consommation annuelle AN1"]]

# Création des moyennes de consommation de différents appareils:
consommation_audio_TV = consommation_appareils_kWh[consommation_appareils_kWh["Appareil suivi"] == "Audio_TV"]
moyenne_audioTV = round(consommation_audio_TV["Consommation annuelle AN1"].mean(), 2)

consommation_chauffage_electrique = consommation_appareils_kWh[
    consommation_appareils_kWh["Appareil suivi"] == "Chauffage electrique"]
moyenne_chauffage_electrique = round(consommation_chauffage_electrique["Consommation annuelle AN1"].mean(), 2)

consommation_eclairage = consommation_appareils_kWh[consommation_appareils_kWh["Appareil suivi"] == "Eclairage"]
moyenne_eclairage = round(consommation_appareils_kWh["Consommation annuelle AN1"].mean(), 2)

# Création d'une data frame avec les moyennes pour ensuite les mettre dans un fichier csv:
moyennes = pandas.DataFrame({"Audio TV": [moyenne_audioTV],
                             "chauffage_électrique": [moyenne_chauffage_electrique],
                             "éclairage": [moyenne_eclairage]})

moyennes.to_csv("moyennes.csv", index=False)

# Création d'une data frame avec toutes les valeurs de consommation à notre disposition pour ensuite les mettre dans un fichier csv:
consommation_totale = consommation_appareils_kWh["Consommation annuelle AN1"].tolist()
consommation_totale = [i for i in consommation_totale if
                       i < 10000]  # On enlève les valeurs trop élevées pour que les graphs de matplotlib soient plus lisibles
consommation_totale = pandas.DataFrame(consommation_totale, columns=["Consommation totale"])
consommation_totale = consommation_totale.dropna()
consommation_totale.to_csv("Consommation totale.csv", index=False)

# Création d'une data frame avec les valeurs de consommation des Televiseurs (un  des plus gros sets de données):
consommation_televiseurs = consommation_appareils_kWh[consommation_appareils_kWh["Appareil suivi"] == "Televiseurs"]
consommation_televiseurs = consommation_televiseurs["Consommation annuelle AN1"].tolist()
consommation_televiseurs = pandas.DataFrame(consommation_televiseurs, columns=["Consommation des téléviseurs"])
consommation_televiseurs = consommation_televiseurs.dropna()
consommation_televiseurs.to_csv("Consommation televiseurs.csv", index=False)

# Création d'un fichier csv qui réunni tous ceux créés précédemment:
toutes_les_df = pandas.concat([moyennes, consommation_totale, consommation_televiseurs], axis=1)
toutes_les_df.to_csv("Consommations.csv", index=False)
