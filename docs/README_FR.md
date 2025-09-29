# 🗺️ Visualisation des Données SIG - Projet Commande Entreprise

## 📋 Description du Projet

Ce projet d'analyse géospatiale porte sur l'évolution côtière en Normandie dans le cadre du **Projet Commande Entreprise** de l'**IMT Atlantique**. Il combine des données d'érosion de falaises et des classifications nationales de transport sédimentaire pour analyser la vulnérabilité côtière.

## 🗂️ Structure des Données

### Jeux de Données Analysés

1. **Cap Le Tréport (2000-2022)**
   - 693 événements d'éboulement de falaises
   - 6 cellules de surveillance côtière
   - 22 années de données temporelles
   - Variables morphométriques (surface, périmètre)

2. **Cellules Hydrosédimentaires France**
   - 97 unités de transport sédimentaire
   - Classification nationale MEDDE
   - Couverture France métropolitaine

3. **Données Météo France (1995-2022)**
   - Observations horaires station Dieppe
   - 28 années de données météorologiques
   - Corrélation possible avec événements d'érosion

## 🖥️ Interface de Visualisation

### Fichiers Principaux
- **`index.html`** - Interface web principale
- **`carte_interactive_Cap_Le_Treport.html`** - Carte interactive des éboulements
- **`carte_interactive_Cellules_Hydrosedimentaires.html`** - Carte des cellules sédimentaires

### Images Statiques
- **`carte_Cap_Le_Treport.png`** - Vue d'ensemble des éboulements
- **`carte_Cellules_Hydrosedimentaires.png`** - Classification nationale
- **`comparaison_complete_jeux_donnees.png`** - Superposition comparative

## 📊 Données Exportées

### Fichiers CSV
- **`resume_Evolution_Cap_Le_Treport_2000-2022.csv`** - Données tabulaires éboulements
- **`resume_Cellules_Hydrosedimentaires_France.csv`** - Attributs cellules sédimentaires

### Documentation
- **`RESUME_ANALYSE_SIG_FR.md`** - Analyse scientifique complète
- **`GUIDE_VISUALISATION_SIG_FR.md`** - Guide technique d'utilisation

## 🛠️ Outils et Scripts

### Scripts Python
- **`examiner_attributs_FR.py`** - Analyse rapide des attributs
- **`visualiser_ameliore_FR.py`** - Génération complète des visualisations
- **`nettoyer_fichiers_FR.py`** - Nettoyage des fichiers temporaires

### Dépendances Techniques
```python
geopandas>=1.1.1
matplotlib>=3.10.6
folium>=0.20.0
fiona>=1.10.1
```

## 🌐 Démarrage Rapide

### 1. Lancement du Serveur Web
```powershell
python -m http.server 8080
```

### 2. Accès à l'Interface
Ouvrir dans un navigateur : **http://localhost:8080/index.html**

### 3. Analyse des Données
```powershell
python examiner_attributs_FR.py
```

### 4. Génération des Cartes
```powershell
python visualiser_ameliore_FR.py
```

## 📈 Applications Scientifiques

### Analyses Possibles
1. **Corrélation temporelle** : Éboulements vs conditions météorologiques
2. **Analyse spatiale** : Vulnérabilité par cellule côtière  
3. **Modélisation prédictive** : Évolution future des falaises
4. **Gestion des risques** : Cartographie des zones sensibles

### Méthodologie
- **Approche multi-temporelle** : 6 campagnes sur 22 ans
- **Analyse par cellules** : Comparaisons inter-sites
- **Variables morphométriques** : Quantification des processus
- **Classification nationale** : Contextualisation sédimentaire

## 🎓 Contexte Académique

**Institution** : IMT Atlantique  
**Projet** : Commande Entreprise  
**Domaine** : Géomorphologie côtière et risques littoraux  
**Période** : 2025  
**Zone d'étude** : Côte de Normandie (France)

## 📞 Sources de Données

- **Météo France** : Observations météorologiques (1995-2022)
- **MEDDE** : Classification cellules hydrosédimentaires
- **Recherche Littorale** : Base de données éboulements Cap Le Tréport

---

*Dernière mise à jour : Septembre 2025*  
*Interface entièrement en français - Projet IMT Atlantique*