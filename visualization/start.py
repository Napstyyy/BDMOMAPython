"""
Script de démarrage rapide pour le projet d'évolution côtière
Facilite le lancement et la navigation du projet
"""

import os
import subprocess
import sys
import webbrowser
import time

def verifier_dependances():
    """Vérifier que les dépendances Python sont installées"""
    
    dependances_requises = [
        'geopandas',
        'matplotlib', 
        'folium',
        'pandas'
    ]
    
    print("🔍 VÉRIFICATION DES DÉPENDANCES")
    print("="*40)
    
    manquantes = []
    
    for dep in dependances_requises:
        try:
            __import__(dep)
            print(f"✅ {dep}")
        except ImportError:
            print(f"❌ {dep} - MANQUANT")
            manquantes.append(dep)
    
    if manquantes:
        print(f"\n⚠️  Dépendances manquantes : {', '.join(manquantes)}")
        print("💡 Installez avec : pip install " + " ".join(manquantes))
        return False
    
    print("✅ Toutes les dépendances sont présentes")
    return True

def demarrer_serveur_web():
    """Démarrer le serveur web local"""
    
    print(f"\n🌐 DÉMARRAGE DU SERVEUR WEB")
    print("="*40)
    
    # Vérifier si on est dans le bon répertoire
    if not os.path.exists('web/index.html'):
        print("❌ Fichier web/index.html non trouvé")
        print("💡 Exécutez ce script depuis la racine du projet")
        return False
    
    try:
        print("🚀 Démarrage du serveur sur le port 8080...")
        
        # Changer vers le répertoire web
        os.chdir('web')
        
        # Démarrer le serveur en arrière-plan
        if sys.platform.startswith('win'):
            process = subprocess.Popen([
                sys.executable, '-m', 'http.server', '8080'
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            process = subprocess.Popen([
                sys.executable, '-m', 'http.server', '8080'
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Attendre un peu pour que le serveur démarre
        time.sleep(2)
        
        print("✅ Serveur démarré avec succès")
        print("🌐 URL : http://localhost:8080/index.html")
        
        return process
        
    except Exception as e:
        print(f"❌ Erreur lors du démarrage du serveur : {e}")
        return False

def afficher_menu():
    """Afficher le menu principal"""
    
    print(f"\n🗺️  PROJET ÉVOLUTION CÔTIÈRE - IMT ATLANTIQUE")
    print("="*50)
    print("1. 🌐 Lancer l'interface web")
    print("2. 📊 Analyser les données")
    print("3. 🗺️  Générer les cartes")
    print("4. 📁 Explorer la structure")
    print("5. 📖 Ouvrir la documentation")
    print("6. ❌ Quitter")
    print("="*50)
    
    return input("Choisissez une option (1-6) : ")

def analyser_donnees():
    """Exécuter l'analyse des données"""
    
    print(f"\n📊 ANALYSE DES DONNÉES")
    print("="*30)
    
    script_analyse = 'scripts/examiner_attributs_FR.py'
    
    if os.path.exists(script_analyse):
        try:
            subprocess.run([sys.executable, script_analyse], check=True)
            print("✅ Analyse terminée")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors de l'analyse : {e}")
    else:
        print(f"❌ Script {script_analyse} non trouvé")

def generer_cartes():
    """Générer les cartes et visualisations"""
    
    print(f"\n🗺️  GÉNÉRATION DES CARTES")
    print("="*35)
    
    script_cartes = 'scripts/visualiser_ameliore_FR.py'
    
    if os.path.exists(script_cartes):
        try:
            subprocess.run([sys.executable, script_cartes], check=True)
            print("✅ Cartes générées")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors de la génération : {e}")
    else:
        print(f"❌ Script {script_cartes} non trouvé")

def explorer_structure():
    """Afficher la structure du projet"""
    
    print(f"\n📁 STRUCTURE DU PROJET")
    print("="*30)
    
    structure_info = """
📦 projet-evolution-cotiere/
├── 📁 docs/                    # Documentation
├── 📁 data/                    # Données
│   ├── 📁 raw/                 # Données sources
│   └── 📁 processed/           # Données traitées
├── 📁 scripts/                 # Scripts Python
├── 📁 web/                     # Interface web
│   └── 📁 maps/                # Cartes interactives
└── 📁 outputs/                 # Résultats
    └── 📁 images/              # Images générées
    """
    
    print(structure_info)
    
    # Compter les fichiers
    print("📊 STATISTIQUES :")
    for dossier in ['docs', 'data/processed', 'scripts', 'web/maps', 'outputs/images']:
        if os.path.exists(dossier):
            nb_fichiers = len([f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))])
            print(f"   {dossier:<20} : {nb_fichiers} fichiers")

def ouvrir_documentation():
    """Ouvrir la documentation principale"""
    
    print(f"\n📖 DOCUMENTATION")
    print("="*25)
    
    docs_disponibles = [
        ('README.md', 'Vue d\'ensemble du projet'),
        ('docs/README_FR.md', 'Guide détaillé'),
        ('docs/RESUME_ANALYSE_SIG_FR.md', 'Analyse scientifique'),
        ('docs/GUIDE_VISUALISATION_SIG_FR.md', 'Guide technique'),
        ('CONFIG.md', 'Configuration')
    ]
    
    for doc, description in docs_disponibles:
        if os.path.exists(doc):
            print(f"✅ {doc:<35} - {description}")
        else:
            print(f"❌ {doc:<35} - MANQUANT")

def main():
    """Fonction principale du menu interactif"""
    
    # Vérifier les dépendances au démarrage
    if not verifier_dependances():
        input("\nAppuyez sur Entrée pour continuer quand même...")
    
    serveur_process = None
    
    try:
        while True:
            choix = afficher_menu()
            
            if choix == '1':
                if not serveur_process:
                    serveur_process = demarrer_serveur_web()
                if serveur_process:
                    try:
                        webbrowser.open('http://localhost:8080/index.html')
                        print("🌐 Interface ouverte dans le navigateur")
                    except:
                        print("⚠️  Ouvrez manuellement : http://localhost:8080/index.html")
                        
            elif choix == '2':
                analyser_donnees()
                
            elif choix == '3':
                generer_cartes()
                
            elif choix == '4':
                explorer_structure()
                
            elif choix == '5':
                ouvrir_documentation()
                
            elif choix == '6':
                print("👋 Au revoir !")
                break
                
            else:
                print("❌ Option non valide")
            
            input("\nAppuyez sur Entrée pour continuer...")
    
    finally:
        # Nettoyer le serveur si il était démarré
        if serveur_process:
            try:
                serveur_process.terminate()
                print("🛑 Serveur web arrêté")
            except:
                pass

if __name__ == "__main__":
    main()