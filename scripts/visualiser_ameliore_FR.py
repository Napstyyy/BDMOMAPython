"""
Script français amélioré pour visualiser les shapefiles SIG
"""

import geopandas as gpd
import matplotlib
matplotlib.use('Agg')  # Backend sans fenêtre pour générer des fichiers
import matplotlib.pyplot as plt
import folium
import os
import warnings
warnings.filterwarnings('ignore')

def creer_visualisation_matplotlib(gdf, nom, couleur='blue'):
    """Créer une visualisation statique avec matplotlib"""
    try:
        print(f"Création de la visualisation matplotlib pour {nom}...")
        
        fig, ax = plt.subplots(1, 1, figsize=(15, 10))
        
        # Plot principal
        gdf.plot(ax=ax, color=couleur, alpha=0.7, edgecolor='black', linewidth=0.5)
        
        ax.set_title(f'Carte de {nom}', fontsize=16, pad=20)
        ax.set_xlabel('Coordonnée X (Lambert 93)', fontsize=12)
        ax.set_ylabel('Coordonnée Y (Lambert 93)', fontsize=12)
        
        # Ajouter une grille
        ax.grid(True, alpha=0.3)
        
        # Ajuster la mise en page
        plt.tight_layout()
        
        # Sauvegarder le fichier
        nom_fichier = f'carte_{nom.replace(" ", "_")}.png'
        plt.savefig(nom_fichier, dpi=300, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        plt.close()
        
        print(f"✅ Carte sauvegardée : {nom_fichier}")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la création de la visualisation matplotlib : {e}")
        return False

def creer_carte_folium(gdf, nom, couleur='blue'):
    """Créer une carte interactive avec Folium"""
    try:
        print(f"Création de la carte interactive pour {nom}...")
        
        # Reprojeter en WGS84
        gdf_wgs84 = gdf.to_crs('EPSG:4326')
        
        # Calculer le centre
        bounds = gdf_wgs84.total_bounds
        centre_lat = (bounds[1] + bounds[3]) / 2
        centre_lon = (bounds[0] + bounds[2]) / 2
        
        # Créer la carte
        m = folium.Map(
            location=[centre_lat, centre_lon],
            zoom_start=11,
            tiles='OpenStreetMap'
        )
        
        # Ajouter une couche de base alternative
        folium.TileLayer(
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr='Esri',
            name='Satellite',
            overlay=False,
            control=True
        ).add_to(m)
        
        # Fonction de style
        def fonction_style(feature):
            return {
                'fillColor': couleur,
                'color': 'black',
                'weight': 1,
                'fillOpacity': 0.6
            }
        
        # Ajouter les données
        folium.GeoJson(
            gdf_wgs84,
            style_function=fonction_style,
            tooltip=folium.features.GeoJsonTooltip(
                fields=['cell_6', 'annee_dig', 'shape_area'] if 'cell_6' in gdf_wgs84.columns else ['nom_cell', 'num_cell'],
                labels=True,
                sticky=True,
                opacity=0.9,
                direction='right'
            )
        ).add_to(m)
        
        # Contrôle des couches
        folium.LayerControl().add_to(m)
        
        # Sauvegarder
        nom_fichier = f'carte_interactive_{nom.replace(" ", "_")}.html'
        m.save(nom_fichier)
        
        print(f"✅ Carte interactive sauvegardée : {nom_fichier}")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la création de la carte Folium : {e}")
        return False

def analyser_jeu_donnees(chemin, nom):
    """Analyser un jeu de données complet"""
    print(f"\n{'='*60}")
    print(f"TRAITEMENT : {nom}")
    print(f"{'='*60}")
    
    try:
        # Charger le shapefile
        gdf = gpd.read_file(chemin)
        print(f"✅ Shapefile chargé avec succès")
        print(f"   - {len(gdf)} caractéristiques")
        print(f"   - SCR : {gdf.crs}")
        print(f"   - Type : {gdf.geometry.geom_type.iloc[0] if len(gdf) > 0 else 'Sans données'}")
        
        # Information d'étendue
        bounds = gdf.total_bounds
        print(f"   - Étendue : X[{bounds[0]:.0f}, {bounds[2]:.0f}] Y[{bounds[1]:.0f}, {bounds[3]:.0f}]")
        
        # Créer les visualisations
        couleur = 'blue' if 'cap' in nom.lower() else 'red'
        
        # Matplotlib
        creer_visualisation_matplotlib(gdf, nom, couleur)
        
        # Folium
        creer_carte_folium(gdf, nom, couleur)
        
        return gdf
        
    except Exception as e:
        print(f"❌ Erreur lors du traitement de {nom} : {e}")
        return None

def creer_carte_comparative(gdf1, gdf2, nom1, nom2):
    """Créer une carte comparative des deux jeux de données"""
    try:
        print(f"\n{'='*60}")
        print("CRÉATION DE LA CARTE COMPARATIVE")
        print(f"{'='*60}")
        
        fig, ax = plt.subplots(1, 1, figsize=(18, 12))
        
        # Reprojeter au même système si nécessaire
        if gdf1.crs != gdf2.crs:
            gdf2_proj = gdf2.to_crs(gdf1.crs)
        else:
            gdf2_proj = gdf2
        
        # Tracer les deux jeux de données
        gdf1.plot(ax=ax, color='blue', alpha=0.6, edgecolor='navy', 
                 linewidth=0.5, label=nom1)
        gdf2_proj.plot(ax=ax, color='red', alpha=0.6, edgecolor='darkred', 
                      linewidth=0.5, label=nom2)
        
        ax.set_title('Comparaison des Jeux de Données Géospatiaux', fontsize=18, pad=20)
        ax.set_xlabel('Coordonnée X (Lambert 93)', fontsize=14)
        ax.set_ylabel('Coordonnée Y (Lambert 93)', fontsize=14)
        ax.legend(fontsize=12)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('comparaison_complete_jeux_donnees.png', dpi=300, bbox_inches='tight',
                   facecolor='white', edgecolor='none')
        plt.close()
        
        print("✅ Carte comparative sauvegardée : comparaison_complete_jeux_donnees.png")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la création de la carte comparative : {e}")
        return False

def main():
    """Fonction principale améliorée"""
    print("🗺️  ANALYSE ET VISUALISATION DES DONNÉES SIG")
    print("="*60)
    
    # Configuration des jeux de données
    jeux_donnees = {
        'Cap Le Treport': r'SIG_data\BD_eb_Cap_LeTrep_2000-2022\BD_eb_cap_LeTrep_2000-2022_6cellules.shp',
        'Cellules Hydrosedimentaires': r'SIG_data\N_cellule_hydrosedimentaire_092020_MEDDE_geolitt\N_cellule_hydrosedimentaire_L_metropole_epsg2154_092020.shp'
    }
    
    # Vérifier les fichiers
    fichiers_disponibles = {}
    for nom, chemin in jeux_donnees.items():
        if os.path.exists(chemin):
            fichiers_disponibles[nom] = chemin
            print(f"✅ Trouvé : {chemin}")
        else:
            print(f"❌ Non trouvé : {chemin}")
    
    if not fichiers_disponibles:
        print("❌ Aucun fichier shapefile trouvé")
        return
    
    # Traiter chaque jeu de données
    gdfs = {}
    for nom, chemin in fichiers_disponibles.items():
        gdf = analyser_jeu_donnees(chemin, nom)
        if gdf is not None:
            gdfs[nom] = gdf
    
    # Créer une carte comparative si plusieurs jeux de données
    if len(gdfs) >= 2:
        noms = list(gdfs.keys())
        creer_carte_comparative(gdfs[noms[0]], gdfs[noms[1]], noms[0], noms[1])
    
    # Résumé final
    print(f"\n{'='*60}")
    print("RÉSUMÉ DES FICHIERS GÉNÉRÉS")
    print(f"{'='*60}")
    
    fichiers_generes = []
    for fichier in os.listdir('.'):
        if fichier.endswith(('.png', '.html')) and ('carte' in fichier or 'comparaison' in fichier):
            fichiers_generes.append(fichier)
            print(f"📁 {fichier}")
    
    if fichiers_generes:
        print(f"\n✅ Total : {len(fichiers_generes)} fichiers de visualisation générés")
        print("\n💡 Pour voir les cartes :")
        print("   - Fichiers PNG : ouvrir avec un visualiseur d'images")
        print("   - Fichiers HTML : ouvrir dans un navigateur web")
    else:
        print("\n⚠️  Aucun fichier de visualisation généré")

if __name__ == "__main__":
    main()