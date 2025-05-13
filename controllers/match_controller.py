from models.match_model import Match
from models.round_model import Round
from views.match_view import MatchView


class MatchController:
    """Gère la logique des matchs entre les joueurs."""

    @staticmethod
    def play_all_rounds(tournament):
        """Joue tous les matchs possibles entre les joueurs sans répétition."""
        already_played = set()
        players = tournament.players
        round_number = 1

        # On génère toutes les paires possibles
        while True:
            round_obj = Round(f"Round {round_number}")
            available_pairs = []

            # Génère toutes les paires non encore jouées
            for i in range(len(players)):
                for j in range(i + 1, len(players)):
                    p1 = players[i]
                    p2 = players[j]
                    pair = tuple(sorted([p1.national_id, p2.national_id]))
                    if pair not in already_played:
                        available_pairs.append((p1, p2))
                        already_played.add(pair)

            if not available_pairs:
                break  # Plus de paires disponibles → fin du tournoi

            for p1, p2 in available_pairs:
                MatchView.show_match(p1, p2)
                score1, score2 = MatchView.ask_scores(p1, p2)

                # Mise à jour des scores
                p1.update_score(score1)
                p2.update_score(score2)

                match = Match(p1, p2, score1, score2)
                MatchView.show_result(match)
                round_obj.add_match(match)

            round_obj.end_round()
            tournament.add_round(round_obj)

            # Affiche les résultats du round
            for result in round_obj.get_match_results():
                print(result)

            round_number += 1
