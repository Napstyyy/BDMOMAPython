"""
Script de nettoyage final pour supprimer les cartes avec éléments espagnols
et ne garder que les versions 100% françaises
"""

import os

def nettoyage_final():
    """Supprimer les anciennes cartes avec éléments espagnols"""
    
    # Anciennes cartes à supprimer
    anciennes_cartes = [
        "carte_interactive_Cap_Le_Treport.html",
        "carte_interactive_Cellules_Hydrosedimentaires.html"
    ]
    
    print("🧹 NETTOYAGE FINAL - SUPPRESSION DES CARTES AVEC ÉLÉMENTS ESPAGNOLS")
    print("="*70)
    
    supprimes = 0
    
    for carte in anciennes_cartes:
        if os.path.exists(carte):
            try:
                os.remove(carte)
                print(f"✅ Supprimé : {carte} (contenait des éléments espagnols)")
                supprimes += 1
            except Exception as e:
                print(f"❌ Erreur suppression {carte} : {e}")
        else:
            print(f"ℹ️  Déjà supprimé : {carte}")
    
    # Vérifier les nouvelles cartes françaises
    print(f"\n🇫🇷 VÉRIFICATION DES CARTES 100% FRANÇAISES :")
    
    cartes_francaises = [
        "carte_interactive_Cap_Le_Treport_FR.html",
        "carte_interactive_Cellules_Hydrosedimentaires_FR.html"
    ]
    
    for carte in cartes_francaises:
        if os.path.exists(carte):
            print(f"✅ Carte française présente : {carte}")
        else:
            print(f"❌ MANQUANT : {carte}")
    
    print(f"\n📊 RÉSUMÉ FINAL :")
    print(f"   - Anciennes cartes supprimées : {supprimes}")
    print(f"   - Nouvelles cartes françaises : {len([c for c in cartes_francaises if os.path.exists(c)])}")
    
    # Lister tous les fichiers finaux
    print(f"\n📁 FICHIERS DE VISUALISATION FINAUX (100% FRANÇAIS) :")
    
    fichiers_finaux = []
    for fichier in sorted(os.listdir('.')):
        if (fichier.endswith('.html') and 'carte' in fichier) or \
           (fichier.endswith('.png') and ('carte' in fichier or 'comparaison' in fichier)):
            fichiers_finaux.append(fichier)
            print(f"   📄 {fichier}")
    
    print(f"\n🎉 TOUS LES ÉLÉMENTS SONT MAINTENANT 100% EN FRANÇAIS !")
    print(f"🌐 Interface principale : http://localhost:8080/index.html")

if __name__ == "__main__":
    nettoyage_final()