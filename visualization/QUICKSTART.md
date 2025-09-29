# 🚀 Guide de Démarrage Rapide

## Pour les Utilisateurs Pressés

### ⚡ Démarrage Ultra-Rapide (30 secondes)

1. **Ouvrir un terminal** dans ce dossier
2. **Exécuter** :
   ```powershell
   python start.py
   ```
3. **Choisir l'option 1** dans le menu
4. **L'interface s'ouvre automatiquement** dans votre navigateur

---

## 📋 Checklist de Vérification

Avant de commencer, vérifiez que vous avez :

- [ ] **Python 3.8+** installé
- [ ] **Accès internet** (pour les dépendances)
- [ ] **Navigateur web** moderne
- [ ] **Terminal/PowerShell** fonctionnel

---

## 🔧 Résolution de Problèmes Courants

### ❌ "Module non trouvé"
```powershell
pip install -r requirements.txt
```

### ❌ "Permission refusée"
```powershell
# Windows: Exécuter PowerShell en tant qu'administrateur
# Ou utiliser:
python -m pip install --user -r requirements.txt
```

### ❌ "Port 8080 déjà utilisé"
```powershell
# Utiliser un autre port
python -m http.server 8081
# Puis ouvrir http://localhost:8081
```

### ❌ "Données SIG non trouvées"
Vérifiez que le dossier `data/raw/SIG_data/` contient bien les shapefiles.

---

## 🗂️ Navigation Rapide

| 🎯 Objectif | 📁 Dossier | 🔗 Action |
|-------------|------------|-----------|
| **Voir les cartes** | `web/` | Ouvrir `index.html` |
| **Analyser les données** | `scripts/` | Exécuter `examiner_attributs_FR.py` |
| **Lire la doc** | `docs/` | Ouvrir `README_FR.md` |
| **Voir les résultats** | `outputs/` | Images PNG et rapports |

---

## 💡 Conseils d'Usage

### 🎓 Pour une Présentation Académique
1. Lancer l'interface web (`python start.py` → option 1)
2. Présenter les cartes interactives en temps réel
3. Utiliser les images PNG de `outputs/images/` pour les slides

### 📊 Pour une Analyse Poussée
1. Examiner les CSV dans `data/processed/`
2. Modifier les scripts dans `scripts/`
3. Consulter la documentation dans `docs/`

### 🗺️ Pour Créer de Nouvelles Cartes
1. Modifier `scripts/creer_cartes_francaises.py`
2. Relancer la génération
3. Les nouvelles cartes apparaissent dans `web/maps/`

---

## 📞 Support

En cas de problème :

1. **Consulter** `CONFIG.md` pour la configuration
2. **Vérifier** les logs dans le terminal
3. **Relancer** `python start.py` pour un menu guidé

---

*Guide mis à jour - Septembre 2025*
*Projet IMT Atlantique - Évolution Côtière Normandie*