# models/match_model.py
"""Modèle de données pour un match entre deux joueurs (couche Model, MVC)."""

from models.player_model import Player

class Match:
    """Représente un match entre deux joueurs avec leurs scores."""
    def __init__(self, player1: Player, player2: Player, score1: int = 0, score2: int = 0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def update_scores(self, score1: int, score2: int):
        """Met à jour les scores du match."""
        self.score1 = score1
        self.score2 = score2

    def get_result_summary(self) -> str:
        """Retourne un résumé du match sous forme de texte."""
        return f"{self.player1.full_name()} ({self.score1}) - ({self.score2}) {self.player2.full_name()}"

    def to_list(self) -> list:
        """Sérialise le match en liste pour JSON."""
        return [
            self.player1.national_id,
            self.player2.national_id,
            self.score1,
            self.score2
        ]

    @classmethod
    def from_list(cls, data: list, player_resolver: callable):
        """ Reconstruit un match à partir d'une liste [id1, id2, score1, score2]."""
        p1 = player_resolver(data[0])
        p2 = player_resolver(data[1])
        score1 = data[2]
        score2 = data[3]
        return cls(p1, p2, score1, score2)
    
    def get_winner(self):
        """Retourne le Player gagnant, ou None en cas d'égalité."""
        if self.score1 > self.score2:
            return self.player1
        if self.score2 > self.score1:
            return self.player2
        return None

    def get_winner_text(self) -> str:
        """Texte lisible : nom du gagnant ou 'Égalité'."""
        winner = self.get_winner()
        return winner.full_name() if winner else "Égalité"