class ConsoleView:
    """Vue pour afficher le menu principal et lire le choix de l'utilisateur."""

    @staticmethod
    def show_main_menu() -> str:
        print("\n=== Menu Principal ===")
        print("1. Créer un nouveau tournoi")
        print("2. Ajouter des joueurs à un tournoi")
        print("3. Lancer les rounds d’un tournoi")
        print("4. Afficher le rapport d’un tournoi")
        print("5. Lister tous les tournois")
        print("6. Lister tous les joueurs")
        print("7. Charger un tournoi depuis JSON")
        print("8. Quitter")
        return input("Sélectionnez une option (1-8) : ")
