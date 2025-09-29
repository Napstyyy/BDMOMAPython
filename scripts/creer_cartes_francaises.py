"""
Script pour créer des cartes interactives entièrement en français
Tous les éléments (titres, tooltips, contrôles) seront en français
"""

import geopandas as gpd
import folium
import os

def creer_carte_francaise_cap_treport():
    """Créer une carte interactive entièrement française pour Cap Le Tréport"""
    print("🇫🇷 Création de la carte française Cap Le Tréport...")
    
    try:
        # Charger les données
        chemin = r'SIG_data\BD_eb_Cap_LeTrep_2000-2022\BD_eb_cap_LeTrep_2000-2022_6cellules.shp'
        gdf = gpd.read_file(chemin)
        
        # Reprojeter en WGS84
        gdf_wgs84 = gdf.to_crs('EPSG:4326')
        
        # Calculer le centre
        bounds = gdf_wgs84.total_bounds
        centre_lat = (bounds[1] + bounds[3]) / 2
        centre_lon = (bounds[0] + bounds[2]) / 2
        
        # Créer la carte avec titre français
        m = folium.Map(
            location=[centre_lat, centre_lon],
            zoom_start=11,
            tiles=None  # Nous ajouterons les tuiles manuellement
        )
        
        # Ajouter la couche OpenStreetMap avec nom français
        folium.TileLayer(
            tiles='OpenStreetMap',
            name='Carte Routière',
            overlay=False,
            control=True
        ).add_to(m)
        
        # Ajouter la couche satellite avec nom français
        folium.TileLayer(
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr='Esri',
            name='Vue Satellite',
            overlay=False,
            control=True
        ).add_to(m)
        
        # Fonction de style française
        def style_francais(feature):
            return {
                'fillColor': 'blue',
                'color': 'navy',
                'weight': 1.5,
                'fillOpacity': 0.7,
                'opacity': 0.9
            }
        
        # Préparer les données pour les tooltips français
        gdf_fr = gdf_wgs84.copy()
        
        # Traduire les noms de colonnes pour l'affichage
        colonnes_francaises = {
            'cell_6': 'Cellule',
            'annee_dig': 'Année Digitalisation',
            'shape_area': 'Surface (m²)',
            'shape_leng': 'Périmètre (m)',
            'auteur': 'Auteur',
            'eb_success': 'Succès Éboulement'
        }
        
        # Ajouter les données avec tooltips français
        folium.GeoJson(
            gdf_fr,
            style_function=style_francais,
            tooltip=folium.features.GeoJsonTooltip(
                fields=['cell_6', 'annee_dig', 'shape_area', 'shape_leng', 'auteur'],
                aliases=['🏖️ Cellule:', '📅 Année:', '📐 Surface (m²):', '📏 Périmètre (m):', '👤 Auteur:'],
                labels=True,
                sticky=True,
                opacity=0.9,
                direction='right',
                style="""
                    background-color: white;
                    border: 2px solid navy;
                    border-radius: 3px;
                    box-shadow: 3px;
                """
            ),
            popup=folium.features.GeoJsonPopup(
                fields=['cell_6', 'annee_dig', 'shape_area', 'eb_success'],
                aliases=['Cellule de Surveillance', 'Année de Digitalisation', 'Surface Affectée (m²)', 'Type d\'Éboulement'],
                labels=True,
                style="font-size: 12px;"
            )
        ).add_to(m)
        
        # Ajouter le contrôle des couches avec noms français
        folium.LayerControl(
            position='topright',
            collapsed=False
        ).add_to(m)
        
        # Ajouter un titre français à la carte
        titre_html = '''
        <div style="position: fixed; 
                    top: 10px; left: 50px; width: 300px; height: 60px; 
                    background-color:white; border:2px solid navy; z-index:9999; 
                    font-size:14px; font-weight: bold; padding: 10px; border-radius: 5px;
                    ">
        <h4 style="margin: 0; color: navy;">🌊 Évolution Côtière Cap Le Tréport</h4>
        <p style="margin: 5px 0 0 0; font-size: 11px;">693 événements d'éboulement (2000-2022)</p>
        </div>
        '''
        m.get_root().html.add_child(folium.Element(titre_html))
        
        # Ajouter une légende française
        legende_html = '''
        <div style="position: fixed; 
                    bottom: 50px; left: 50px; width: 200px; height: 80px; 
                    background-color:white; border:2px solid navy; z-index:9999; 
                    font-size:12px; padding: 10px; border-radius: 5px;
                    ">
        <h5 style="margin: 0; color: navy;">📍 Légende</h5>
        <p style="margin: 5px 0;"><span style="color: blue;">■</span> Zones d'éboulement</p>
        <p style="margin: 5px 0; font-size: 10px;"><i>Survoler pour plus d'infos</i></p>
        </div>
        '''
        m.get_root().html.add_child(folium.Element(legende_html))
        
        # Sauvegarder
        m.save('carte_interactive_Cap_Le_Treport_FR.html')
        print("✅ Carte française Cap Le Tréport créée : carte_interactive_Cap_Le_Treport_FR.html")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la création de la carte Cap Le Tréport : {e}")
        return False

