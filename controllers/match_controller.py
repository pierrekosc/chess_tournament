from models.match_model import Match
from models.player_model import Player
from models.round_model import Round
from views.match_view import MatchView
from services.pairing_service import available_pairs

class MatchController:
    ...

    @staticmethod
    def play_all_rounds(tournament):
        """Lance tous les rounds possibles du tournoi."""
        players = tournament.players
        already_played = set()
        round_number = 1

        while True:
            round_obj = MatchController._create_round(round_number, players, already_played)
            if round_obj is None:  # plus de paires disponibles
                break
            tournament.add_round(round_obj)
            round_number += 1

    @staticmethod
    def _create_round(round_number: int, players: list, already_played: set):
        """(Optionnel) Version factorisée si tu veux garder une méthode dédiée à la création d'un round."""
        pairs = available_pairs(players, already_played)
        if not pairs:
            return None
        return Round.create_from_pairs(
            f"Round {round_number}",
            pairs,
            already_played,
            MatchController._play_match
        )

    @staticmethod
    def _play_match(player1: 'Player', player2: 'Player') -> Match:
        """Joue un match entre deux joueurs et retourne l'objet Match."""
        score1, score2 = MatchView.ask_scores(player1, player2)
        # Mise à jour des scores cumulés des joueurs
        player1.update_score(score1)
        player2.update_score(score2)
        return Match(player1, player2, score1, score2)