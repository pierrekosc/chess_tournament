# models/tournament_model.py
from datetime import date

class Tournament:
    def __init__(
        self,
        name: str,
        location: str,
        description: str = '',
        start_date=None,
        end_date=None,
        num_rounds: int = 4,
        players=None,
        rounds=None,
        current_round: int = 0
    ):
        # Métadonnées
        self.name = name
        self.location = location
        self.description = description

        # Dates (accepte date ou str ISO)
        if isinstance(start_date, str):
            self.start_date = date.fromisoformat(start_date)
        elif start_date is None:
            self.start_date = date.today()
        else:
            self.start_date = start_date

        if isinstance(end_date, str):
            self.end_date = date.fromisoformat(end_date)
        else:
            self.end_date = end_date  # None ou date

        # Paramètres & état
        self.num_rounds = num_rounds
        self.current_round = current_round
        self.players = players if players is not None else []   # en mémoire : objets Player
        self.rounds = rounds if rounds is not None else []      # en mémoire : objets Round
        self.past_matchups = set()

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round_obj):
        self.rounds.append(round_obj)
        self.current_round += 1

    def record_match(self, player1, player2):
        pair = tuple(sorted([player1.national_id, player2.national_id]))
        self.past_matchups.add(pair)

    def end_tournament(self):
        self.end_date = date.today()

    def to_dict(self) -> dict:
        """Sérialise pour JSON : players -> IDs, rounds -> dicts."""
        return {
            'name': self.name,
            'location': self.location,
            'description': self.description,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'num_rounds': self.num_rounds,
            'current_round': self.current_round,
            'players': [player.national_id for player in self.players],     # liste d'IDs
            'rounds': [r.to_dict() for r in self.rounds]          # liste de dicts
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Construit un Tournament depuis un dict JSON.
        NOTE: players ici sera une liste d'IDs, et rounds une liste de dicts.
        La reconstruction en vrais objets peut se faire dans le controller/service.
        """
        return cls(
            name=data['name'],
            location=data['location'],
            description=data.get('description', ''),
            start_date=data.get('start_date'),
            end_date=data.get('end_date'),
            num_rounds=data.get('num_rounds', 4),
            players=data.get('players', []),     # pour l'instant: liste d'IDs
            rounds=data.get('rounds', []),       # pour l'instant: liste de dicts
            current_round=data.get('current_round', 0)
        )