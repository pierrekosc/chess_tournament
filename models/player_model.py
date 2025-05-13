import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class Player:
    """Représente un joueur avec ses informations personnelles et son score."""

    def __init__(
        self,
        first_name: str,
        last_name: str,
        national_id: str,
        birthdate: str
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id  # Identifiant unique, ex. 'AB12345'
        # stocke la date sous forme de datetime.date pour usage interne
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
        self.score = 0.0  # Score initial du joueur
        logger.debug(
            "Joueur créé : %s (%s)",
            self.full_name(),
            self.national_id
        )

    def full_name(self) -> str:
        """Retourne le nom complet du joueur."""
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        """Affiche les informations du joueur."""
        return (
            f"{self.full_name()} – ID : {self.national_id} – "
            f"Score : {self.score}"
        )

    def update_score(self, points: float) -> None:
        """Met à jour le score du joueur avec les points donnés."""
        self.score += points
        logger.debug(
            "Mise à jour du score pour %s : +%s",
            self.full_name(),
            points
        )
