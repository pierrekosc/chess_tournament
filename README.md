# Chess Tournament Manager

Une application console **autonome et hors ligne** pour gérer tournois d'échecs en suivant le modèle MVC.

---

## Objectif

* Créer et gérer des **tournois d'échecs**.
* Enregistrer vos joueurs et tournois dans des **fichiers JSON**.
* Gérer automatiquement les **rounds**, appariements et scores.
* Générer un **rapport final** en JSON et l'afficher en console.
* Respecter les bonnes pratiques Python (PEP8) grâce à **flake8**.

---

## Structure du projet

```
chess/
├── .flake8               # Configuration Flake8
├── .gitignore            # Fichiers ignorés par Git
├── main.py               # Point d'entrée (menu principal)
├── requirements.txt      # Dépendances Python
├── README.md             # Ce document
│
├── controllers/          # Logique métier (M de MVC)
│   ├── player_controller.py
│   ├── match_controller.py
│   └── tournament_controller.py
│
├── models/               # Représentations de données (M de MVC)
│   ├── player_model.py
│   ├── match_model.py
│   ├── round_model.py
│   └── tournament_model.py
│
├── views/                # Interface console (V de MVC)
│   ├── console_view.py
│   ├── player_view.py
│   ├── match_view.py
│   └── tournament_view.py
│
├── services/             # Persistences et utilitaires
│   ├── json_service.py
│   ├── player_storage_service.py
│   └── tournament_storage_service.py
│
├── data/                 # Base JSON (players.json, tournaments.json)
├── exports/              # Rapports JSON exportables
└── flake8_report/        # Rapport HTML flake8 (0 violation)
```

---

## Installation et exécution

1. **Cloner** le dépôt :

   ```bash
   git clone <URL_DU_DEPOT>
   cd chess
   ```

2. **Créer** et activer un **venv** Python :

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   # .venv\Scripts\activate   # Windows
   ```

3. **Installer** les dépendances :

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Lancer** l’application :

   ```bash
   python main.py
   ```

---

##  Menu principal

Au démarrage, vous trouverez :

```
=== Gestion des Tournois d'Échecs ===
1. Créer un nouveau tournoi
2. Charger un tournoi existant
3. Afficher la liste des joueurs
4. Afficher la liste des tournois
5. Quitter
> 
```

* **Créer** : choix des infos tournoi + ajout des joueurs.
* **Charger** : sélectionne un tournoi sauvegardé.
* **Afficher** : liste alphabétique.
* **Quitter** : termine le programme.

---

## Persistance JSON

* `data/players.json` : base des joueurs.
* `data/tournaments.json` : base des tournois.
* `exports/` : rapports complets par tournoi (JSON horodaté).

Les services garantissent **synchronisation** mémoire ⇆ disque à chaque modification.

---

## Qualité du code (Flake8)

Nous utilisons **flake8** avec plugin `flake8-html` pour le style PEP8.

* Config : `.flake8` (max-line-length=119, exclusions).
* Rapport : `flake8 --format=html --htmldir=flake8_report .`
  Ouvrir `flake8_report/index.html` doit afficher **0 violation**.

---

## Contribution

Pull requests bienvenues pour :

* Ajouter des tests unitaires.
* Améliorer la persistance (SQLite, ORM).
* Interface graphique.

Merci de suivre les conventions PEP8 et d'ajouter votre rapport flake8.

---

*Développé par Centre Échecs · Licence MIT*
