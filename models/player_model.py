"""Modèle de données pour un joueur (couche Model, MVC)."""

from datetime import datetime, date

class Player:
    """Représente un joueur avec ses informations et son score."""
    def __init__(self, first_name: str, last_name: str, birthdate: str, national_id: str):
        self.first_name = first_name
        self.last_name = last_name
        # Ici on parse une seule fois du ISO vers un objet date
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
        self.national_id = national_id
        self.score = 0.0

    @classmethod
    def from_dict(cls, data: dict) -> "Player":
        """Crée une instance de Player à partir d'un dictionnaire."""
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birthdate=data["birthdate"],
            national_id=data["national_id"]
        )

    def to_dict(self) -> dict:
        """Sérialise le joueur en dictionnaire pour JSON."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate": self.birthdate.isoformat(),
            "national_id": self.national_id,
            "score": self.score,
        }

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
        
   
