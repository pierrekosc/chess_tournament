"""
models/round_model.py

Ce module contient la classe Round qui représente un tour (round) dans un tournoi.
Elle gère l'heure de début, l'heure de fin, et les matchs associés.
"""


from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class Round:
    """
    Classe modèle pour représenter un round dans un tournoi.
    Chaque round contient un nom, des horodatages et une liste de matchs.
    """

    def __init__(self, name: str):
        """Initialise un round avec un nom et une date de début."""
        self.name = name
        self.start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.end_time = None
        self.matches = []  # Liste de Match
        logger.debug(
            "Round initialisé : %s - Début à %s",
            self.name,
            self.start_time
        )

    def end_round(self) -> None:
        """Enregistre l'heure de fin du round."""
        self.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.debug(
            "Round terminé : %s - Fin à %s",
            self.name,
            self.end_time
        )

    def add_match(self, match) -> None:
        """Ajoute un match à la liste des matchs du round."""
        self.matches.append(match)
        logger.debug(
            "Match ajouté à %s : %s",
            self.name,
            match
        )

    def __str__(self) -> str:
        """Retourne une description textuelle du round."""
        end_display = self.end_time if self.end_time else "En cours"
        return f"{self.name} - Début : {self.start_time} - Fin : {end_display}"

    def get_match_results(self) -> list[str]:
        """Retourne une liste de résumés de chaque match du round."""
        return [match.get_result_summary() for match in self.matches]

    def to_dict(self) -> dict:
        """Sérialise le round en dict JSON-friendly."""
        return {
            'name': self.name,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'matches': [m.to_tuple() for m in self.matches]
        }
