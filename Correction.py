import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# • Importer le fichier Excel 

data= pd.read_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/cmportement_des_jeunes_vs_RS.xlsx")
print(data.head())
# • Supprimer les doublons et gérer les valeurs manquantes 
data.drop_duplicates(subset=[
        'Fréquence_notifications',
        'Stress_perçu',
        'Usage_soirée (min)',
        'Satisfaction_vie',
        'Heures_sommeil_moy',
        'Interactions_amis',
        'Nb_publications_semaine',
        'Temps_moyen_jour (min)'
    ],
    inplace=True
)
print(data["Âge"].min())
print(data["Âge"].max())
bornes = [15, 21, 25, 30]
etiquettes = ["16-21", "22-25", "26-30"]
data["Tranche_age"] = pd.cut(data["Âge"], bins=bornes, labels=etiquettes)
print(data.describe())
# • Moyenne, médiane, min, max du temps passé sur les réseaux par âge et sexe
stat_desc_age= data.groupby("Tranche_age")["Temps_moyen_jour (min)"].describe()
stat_desc_sexe= data.groupby("Sexe")["Temps_moyen_jour (min)"].describe()
print(f"temps_sur_réseau_par_age est :{stat_desc_age}")
# stat_desc_age.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/stat_desc_age.xlsx")

print(f"temps_sur_réseau_par_age est:{stat_desc_sexe}" )


# # • Plateformes les plus utilisées par tranche d’âge
reseaux= data.groupby("Tranche_age")["Plateforme_principale"].value_counts()
print(reseaux)
# reseaux.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/reseaux.xlsx")

# # print(data.dtypes)
# - division par tranche d'âge
bornes = [15, 21, 25, 30]
etiquettes = ["16-21", "22-25", "26-30"]
data["Tranche_age"] = pd.cut(data["Âge"], bins=bornes, labels=etiquettes)
# print(data.head())

# #- division par tranche d'heure de sommeil
bornes_heures_sommeil = [4, 4.9, 5.9, 6.9, 7.9, 8.9, 9.9, 10]
etiquettes_heure_sommeil = ["4h","5h", "6h", "7h", "8h", "9h", "10h"]
data["Heures_sommeil_moy_tranche"] = pd.cut(data["Heures_sommeil_moy"], bins=bornes_heures_sommeil, labels=etiquettes_heure_sommeil)

# #  Distribution des heures de sommeil 
Distribution_sommeil= data["Heures_sommeil_moy_tranche"].value_counts()
print(f" sommeil_par_sex est :{Distribution_sommeil }")
# Distribution_sommeil.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/Distribution_sommeil.xlsx")

# # Distribution du stress perçu
Distribution_stress= data["Stress_perçu"].value_counts()
print(f"stress_percu : {Distribution_stress}")

#- Analyse descriptive
description_globale = data.describe()
print(description_globale)
# description_globale.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/description_globale.xlsx")

#- temps moyen par jour par plateforme
temps_moyen_par_plateforme = data.groupby("Plateforme_principale")["Temps_moyen_jour (min)"].mean()
print(f"Temps moyen par plateforme: {temps_moyen_par_plateforme}")
# temps_moyen_par_plateforme.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/temps_moyen_par_plateforme.xlsx")


#- temps moyen par jour par pays
temps_moyen_par_pays = data.groupby("Pays")["Temps_moyen_jour (min)"].mean()
print(f"Temps moyen par pays: {temps_moyen_par_pays}")
#- temps moyen par jour par tranche age
temps_moyen_par_tranche_age = data.groupby("Tranche_age")["Temps_moyen_jour (min)"].mean()
print(f"Temps moyen par tranche age: {temps_moyen_par_tranche_age}")
# temps_moyen_par_tranche_age.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/temps_moyen_par_tranche_age.xlsx")

#- temps moyen par jour par sexe
temps_moyen_par_sexe = data.groupby("Sexe")["Temps_moyen_jour (min)"].mean()
print(f"Temps moyen par sexe: {temps_moyen_par_sexe}")
# temps_moyen_par_sexe.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/temps_moyen_par_sexe.xlsx")


#- Distribution des heures de sommeil et du stress perçu  
distribution_heures_sommeil = data["Heures_sommeil_moy_tranche"].value_counts()
print(distribution_heures_sommeil)

