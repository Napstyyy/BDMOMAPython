"""
Script de réorganisation du projet selon les bonnes pratiques
Structure claire et professionnelle pour le projet IMT Atlantique
"""

import os
import shutil

def creer_structure_projet():
    """Créer la structure de dossiers selon les bonnes pratiques"""
    
    structure = {
        'docs/': 'Documentation du projet',
        'data/': 'Données sources et traitées',
        'data/raw/': 'Données brutes (SIG, Météo France)',
        'data/processed/': 'Données traitées et CSV générés',
        'scripts/': 'Scripts Python d\'analyse',
        'web/': 'Interface web et cartes interactives',
        'web/assets/': 'Images et ressources web',
        'web/maps/': 'Cartes interactives HTML',
        'outputs/': 'Résultats et visualisations finales',
        'outputs/images/': 'Cartes statiques PNG',
        'outputs/reports/': 'Rapports d\'analyse'
    }
    
    print("📁 CRÉATION DE LA STRUCTURE DE PROJET")
    print("="*50)
    
    for dossier, description in structure.items():
        if not os.path.exists(dossier):
            os.makedirs(dossier, exist_ok=True)
            print(f"✅ Créé : {dossier:<20} - {description}")
        else:
            print(f"ℹ️  Existe : {dossier:<20} - {description}")
    
    return structure

def organiser_fichiers():
    """Organiser les fichiers existants dans la nouvelle structure"""
    
    print(f"\n📦 ORGANISATION DES FICHIERS")
    print("="*50)
    
    # Mappings des fichiers vers leur nouvelle destination
    mappings = {
        # Documentation
        'docs/': [
            'README_FR.md',
            'RESUME_ANALYSE_SIG_FR.md',
            'GUIDE_VISUALISATION_SIG_FR.md',
            'RAPPORT_VERIFICATION_FRANCISATION.md'
        ],
        
        # Scripts Python
        'scripts/': [
            'examiner_attributs_FR.py',
            'visualiser_ameliore_FR.py',
            'creer_cartes_francaises.py',
            'nettoyage_final_FR.py',
            'nettoyer_fichiers_FR.py'
        ],
        
        # Données traitées
        'data/processed/': [
            'resume_Evolution_Cap_Le_Treport_2000-2022.csv',
            'resume_Cellules_Hydrosedimentaires_France.csv'
        ],
        
        # Interface web
        'web/': [
            'index.html'
        ],
        
        # Cartes interactives
        'web/maps/': [
            'carte_interactive_Cap_Le_Treport_FR.html',
            'carte_interactive_Cellules_Hydrosedimentaires_FR.html'
        ],
        
        # Images
        'outputs/images/': [
            'carte_Cap_Le_Treport.png',
            'carte_Cellules_Hydrosedimentaires.png',
            'comparaison_complete_jeux_donnees.png'
        ]
    }
    
    # Déplacer les fichiers
    for destination, fichiers in mappings.items():
        for fichier in fichiers:
            if os.path.exists(fichier):
                try:
                    nouveau_chemin = os.path.join(destination, fichier)
                    shutil.move(fichier, nouveau_chemin)
                    print(f"📁 {fichier:<40} → {destination}")
                except Exception as e:
                    print(f"❌ Erreur déplacement {fichier}: {e}")
            else:
                print(f"⚠️  Non trouvé: {fichier}")
    
    # Créer un lien symbolique pour SIG_data dans data/raw/
    if os.path.exists('SIG_data') and not os.path.exists('data/raw/SIG_data'):
        try:
            if os.name == 'nt':  # Windows
                # Sur Windows, on copie le dossier
                shutil.copytree('SIG_data', 'data/raw/SIG_data')
                print("📁 SIG_data copié vers data/raw/SIG_data")
            else:
                os.symlink('../../SIG_data', 'data/raw/SIG_data')
                print("📁 SIG_data lié vers data/raw/SIG_data")
        except Exception as e:
            print(f"⚠️  Impossible de lier SIG_data: {e}")

