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
        TournamentView._print_tournament_header(tournament)
        TournamentView._print_players_list(tournament.players)

    @staticmethod
    def _print_tournament_header(tournament):
        print(f"Nom du tournoi : {tournament.name}")
        print(f"Lieu             : {tournament.location}")
        print(f"Date de début    : {tournament.start_date}")
        print(f"Date de fin      : {tournament.end_date or '– non définie –'}")
        print(f"Nombre de joueurs: {len(tournament.players)}")

    @staticmethod
    def _print_players_list(players):
        if not players:
            return
        print("Liste des joueurs :")
        for player in sorted(players, key=lambda p: p.full_name() if hasattr(p, 'full_name') else str(p)):
            nid = getattr(player, 'national_id', '')
            fullname = player.full_name() if hasattr(player, 'full_name') else str(player)
            print(f"- {fullname} ({nid})")

    @staticmethod
    def display_tournament_report(tournament, players_sorted=None):
        """Affiche un rapport complet du tournoi (entête, joueurs, rounds, matchs)."""
        print("\n=== Rapport du Tournoi ===")
        TournamentView._print_tournament_header(tournament)
        # joueurs (triés si fourni)
        players = players_sorted if players_sorted is not None else getattr(tournament, 'players', [])
        TournamentView._print_players_list(players)

        # rounds & matchs
        rounds = getattr(tournament, 'rounds', [])
        if rounds:
            print("\n— Rounds —")
            for r in rounds:
                end = r.end_time or "—"
                print(f"\n{r.name} ({r.start_time} → {end})")
                for m in getattr(r, 'matches', []):
                    # supporte get_result_summary() si présent, sinon format minimal
                    if hasattr(m, 'get_result_summary'):
                        print(f"   - {m.get_result_summary()}")
                    else:
                        p1 = getattr(m, 'player1', None)
                        p2 = getattr(m, 'player2', None)
                        s1 = getattr(m, 'score1', '?')
                        s2 = getattr(m, 'score2', '?')
                        p1n = p1.full_name() if hasattr(p1, 'full_name') else str(p1)
                        p2n = p2.full_name() if hasattr(p2, 'full_name') else str(p2)
                        print(f"   - {p1n} {s1} vs {p2n} {s2}")

    @staticmethod
    def display_round(round_obj):
        """Affiche un round et ses matchs."""
        end = round_obj.end_time or "en cours"
        print(f"\n--- {round_obj.name} ({round_obj.start_time} → {end}) ---")
        for match in round_obj.matches:
            print(" •", match.get_result_summary())

    @staticmethod
    def display_tournament_choices(tournaments, prompt: str = "Choisissez un tournoi : ") -> int | None:
        """
        Affiche la liste des tournois (objets ou dicts) et retourne l'index (0-based) choisi,
        ou None si annulation / erreur.
        """
        if not tournaments:
            print("Aucun tournoi en mémoire.")
            return None

        print("\nTournois disponibles :")
        for i, t in enumerate(tournaments, start=1):
            if isinstance(t, dict):
                name = t.get("name", "?")
                loc = t.get("location", "?")
                start = t.get("start_date", "?")
            else:
                name = getattr(t, "name", "?")
                loc = getattr(t, "location", "?")
                start = getattr(t, "start_date", "?")
            print(f"{i}. {name} — {loc} (début : {start})")

        try:
            sel = int(input(prompt)) - 1
            if 0 <= sel < len(tournaments):
                return sel
            print("Sélection invalide.")
        except ValueError:
            print("Entrée non valide.")
        return None

    @staticmethod
    def choose_tournament(items, prompt: str = "Numéro du tournoi à charger : ") -> int | None:
        """Alias : délègue à display_tournament_choices pour conserver la compatibilité."""
        return TournamentView.display_tournament_choices(items, prompt)

    @staticmethod
    def display_tournaments_from_dicts(items) -> int | None:
        """Alias : accepte une liste de dicts et renvoie l'index choisi."""
        return TournamentView.display_tournament_choices(items)