# Ouvrir fichier csv
import pandas as pd 
df=pd.read_csv("flight_data_2018_to_2022.csv", sep=";" , low_memory=False )
# Choisir aléatoirement des lignes dans le df
df_min=df.sample(1000)
# afficher les valeurs Null
df_min.isna()
# visualiser le ratio des valeurs Null dans un csv
ratio_na=(df_min.isna().sum()/df_min.shape[0])
ratio_na.to_csv("ratio_na.csv")
# modifier le df avec uniquement les colonnes dont le ratio de valeurs null est < 0.5
columns_useful=ratio_na[ratio_na<0.5].index
df_min=df_min[columns_useful]
df_min.columns
df_min.shape
# créer un nouveau df
df=df[columns_useful]
# Créer un nouveau csv 
df.to_csv("fichier_final.csv")
