"""
Script d'examen rapide des attributs de shapefiles en français
Nécessite seulement : pip install geopandas
"""

import geopandas as gpd
import pandas as pd

def examiner_attributs(chemin_shapefile, nom_dataset):
    """Examine les attributs d'un shapefile"""
    print(f"\n{'='*60}")
    print(f"ANALYSE DES ATTRIBUTS : {nom_dataset}")
    print(f"{'='*60}")
    
    try:
        # Lire seulement les attributs (sans géométrie pour être plus rapide)
        df = gpd.read_file(chemin_shapefile).drop('geometry', axis=1)
        
        print(f"\nDimensions du jeu de données : {df.shape[0]} lignes × {df.shape[1]} colonnes")
        
        print(f"\nColonnes disponibles :")
        for i, col in enumerate(df.columns, 1):
            dtype = df[col].dtype
            print(f"  {i:2d}. {col:<30} ({dtype})")
        
        print(f"\nInformation statistique :")
        print(df.describe(include='all'))
        
        print(f"\nPremiers 5 enregistrements :")
        print(df.head())
        
        print(f"\nValeurs uniques par colonne (10 premières colonnes) :")
        for col in df.columns[:10]:
            n_unique = df[col].nunique()
            print(f"  {col}: {n_unique} valeurs uniques")
            if n_unique <= 10:
                print(f"    Valeurs : {list(df[col].unique())}")
        
        return df
        
    except Exception as e:
        print(f"Erreur lors du traitement de {nom_dataset} : {e}")
        return None

# Chemins vers les fichiers
datasets = {
    "Évolution Cap Le Tréport (2000-2022)": r"SIG_data\BD_eb_Cap_LeTrep_2000-2022\BD_eb_cap_LeTrep_2000-2022_6cellules.shp",
    "Cellules Hydrosédimentaires France": r"SIG_data\N_cellule_hydrosedimentaire_092020_MEDDE_geolitt\N_cellule_hydrosedimentaire_L_metropole_epsg2154_092020.shp"
}

print("ANALYSE RAPIDE DES SHAPEFILES")
print("Examen des attributs sans charger les géométries...")

for nom, chemin in datasets.items():
    df = examiner_attributs(chemin, nom)
    
    if df is not None:
        # Sauvegarder le résumé en CSV pour révision ultérieure
        fichier_resume = f"resume_{nom.replace(' ', '_').replace('(', '').replace(')', '')}.csv"
        df.head(100).to_csv(fichier_resume, index=False, encoding='utf-8')
        print(f"Résumé sauvegardé dans : {fichier_resume}")