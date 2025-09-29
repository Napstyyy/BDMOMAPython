"""
Script de nettoyage pour supprimer les fichiers avec noms espagnols
et ne garder que les versions françaises
"""

import os

def nettoyer_fichiers():
    """Supprimer les anciens fichiers avec noms espagnols"""
    
    fichiers_a_supprimer = [
        # Cartes interactives espagnoles
        "mapa_interactivo_Cap_Le_Treport.html",
        "mapa_interactivo_Cellules_Hydrosedimentaires.html",
        
        # Images statiques espagnoles
        "mapa_Cap_Le_Treport.png",
        "mapa_Cellules_Hydrosedimentaires.png",
        "mapa_cap_letreport.html",
        "mapa_cellules_hydro.html",
        
        # Visualisations espagnoles
        "visualizacion_cap_letreport.png",
        "visualizacion_cellules_hydro.png",
        
        # Comparaisons espagnoles
        "comparacion_completa_datasets.png",
        "comparacion_datasets.png",
        
        # CSV espagnols
        "resumen_Células_Hidrosedimentarias_Francia.csv",
        "resumen_Evolución_Cap_Le_Tréport_2000-2022.csv",
        
        # Documentation espagnole
        "RESUMEN_ANALISIS_SIG.md",
        "GUIA_VISUALIZACION_SIG.md",
        
        # Scripts espagnols
        "examinar_atributos.py",
        "visualizar_shapefiles.py",
        "visualizar_mejorado.py"
    ]
    
    print("🧹 NETTOYAGE DES FICHIERS ESPAGNOLS")
    print("="*50)
    
    supprimes = 0
    non_trouves = 0
    
    for fichier in fichiers_a_supprimer:
        if os.path.exists(fichier):
            try:
                os.remove(fichier)
                print(f"✅ Supprimé : {fichier}")
                supprimes += 1
            except Exception as e:
                print(f"❌ Erreur suppression {fichier} : {e}")
        else:
            print(f"⚠️  Non trouvé : {fichier}")
            non_trouves += 1
    
    print(f"\n📊 RÉSUMÉ :")
    print(f"   - Fichiers supprimés : {supprimes}")
    print(f"   - Fichiers non trouvés : {non_trouves}")
    
    # Lister les fichiers français restants
    print(f"\n🇫🇷 FICHIERS FRANÇAIS CONSERVÉS :")
    fichiers_francais = [
        "carte_interactive_Cap_Le_Treport.html",
        "carte_interactive_Cellules_Hydrosedimentaires.html", 
        "carte_Cap_Le_Treport.png",
        "carte_Cellules_Hydrosedimentaires.png",
        "comparaison_complete_jeux_donnees.png",
        "resume_Evolution_Cap_Le_Treport_2000-2022.csv",
        "resume_Cellules_Hydrosedimentaires_France.csv",
        "RESUME_ANALYSE_SIG_FR.md",
        "GUIDE_VISUALISATION_SIG_FR.md",
        "examiner_attributs_FR.py",
        "visualiser_ameliore_FR.py",
        "index.html"
    ]
    
    for fichier in fichiers_francais:
        if os.path.exists(fichier):
            print(f"✅ {fichier}")
        else:
            print(f"❌ MANQUANT : {fichier}")

if __name__ == "__main__":
    nettoyer_fichiers()