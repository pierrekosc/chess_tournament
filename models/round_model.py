from datetime import datetime
from models.match_model import Match

class Round:
    """Classe modèle pour représenter un round dans un tournoi.
    Chaque round contient un nom, des horodatages et une liste de matchs."""

    def __init__(self, name: str):
        """Initialise un round avec un nom et une date de début."""
        self.name = name
        self.start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.end_time = None
        self.matches = []  # Liste de Match

    def end_round(self) -> None:
        """Enregistre l'heure de fin du round."""
        self.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_match(self, match) -> None:
        """Ajoute un match à la liste des matchs du round."""
        self.matches.append(match)

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
            'matches': [m.to_list() for m in self.matches]
        }
        
    @classmethod
    def from_dict(cls, data: dict, player_resolver: callable):
        """Reconstruit une instance de Round à partir d'un dictionnaire."""
        round_instance = cls(data['name'])
        round_instance.start_time = data.get('start_time')
        round_instance.end_time = data.get('end_time')
        matches = []
        for match_data in data.get("matches", []):
            match_obj = Match.from_list(match_data, player_resolver)
            matches.append(match_obj)
        round_instance.matches = matches
        return round_instance

    @classmethod
    def create_from_pairs(cls, round_number: int, pairs: list, already_played: set, play_match_callable: callable):
        """Crée un round à partir de paires de joueurs et d'une fonction de jeu de match."""
        if not pairs:
            return None
        round_instance = cls(f"Round {round_number}")
        for player1, player2 in pairs:
            match = play_match_callable(player1, player2)
            round_instance.add_match(match)
            key = tuple(sorted([player1.national_id, player2.national_id]))
            already_played.add(key)
            round_instance.end_round()
        return round_instance
