# ANALYSE DES DONNÉES SIG - RÉSULTATS

## Jeu de données 1 : Évolution Cap Le Tréport (2000-2022)

### Caractéristiques générales :
- **693 événements d'érosion/éboulement** enregistrés
- **22 années de surveillance** (2000-2022) 
- **6 cellules d'analyse** côtières
- **18 variables** par événement

### Informations spatiales :
- **Coordonnées X** : 495 519 - 582 584 (système Lambert)  
- **Coordonnées Y** : 6 958 065 - 6 996 820 (système Lambert)
- **Zone d'étude** : Côte de Normandie (Cap Fécamp, St-Valéry-en-Caux/Dieppe, etc.)

### Variables clés identifiées :
1. **cell_6** : 6 cellules d'analyse (Cap_Fecamp, St-Val_Dieppe, etc.)
2. **annee_dig** : Années de numérisation (2000, 2008, 2012, 2015, 2019, 2022)
3. **eb_success** : Succès de l'éboulement (172 valeurs uniques)
4. **shape_area** : Surface affectée par événement
5. **shape_leng** : Longueur du front d'érosion
6. **auteur** : 8 équipes de recherche différentes

### Répartition par cellules :
- **St-Val_Dieppe** : 208 événements (30% du total)
- Les 5 autres cellules se répartissent le reste

---

## Jeu de données 2 : Cellules Hydrosédimentaires France

### Caractéristiques générales :
- **97 cellules hydrosédimentaires** en France métropolitaine
- **60 noms uniques** de cellules (certaines dupliquées)
- **2 types d'emprise** : "Emprise du projet" vs "Hors emprise"

### Variables :
1. **num_cell** : Numéros 0-99 (classification nationale)
2. **nom_cell** : Noms comme "Cap d'Antifer au Cap de la Hève"
3. **emprise** : 59 dans le projet, le reste hors projet
4. **territoire** : Toutes en France métropolitaine

### Exemples de cellules :
- Cap d'Antifer au Cap de la Hève
- Cap d'Antifer aux jetées du port de Fécamp  
- Lupino à l'embouchure du Golo

---

## INTERPRÉTATION SCIENTIFIQUE

### Jeu de données Cap Le Tréport :
- **Surveillance des falaises crayeuses** en Normandie
- **693 événements d'éboulement** = effondrements de falaises
- **Méthodologie multi-temporelle** : 6 campagnes sur 22 ans
- **Analyse par cellules** : permet des études comparatives
- **Variables morphométriques** : aire et périmètre de chaque événement

### Jeu de données Cellules Hydrosédimentaires :
- **Classification nationale française** du transport sédimentaire
- **Unités cohérentes** de transport de sédiments côtiers
- **Base pour la gestion côtière** et les études d'impact
- **Référence officielle** pour les études de vulnérabilité

---

## APPLICATIONS POSSIBLES

1. **Analyse temporelle** de l'érosion côtière (1995-2022 avec données météo)
2. **Corrélation** événements d'éboulement vs conditions météorologiques  
3. **Cartographie des risques** par cellule côtière
4. **Modélisation** du recul des falaises
5. **Comparaison inter-cellules** de vulnérabilité
6. **Gestion territoriale** et planification côtière

---

## FICHIERS GÉNÉRÉS
- `resumen_Evolución_Cap_Le_Tréport_2000-2022.csv`
- `resumen_Células_Hidrosedimentarias_Francia.csv`
- Cartes interactives et statiques
- Documentation complète

Les données sont prêtes pour des analyses plus approfondies avec QGIS ou Python !