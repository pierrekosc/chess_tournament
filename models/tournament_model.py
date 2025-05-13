# models/tournament_model.py

import logging
from datetime import date

logger = logging.getLogger(__name__)


class Tournament:
    """Représente un tournoi d'échecs complet et gère son état."""

    def __init__(
        self,
        name: str,
        location: str,
        description: str = '',
        num_rounds: int = 4
    ):
        # Métadonnées
        self.name = name
        self.location = location
        self.description = description

        # Dates automatiques
        self.start_date = date.today()
        self.end_date = None

        # Paramètres du tournoi
        self.num_rounds = num_rounds
        self.current_round = 0

        # Contenu dynamique
        self.players = []           # Liste des Player
        self.rounds = []            # Liste des Round
        self.past_matchups = set()  # Ensemble de paires (national_id1, national_id2)

        logger.debug(
            "Tournoi créé : %s à %s (début=%s), rounds=%d, desc='%s'",
            self.name,
            self.location,
            self.start_date,
            self.num_rounds,
            self.description
        )

    def add_player(self, player):
        """Ajoute un joueur au tournoi et journalise l'ajout."""
        self.players.append(player)
        logger.debug(
            "Joueur ajouté au tournoi '%s' : %s",
            self.name,
            player.full_name()
        )

    def add_round(self, round_obj):
        """Ajoute un round terminé à la liste et met à jour le compteur."""
        self.rounds.append(round_obj)
        self.current_round += 1
        logger.debug(
            "Round ajouté au tournoi '%s' : %s ({} rounds joués)".format(self.current_round),
            self.name,
            round_obj.name
        )

    def record_match(self, player1, player2):
        """Enregistre une paire de joueurs comme déjà jouée."""
        pair = tuple(sorted([player1.national_id, player2.national_id]))
        self.past_matchups.add(pair)
        logger.debug(
            "Match enregistré dans '%s' : %s vs %s",
            self.name,
            player1.full_name(),
            player2.full_name()
        )

    def end_tournament(self):
        """Clôture le tournoi en enregistrant la date de fin."""
        self.end_date = date.today()
        logger.debug(
            "Tournoi '%s' terminé à %s",
            self.name,
            self.end_date
        )

    def to_dict(self) -> dict:
        """Sérialise le tournoi en dictionnaire JSON-friendly."""
        return {
            'name': self.name,
            'location': self.location,
            'description': self.description,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'num_rounds': self.num_rounds,
            'current_round': self.current_round,
            'players': [p.national_id for p in self.players],
            'rounds': [r.to_dict() for r in self.rounds]
        }
