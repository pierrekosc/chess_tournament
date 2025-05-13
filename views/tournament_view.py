# views/tournament_view.py

class TournamentView:
    """Vue pour interagir avec l'utilisateur concernant le tournoi."""

    @staticmethod
    def ask_tournament_info():
        """Demande les informations de base du tournoi."""
        print("=== Création d’un nouveau tournoi ===")
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        description = input("Remarques (optionnelles) : ")
        return name, location, description

    @staticmethod
    def ask_number_of_players():
        """Demande combien de joueurs participeront."""
        while True:
            try:
                nb_players = int(input("Combien de joueurs veux-tu ajouter ? "))
                if nb_players < 2:
                    print("Il faut au moins 2 joueurs.")
                    continue
                return nb_players
            except ValueError:
                print("Entrée invalide. Entrez un nombre entier.")

    @staticmethod
    def display_player_creation_progress(current, total):
        """Affiche la progression de création des joueurs."""
        print(f"\nCréation du joueur {current}/{total}")

    @staticmethod
    def confirm_tournament_created(tournament):
        """Affiche les détails du tournoi créé."""
        print("\nTournoi créé avec succès !")
        print(f"Nom du tournoi : {tournament.name}")
        print(f"Lieu             : {tournament.location}")
        print(f"Date de début    : {tournament.start_date}")
        print(f"Date de fin      : {tournament.end_date or '– non définie –'}")
        print(f"Nombre de joueurs: {len(tournament.players)}")
        print("Liste des joueurs :")
        for player in sorted(tournament.players, key=lambda p: p.full_name()):
            print(f"- {player.full_name()} ({player.national_id})")

    @staticmethod
    def display_round(round_obj):
        """Affiche un round et ses matchs."""
        end = round_obj.end_time or "en cours"
        print(f"\n--- {round_obj.name} ({round_obj.start_time} → {end}) ---")
        for match in round_obj.matches:
            print(" •", match.get_result_summary())

    @staticmethod
    def display_tournament_report(tournament):
        """Affiche le rapport complet du tournoi."""
        print(f"\nRapport complet du tournoi « {tournament.name} »")
        print("Joueurs inscrits :")
        for p in sorted(tournament.players, key=lambda p: p.full_name()):
            print(" -", p.full_name())
        for rnd in tournament.rounds:
            TournamentView.display_round(rnd)