def creer_readme_principal():
    """Créer un README principal pour le projet organisé"""
    
    readme_contenu = """# 🗺️ Projet Analyse Géospatiale - IMT Atlantique

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

### 1. Lancement du serveur web
```powershell
# Se placer dans le dossier web
cd web
python -m http.server 8080
```

### 2. Accès à l'interface
Ouvrir : **http://localhost:8080/index.html**

### 3. Exécution des analyses
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
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_contenu)
    
    print("✅ README.md principal créé")

def mettre_a_jour_liens():
    """Mettre à jour les liens dans index.html pour la nouvelle structure"""
    
    index_path = 'web/index.html'
    
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            contenu = f.read()
        
        # Mise à jour des liens
        contenu = contenu.replace('carte_interactive_Cap_Le_Treport_FR.html', 'maps/carte_interactive_Cap_Le_Treport_FR.html')
        contenu = contenu.replace('carte_interactive_Cellules_Hydrosedimentaires_FR.html', 'maps/carte_interactive_Cellules_Hydrosedimentaires_FR.html')
        contenu = contenu.replace('carte_Cap_Le_Treport.png', '../outputs/images/carte_Cap_Le_Treport.png')
        contenu = contenu.replace('carte_Cellules_Hydrosedimentaires.png', '../outputs/images/carte_Cellules_Hydrosedimentaires.png')
        contenu = contenu.replace('comparaison_complete_jeux_donnees.png', '../outputs/images/comparaison_complete_jeux_donnees.png')
        contenu = contenu.replace('resume_Evolution_Cap_Le_Treport_2000-2022.csv', '../data/processed/resume_Evolution_Cap_Le_Treport_2000-2022.csv')
        contenu = contenu.replace('resume_Cellules_Hydrosedimentaires_France.csv', '../data/processed/resume_Cellules_Hydrosedimentaires_France.csv')
        contenu = contenu.replace('README_FR.md', '../docs/README_FR.md')
        contenu = contenu.replace('RESUME_ANALYSE_SIG_FR.md', '../docs/RESUME_ANALYSE_SIG_FR.md')
        contenu = contenu.replace('GUIDE_VISUALISATION_SIG_FR.md', '../docs/GUIDE_VISUALISATION_SIG_FR.md')
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(contenu)
        
        print("✅ Liens mis à jour dans web/index.html")

def creer_fichier_config():
    """Créer un fichier de configuration pour le projet"""
    
    config_contenu = """# Configuration du Projet - Évolution Côtière Normandie

## Paramètres des Données

### Shapefiles
- **Cap Le Tréport** : `data/raw/SIG_data/BD_eb_Cap_LeTrep_2000-2022/`
- **Cellules Hydro** : `data/raw/SIG_data/N_cellule_hydrosedimentaire_092020_MEDDE_geolitt/`

### Données Météo France
- **Station** : Dieppe (76217001)
- **Période** : 1995-2022
- **Format** : CSV horaire

## Projections Cartographiques

- **Source** : Lambert 93 (EPSG:2154)
- **Web** : WGS84 (EPSG:4326)

## Ports et Configuration

- **Serveur web** : Port 8080
- **URL locale** : http://localhost:8080/

## Dépendances Python

```
geopandas>=1.1.1
matplotlib>=3.10.6  
folium>=0.20.0
fiona>=1.10.1
pandas>=2.0.0
```

## Structure des Sorties

- **CSV** : `data/processed/`
- **Cartes PNG** : `outputs/images/`
- **Cartes HTML** : `web/maps/`
- **Documentation** : `docs/`
"""
    
    with open('CONFIG.md', 'w', encoding='utf-8') as f:
        f.write(config_contenu)
    
    print("✅ CONFIG.md créé")

def main():
    """Fonction principale de réorganisation"""
    
    print("🏗️  RÉORGANISATION DU PROJET SELON LES BONNES PRATIQUES")
    print("="*65)
    
    # 1. Créer la structure
    creer_structure_projet()
    
    # 2. Organiser les fichiers
    organiser_fichiers()
    
    # 3. Mettre à jour les liens
    mettre_a_jour_liens()
    
    # 4. Créer la documentation
    creer_readme_principal()
    creer_fichier_config()
    
    print(f"\n🎉 RÉORGANISATION TERMINÉE !")
    print("="*50)
    print("📁 Structure professionnelle créée")
    print("🔗 Liens mis à jour")
    print("📖 Documentation organisée")
    print("⚙️  Configuration définie")
    print(f"\n🌐 Pour tester : cd web && python -m http.server 8080")
    print("🌐 Puis ouvrir : http://localhost:8080/index.html")

if __name__ == "__main__":
    main()