distribution_stresse_perçu = data["Stress_perçu"].value_counts()
print(distribution_stresse_perçu)
# distribution_stresse_perçu.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/distribution_stresse_perçu.xlsx")





# Analyse statistique
#- Corrélation entre temps passé sur réseaux et satisfaction
correlation_temps_rs_vs_satisfaction = data[["Temps_moyen_jour (min)", "Satisfaction_vie"]].corr()
print(f"correlation entre temps sur rs et satisfaction:{correlation_temps_rs_vs_satisfaction}")
# correlation_temps_rs_vs_satisfaction.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/correlation_temps_rs_vs_satisfaction.xlsx")

#- Test t pour comparer hommes vs femmes sur stress ou satisfaction 
comparaison_homme_femme_satisfaction = data.groupby("Sexe")["Satisfaction_vie"].describe()
print(comparaison_homme_femme_satisfaction)
# comparaison_homme_femme_satisfaction.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/comparaison_homme_femme_satisfaction.xlsx")

comparaison_homme_femme_stress = data.groupby("Sexe")["Stress_perçu"].describe()
print(comparaison_homme_femme_stress)
# comparaison_homme_femme_stress.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/comparaison_homme_femme_stress.xlsx")

#- Analyse par tranche d’âge 
comparaison_tranche_age_satisfaction = data.groupby("Tranche_age")["Satisfaction_vie"].describe()
print(comparaison_tranche_age_satisfaction)
# comparaison_tranche_age_satisfaction.to_excel ("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/comparaison_tranche_age_satisfaction.xlsx")


comparaison_tranche_age_stress = data.groupby("Tranche_age")["Stress_perçu"].describe()
print(comparaison_tranche_age_stress)
# comparaison_tranche_age_stress.to_excel ("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/comparaisoncomparaison_tranche_age_stress.xlsx")















#- Categories des personnes les plus touchées
#- Categories des personnes montrant une satisfaction plus grande
personnes_satisfaites = data[data["Satisfaction_vie"]>=7]
repartition_age_p_satisfaites= personnes_satisfaites["Tranche_age"].value_counts()
print(repartition_age_p_satisfaites)
# repartition_age_p_satisfaites.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/repartition_age_p_statisfaites.xlsx")

repartition_pays_p_satisfaites = personnes_satisfaites["Pays"].value_counts()
print(repartition_pays_p_satisfaites)
# repartition_pays_p_satisfaites.to_excel ("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/repartition_pays_p_satisfaites.xlsx")

repartition_sexe_p_satisfaites = personnes_satisfaites["Sexe"].value_counts()
print(repartition_sexe_p_satisfaites)
repartition_sexe_p_satisfaites.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/reparepartition_sexe_p_satisfaites.xlsx")

                                        

repartition_plateforme_p_satisfaites = personnes_satisfaites["Plateforme_principale"].value_counts()
print(repartition_plateforme_p_satisfaites)

temps_moyen_par_plateforme_p_satisfaites = personnes_satisfaites.groupby("Plateforme_principale")["Temps_moyen_jour (min)"].mean()
print(f"Temps moyen par plateforme chez les personnes satisfaites: {temps_moyen_par_plateforme_p_satisfaites}")
print()
print()


#- Categories des personnes montrant un niveau de stress plus grand
personnes_stressees = data[data["Stress_perçu"]>3]
repartition_age_p_stressees= personnes_stressees["Tranche_age"].value_counts()
repartition_pays_p_stressees = personnes_stressees["Pays"].value_counts()
repartition_sexe_p_stressees = personnes_stressees["Sexe"].value_counts()
repartition_plateforme_p_stressees = personnes_stressees["Plateforme_principale"].value_counts()
print(repartition_age_p_stressees)
print(repartition_pays_p_stressees)
print(repartition_sexe_p_stressees)
print(repartition_plateforme_p_stressees)
print()
print()

#- Comportement des personnes les plus touchées
#- Comportement des personnes les plus satisfaites
stats_descr_personnes_satisfaites = personnes_satisfaites[

    ["Temps_moyen_jour (min)",                   
      "Nb_publications_semaine",
     "Interactions_amis",                                       
     "Heures_sommeil_moy",
     "Usage_soirée (min)",
     "Fréquence_notifications"]
    
     ].describe()


