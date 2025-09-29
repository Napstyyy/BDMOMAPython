# 🗺️ Projet Analyse Géospatiale - IMT Atlantique

## 📋 Vue d'Ensemble

Projet de **Commande Entreprise** portant sur l'analyse de l'évolution côtière en Normandie.
Combine données d'érosion de falaises, cellules hydrosédimentaires et observations météorologiques.

## 🏗️ Structure du Projet

```
📦 projet-evolution-cotiere/
├── 📁 docs/                          # Documentation complète
│   ├── README_FR.md                  # Guide détaillé du projet
│   ├── RESUME_ANALYSE_SIG_FR.md      # Analyse scientifique
│   ├── GUIDE_VISUALISATION_SIG_FR.md # Guide technique
│   └── RAPPORT_VERIFICATION_FRANCISATION.md
├── 📁 data/                          # Données du projet
│   ├── 📁 raw/                       # Données sources
│   │   ├── SIG_data/                 # Shapefiles (Cap Le Tréport, Cellules Hydro)
│   │   └── data_MeteoFrance_.../     # Données météorologiques (1995-2022)
│   └── 📁 processed/                 # Données traitées
│       ├── resume_Evolution_Cap_Le_Treport_2000-2022.csv
│       └── resume_Cellules_Hydrosedimentaires_France.csv
├── 📁 scripts/                       # Scripts d'analyse Python
│   ├── examiner_attributs_FR.py      # Analyse des attributs
│   ├── visualiser_ameliore_FR.py     # Génération des visualisations
│   ├── creer_cartes_francaises.py    # Création des cartes interactives
│   └── nettoyage_final_FR.py         # Scripts de maintenance
├── 📁 web/                           # Interface web
│   ├── index.html                    # Interface principale
│   └── 📁 maps/                      # Cartes interactives
│       ├── carte_interactive_Cap_Le_Treport_FR.html
│       └── carte_interactive_Cellules_Hydrosedimentaires_FR.html
└── 📁 outputs/                       # Résultats finaux
    └── 📁 images/                    # Cartes statiques
        ├── carte_Cap_Le_Treport.png
        ├── carte_Cellules_Hydrosedimentaires.png
        └── comparaison_complete_jeux_donnees.png
```

## 🚀 Démarrage Rapide

### Option 1: Script de démarrage interactif (Recommandé)
```powershell
python start.py
```
Ce script offre un menu interactif pour :
- 🌐 Lancer l'interface web automatiquement
- 📊 Exécuter les analyses de données
- 🗺️ Générer les cartes et visualisations
- 📁 Explorer la structure du projet

### Option 2: Démarrage manuel

#### 1. Installation des dépendances
```powershell
pip install -r requirements.txt
```

#### 2. Lancement du serveur web
```powershell
cd web
python -m http.server 8080
```

#### 3. Accès à l'interface
Ouvrir : **http://localhost:8080/index.html**

#### 4. Exécution des analyses
```powershell
# Analyse des données
python scripts/examiner_attributs_FR.py

# Génération des cartes
python scripts/visualiser_ameliore_FR.py
```

## 📊 Données Analysées

- **📍 Cap Le Tréport (2000-2022)** : 693 événements d'éboulement, 6 cellules de surveillance
- **🌊 Cellules Hydrosédimentaires** : 97 unités de transport sédimentaire (France)
- **🌤️ Météo France** : Observations horaires Dieppe (1995-2022)

## 🛠️ Technologies Utilisées

- **Python** : geopandas, matplotlib, folium
- **SIG** : Shapefiles, projections Lambert 93 / WGS84
- **Web** : HTML5, CSS3, Leaflet.js
- **Format** : CSV, PNG, HTML interactif

## 🎓 Contexte Académique

**Institution** : IMT Atlantique  
**Projet** : Commande Entreprise 2025  
**Domaine** : Géomorphologie côtière et risques littoraux  
**Zone** : Côte de Normandie (France)

---
*Projet entièrement francisé - Septembre 2025*
