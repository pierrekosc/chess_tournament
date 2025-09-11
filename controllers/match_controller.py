from models.match_model import Match
from models.player_model import Player
from models.round_model import Round
from views.match_view import MatchView
from services.pairing_service import available_pairs

"""
Contrôleur des rounds et matchs (couche Controller, MVC).

Rôle général:
- Orchestrer la génération des rounds d'un tournoi et le déroulement des matchs.
- Déléguer l'affichage/saisie des scores à la vue (`MatchView`).
- Ne fait aucune E/S fichier et ne contient pas de logique métier lourde (celle-ci vit
  dans les Models et dans les Services d'appariement).

Dépendances:
- models.match_model.Match
- models.player_model.Player
- models.round_model.Round
- views.match_view.MatchView
- services.pairing_service.available_pairs
"""

class MatchController:
    """Orchestre la création des rounds et le déroulement des matchs."""
    ...

    @staticmethod
    def play_all_rounds(tournament):
        """Lance tous les rounds possibles du tournoi jusqu'à épuisement des paires."""
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
        """Construit un round à partir des paires de joueurs actuellement disponibles."""
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
        """Joue un match: saisie des scores via la vue, mise à jour des joueurs, retourne un `Match`."""
        score1, score2 = MatchView.ask_scores(player1, player2)
        # Mise à jour des scores cumulés des joueurs
        player1.update_score(score1)
        player2.update_score(score2)
        return Match(player1, player2, score1, score2)