print(stats_descr_personnes_satisfaites)
# stats_descr_personnes_satisfaites.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/stats_descr_personnes_satisfaites.xlsx")


#- Comportement des personnes les plus stressees
stats_descr_personnes_stressees = personnes_stressees[

 ["Temps_moyen_jour (min)",                                   
 "Nb_publications_semaine",
 "Interactions_amis",
 "Heures_sommeil_moy",
 "Usage_soirée (min)",
 "Fréquence_notifications"]
  
   ].describe()

print(stats_descr_personnes_stressees)
# stats_descr_personnes_stressees.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/stats_descr_personnes_stresses.xlsx")

correlation = data[
 ["Temps_moyen_jour (min)",
"Nb_publications_semaine",
 "Interactions_amis",
 "Heures_sommeil_moy",
 "Usage_soirée (min)",
"Fréquence_notifications",
 "Âge",
"Stress_perçu",
 "Satisfaction_vie"]
 ].corr()

print(correlation)
# correlation.to_excel("C:/Users/BonaventureADJAI/Downloads/Dossier eigb/Projet_Soutenance/correlation.xlsx")





#- Visualisations
#- Histogrammes du temps moyen par plateforme
plt.figure(figsize=(7, 6))
plt.bar(temps_moyen_par_plateforme.index, temps_moyen_par_plateforme.values, color="blue")
plt.xlabel("plateformes")
plt.ylabel("temps moyen par jour")
plt.title("Histogrammes du temps moyen par jour par plateforme")
plt.tight_layout()
plt.show()

#- Histogrammes du temps moyen par pays
plt.figure(figsize=(7, 6))
plt.bar(temps_moyen_par_pays.index, temps_moyen_par_pays.values, color="red")
plt.xlabel("Pays")
plt.ylabel("temps moyen par jour")
plt.title("Histogrammes du temps moyen par jour par pays")
plt.tight_layout()
plt.show()

#- Histogrammes du temps moyen par tranche d'âge
plt.figure(figsize=(7, 6))
plt.bar(temps_moyen_par_tranche_age.index, temps_moyen_par_tranche_age.values, color="green")
plt.xlabel("tranche age")
plt.ylabel("temps moyen par jour")
plt.title("Histogrammes du temps moyen par jour par tranche age")
plt.tight_layout()
plt.show()

#- Histogrammes du temps moyen par sexe
plt.figure(figsize=(7, 6))
plt.bar(temps_moyen_par_sexe.index, temps_moyen_par_sexe.values, color="yellow")
plt.xlabel("Sexe")
plt.ylabel("temps moyen par jour")
plt.title("Histogrammes du temps moyen par jour par Sexe")
plt.tight_layout()
plt.show()

#histrogramme répartion du stress
plt.figure(figsize=(7,6))
plt.bar(distribution_stresse_perçu.index, distribution_stresse_perçu.values, color="brown")
plt.xlabel("stress perçu")
plt.ylabel("population")
plt.title( "Distribution du stress")
plt.tight_layout()
plt.show()

#- Boxplots du niveau de stress par plateforme
plt.figure(figsize=(7, 6))
plt.boxplot(data["Stress_perçu"], )

plt.tight_layout()
plt.show()


#- Scatter plot : temps passé vs satisfaction vie, coloré par plateforme 
plt.figure(figsize=(7, 6))
plt.scatter(data["Temps_moyen_jour (min)"], data["Satisfaction_vie"], color="black")
plt.title("Nuages de points  temps passé vs satisfaction vie")
plt.tight_layout()
plt.show()

#- Heatmap des corrélations entre toutes les variables numériques 

plt.figure(figsize=(7, 6))
plt.imshow(correlation, cmap="Blues")
plt.colorbar(label="Barre des couleurs")
plt.xticks(np.arange(len(correlation.columns)), correlation.columns, rotation=90)
plt.yticks(np.arange(len(correlation.columns)), correlation.columns)
plt.tight_layout()
for i in range(len(correlation.columns)):
    for j in range(len(correlation.columns)):
        plt.text(i, j, f"{correlation.iloc[i, j]:.2f}", ha="center", va="center", color="white")
plt.show()
