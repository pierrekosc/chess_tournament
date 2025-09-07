# services/player_storage_service.py

from models.player_model import Player
from services.json_service import JSONService
from config import DATA_DIR


class PlayerStorageService:
    """Service dédié à la sauvegarde des joueurs dans un fichier JSON."""

    FILE_PATH = str(DATA_DIR / "players.json")

    def save_player(self, player: Player) -> bool:
        players = self.load_all()
        exists = any(
            p.first_name == player.first_name and p.last_name == player.last_name
            for p in players
        )
        if exists:
            return False
        players.append(player)
        PlayerStorageService.save_all(players)
        return True

    @staticmethod
    def save_all(players: list[Player]):
        """Sauvegarde tous les joueurs dans le fichier JSON."""
        payload = [p.to_dict() for p in players]
        JSONService.save(PlayerStorageService.FILE_PATH, payload)

    @staticmethod
    def load_all() -> list[Player]:
        """Charge tous les joueurs du JSON et les convertit en objets Player."""
        items = JSONService.load(PlayerStorageService.FILE_PATH) or []
        players: list[Player] = [Player.from_dict(it) for it in items]
        return players

    @staticmethod
    def load_by_id(national_id: str) -> Player | None:
        """Retourne un objet Player à partir de son identifiant national (ou None si introuvable)."""
        items = JSONService.load(PlayerStorageService.FILE_PATH)
        for it in items:
            if it.get("national_id") == national_id:
                return Player.from_dict(it)
        return None