def creer_carte_francaise_cellules_hydro():
    """Créer une carte interactive entièrement française pour les cellules hydrosédimentaires"""
    print("🇫🇷 Création de la carte française Cellules Hydrosédimentaires...")
    
    try:
        # Charger les données
        chemin = r'SIG_data\N_cellule_hydrosedimentaire_092020_MEDDE_geolitt\N_cellule_hydrosedimentaire_L_metropole_epsg2154_092020.shp'
        gdf = gpd.read_file(chemin)
        
        # Reprojeter en WGS84
        gdf_wgs84 = gdf.to_crs('EPSG:4326')
        
        # Calculer le centre (France métropolitaine)
        centre_lat = 46.5
        centre_lon = 2.5
        
        # Créer la carte
        m = folium.Map(
            location=[centre_lat, centre_lon],
            zoom_start=6,
            tiles=None
        )
        
        # Ajouter les couches de base avec noms français
        folium.TileLayer(
            tiles='OpenStreetMap',
            name='Carte Routière',
            overlay=False,
            control=True
        ).add_to(m)
        
        folium.TileLayer(
            tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr='Esri',
            name='Vue Satellite',
            overlay=False,
            control=True
        ).add_to(m)
        
        # Style français pour les cellules
        def style_cellules(feature):
            return {
                'color': 'red',
                'weight': 2,
                'opacity': 0.8,
                'fillColor': 'pink',
                'fillOpacity': 0.3
            }
        
        # Ajouter les données avec tooltips français
        folium.GeoJson(
            gdf_wgs84,
            style_function=style_cellules,
            tooltip=folium.features.GeoJsonTooltip(
                fields=['nom_cell', 'num_cell', 'emprise', 'territoire'],
                aliases=['🏖️ Nom Cellule:', '📊 Numéro:', '📍 Emprise:', '🗺️ Territoire:'],
                labels=True,
                sticky=True,
                opacity=0.9,
                direction='right',
                style="""
                    background-color: white;
                    border: 2px solid red;
                    border-radius: 3px;
                    box-shadow: 3px;
                """
            ),
            popup=folium.features.GeoJsonPopup(
                fields=['nom_cell', 'num_cell', 'emprise'],
                aliases=['Nom de la Cellule', 'Numéro de Cellule', 'Type d\'Emprise'],
                labels=True,
                style="font-size: 12px;"
            )
        ).add_to(m)
        
        # Contrôle des couches
        folium.LayerControl(
            position='topright',
            collapsed=False
        ).add_to(m)
        
        # Titre français
        titre_html = '''
        <div style="position: fixed; 
                    top: 10px; left: 50px; width: 350px; height: 60px; 
                    background-color:white; border:2px solid red; z-index:9999; 
                    font-size:14px; font-weight: bold; padding: 10px; border-radius: 5px;
                    ">
        <h4 style="margin: 0; color: red;">🏖️ Cellules Hydrosédimentaires France</h4>
        <p style="margin: 5px 0 0 0; font-size: 11px;">97 unités de transport sédimentaire côtier</p>
        </div>
        '''
        m.get_root().html.add_child(folium.Element(titre_html))
        
        # Légende française
        legende_html = '''
        <div style="position: fixed; 
                    bottom: 50px; left: 50px; width: 250px; height: 90px; 
                    background-color:white; border:2px solid red; z-index:9999; 
                    font-size:12px; padding: 10px; border-radius: 5px;
                    ">
        <h5 style="margin: 0; color: red;">📍 Légende</h5>
        <p style="margin: 5px 0;"><span style="color: red;">—</span> Cellules hydrosédimentaires</p>
        <p style="margin: 5px 0; font-size: 10px;"><i>Classification MEDDE officielle</i></p>
        <p style="margin: 5px 0; font-size: 10px;"><i>Survoler pour détails</i></p>
        </div>
        '''
        m.get_root().html.add_child(folium.Element(legende_html))
        
        # Sauvegarder
        m.save('carte_interactive_Cellules_Hydrosedimentaires_FR.html')
        print("✅ Carte française Cellules Hydro créée : carte_interactive_Cellules_Hydrosedimentaires_FR.html")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la création de la carte Cellules Hydro : {e}")
        return False

def main():
    """Fonction principale pour créer toutes les cartes françaises"""
    print("🇫🇷 CRÉATION DE CARTES INTERACTIVES ENTIÈREMENT FRANÇAISES")
    print("="*60)
    
    # Créer les cartes françaises
    succes_cap = creer_carte_francaise_cap_treport()
    succes_cellules = creer_carte_francaise_cellules_hydro()
    
    if succes_cap and succes_cellules:
        print(f"\n✅ SUCCÈS : Toutes les cartes françaises ont été créées !")
        print("📁 Fichiers générés :")
        print("   - carte_interactive_Cap_Le_Treport_FR.html")
        print("   - carte_interactive_Cellules_Hydrosedimentaires_FR.html")
        print(f"\n🌐 Accès : http://localhost:8080/")
    else:
        print(f"\n❌ Erreur lors de la création de certaines cartes")

if __name__ == "__main__":
    main()