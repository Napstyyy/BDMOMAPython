# Guide de Visualisation des Fichiers SIG

## Qu'est-ce que les fichiers SIG_data ?

Les fichiers de ce dossier sont des données géospatiales au format **Shapefile** liées à :

1. **BD_eb_Cap_LeTrep_2000-2022** : Base de données d'évolution du bord côtier (éboulement/érosion) du Cap Le Tréport entre 2000-2022, divisée en 6 cellules d'analyse.

2. **N_cellule_hydrosedimentaire** : Données nationales françaises des cellules hydrosédimentaires (transport de sédiments côtiers) du Ministère de l'Environnement (MEDDE).

## Installation des outils

### Option 1 : Logiciel gratuit QGIS (Recommandé)
1. Télécharger QGIS depuis : https://qgis.org/
2. Installer en suivant les instructions
3. Ouvrir QGIS → Couche → Ajouter une couche → Ajouter une couche vectorielle
4. Sélectionner les fichiers .shp

### Option 2 : Python (Pour l'analyse programmatique)

```powershell
# Installer les dépendances
pip install geopandas matplotlib folium jupyter

# Pour l'analyse spatiale avancée (optionnel)
pip install pyproj shapely fiona
```

## Commandes pour exécuter les scripts

### Analyse basique des attributs :
```powershell
python examinar_atributos.py
```

### Visualisation complète :
```powershell
python visualizar_mejorado.py
```

## Structure des données

### Fichiers Shapefile (ensemble obligatoire) :
- `.shp` → Géométries (formes spatiales)
- `.dbf` → Table des attributs
- `.shx` → Index spatial
- `.prj` → Système de coordonnées
- `.cpg` → Codage du texte

### Informations sur les jeux de données :

**Cap Le Tréport (2000-2022)** :
- Évolution temporelle des falaises
- 6 cellules de surveillance
- Période : 22 années d'observation
- Zone : Côte de Normandie

**Cellules Hydrosédimentaires** :
- Classification nationale française
- Unités de transport sédimentaire
- Projection : Lambert 93 (EPSG:2154)
- Couverture : France métropolitaine

## Visualisation dans QGIS (étapes)

1. Ouvrir QGIS
2. Couche → Ajouter une couche → Ajouter une couche vectorielle
3. Naviguer vers le dossier SIG_data
4. Sélectionner le fichier .shp
5. Clic droit sur la couche → Propriétés
6. Onglet "Symbologie" pour changer les couleurs
7. Onglet "Étiquettes" pour afficher les attributs

## Analyses typiques possibles

- Évolution temporelle de l'érosion côtière
- Classification des types de cellules sédimentaires  
- Analyse de vulnérabilité côtière
- Cartographie des risques géomorphologiques
- Corrélation avec données météorologiques (Météo France)

## Serveur web local

Pour visualiser les cartes interactives :
```powershell
python -m http.server 8080
```
Puis ouvrir : http://localhost:8080/index.html