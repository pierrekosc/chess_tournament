# views/match_view.py

class MatchView:
    """Vue pour interagir avec l'utilisateur concernant un match."""

    @staticmethod
    def show_match(player1, player2):
        """Affiche les joueurs qui vont s'affronter."""
        print(f"\n⚔️  Match : {player1.full_name()} VS {player2.full_name()}")

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
                score = float(input(f"Score de {player.full_name()} (1, 0.5 ou 0) : "))
                if score in [1.0, 0.5, 0.0]:
                    return score
                else:
                    print("Entrée invalide. Tape un nombre comme 1, 0.5 ou 0.")
            except ValueError:
                print(" Entrée invalide. Utilise uniquement des chiffres.")

    @staticmethod
    def show_result(match):
        """Affiche le résumé du match avec gagnant ou égalité."""
        print(f"\n Résultat : {match.get_result_summary()}")
