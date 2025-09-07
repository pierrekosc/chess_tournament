class MenuView:
    """Vue CLI : affiche le menu et les messages utilisateur (aucune logique métier)."""

    def render_menu(self) -> None:
        print("\n=== Gestion des Tournois d'Échecs ===")
        print("1. Créer un nouveau tournoi")
        print("2. Ajouter des joueurs à un tournoi")
        print("3. Lancer les rounds d’un tournoi")
        print("4. Afficher le rapport d’un tournoi")
        print("5. Lister tous les tournois")
        print("6. Lister tous les joueurs")
        print("7. Charger un tournoi depuis JSON")
        print("8. Quitter")

    def ask_choice(self) -> str:
        return input("Votre choix: ").strip()

    # --- Méthodes d'affichage utilitaires ---

    def notify(self, message: str) -> None:
        """Message d'information générique."""
        print(message)

    @staticmethod
    def show_goodbye() -> None:
        print("\nMerci d'avoir utilisé le gestionnaire de tournoi. À bientôt !\n")

    @staticmethod
    def show_no_tournaments() -> None:
        print("Aucun tournoi en mémoire.")

    @staticmethod
    def show_tournaments_list(tournaments) -> None:
        print("\nTournois en mémoire :")
        for t in tournaments:
            end = getattr(t, "end_date", None) or "…"
            print(f"- {getattr(t, 'name', '?')} ({getattr(t, 'start_date', '?')} → {end})")

    @staticmethod
    def show_no_players() -> None:
        print("Aucun joueur enregistré.")

    @staticmethod
    def show_players_list(players) -> None:
        print("\nJoueurs enregistrés :")
        for p in players:
            if isinstance(p, dict):
                first = p.get('first_name', '')
                last = p.get('last_name', '')
                nid = p.get('national_id', '')
            else:
                first = getattr(p, 'first_name', '')
                last = getattr(p, 'last_name', '')
                nid = getattr(p, 'national_id', '')
            print(f"- {first} {last} ({nid})")