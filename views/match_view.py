# views/match_view.py

class MatchView:
    """Vue pour interagir avec l'utilisateur concernant un match."""

    @staticmethod
    def show_match(player1, player2):
        """Affiche les joueurs qui vont s'affronter."""
        print(f"\n Match : {player1.full_name()} VS {player2.full_name()}")

    @staticmethod
    def ask_scores(player1, player2):
        """Demande à l'utilisateur d'entrer les scores des deux joueurs."""
        print("\n Résultat du match :")
        score1 = MatchView._ask_score(player1)
        score2 = MatchView._ask_score(player2)
        return score1, score2

    @staticmethod
    def _ask_score(player):
        """Demande un score valide pour un joueur donné (1, 0.5 ou 0)."""
        while True:
            try:
                raw = input(f"Score de {player.full_name()} (1, 0.5 ou 0) : ")
                # Autoriser la virgule comme séparateur décimal
                raw = raw.replace(',', '.')
                score = float(raw)
                if score in {1.0, 0.5, 0.0}:
                    return score
                print("Entrée invalide. Tape 1, 0.5 ou 0.")
            except ValueError:
                print("Entrée invalide. Utilise uniquement 1, 0.5 ou 0.")
        
    @staticmethod
    def show_match_result(match):
        """Affiche le résultat d'un match."""
        print(f"\n Résultat du match : {match.get_result_summary()}")
        print(f"Gagnant : {match.get_winner_text()}")
    
    @staticmethod
    def show_round_results(round_obj):
        """Affiche tous les matchs et résultats d'un round."""
        header = f"\n--- {round_obj.name} ({round_obj.start_time} -> {round_obj.end_time or 'en cours'}) ---"
        print(header)
        for match in round_obj.matches:
            print(" •", f"{match.get_result_summary()} -> {match.get_winner_text()}")

    @staticmethod
    def show_all_rounds_results(tournament):
        """Affiche les résultats de tous les rounds d'un tournoi."""
        print(f"\nRésultats du tournoi : {tournament.name}")
        for round_obj in tournament.rounds:
            MatchView.show_round_results(round_obj)

