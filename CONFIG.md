# Configuration du Projet - Évolution Côtière Normandie

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
