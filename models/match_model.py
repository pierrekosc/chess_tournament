import logging
from typing import Optional
from models.player_model import Player

logger = logging.getLogger(__name__)


class Match:
    """Représente un match entre deux joueurs avec leurs scores."""

    def __init__(
        self,
        player1: Player,
        player2: Player,
        score1: float = 0.0,
        score2: float = 0.0
    ):
        # Initialise les joueurs et leurs scores
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2
        logger.debug(
            "Match créé : %s vs %s – scores initiaux : %s, %s",
            player1.full_name(),
            player2.full_name(),
            score1,
            score2
        )

    def set_scores(self, score1: float, score2: float) -> None:
        """Met à jour les scores des deux joueurs."""
        self.score1 = score1
        self.score2 = score2
        logger.debug(
            "Mise à jour des scores : %s = %s, %s = %s",
            self.player1.full_name(),
            score1,
            self.player2.full_name(),
            score2
        )

    def get_winner(self) -> Optional[Player]:
        """Retourne le joueur gagnant ou None s'il y a égalité."""
        if self.score1 > self.score2:
            logger.debug("Gagnant : %s", self.player1.full_name())
            return self.player1
        elif self.score2 > self.score1:
            logger.debug("Gagnant : %s", self.player2.full_name())
            return self.player2
        logger.debug("Match nul entre %s et %s",
                     self.player1.full_name(),
                     self.player2.full_name())
        return None

    def get_result_summary(self) -> str:
        """Retourne une chaîne résumée du résultat du match."""
        winner = self.get_winner()
        winner_name = winner.full_name() if winner else "Égalité"
        summary = (
            f"{self.player1.full_name()} ({self.score1}) vs "
            f"{self.player2.full_name()} ({self.score2}) ➔ {winner_name}"
        )
        logger.debug("Résumé du match : %s", summary)
        return summary

    def to_tuple(self) -> tuple[list, list]:
        """Retourne le match sous forme de tuples sérialisables [id, score]."""
        return (
            [self.player1.national_id, self.score1],
            [self.player2.national_id, self.score2]
        )

    def __str__(self) -> str:
        """Représentation textuelle du match."""
        return self.get_result_summary()
