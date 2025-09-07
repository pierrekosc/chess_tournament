from models.player_model import Player
from services.player_storage_service import PlayerStorageService

class PlayerController:
    def __init__(self):
        self.storage = PlayerStorageService()

    def create_player(self, first_name: str, last_name: str, birthdate: str, national_id: str) -> Player:
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "birthdate": birthdate,  # déjà ISO
            "national_id": national_id,
        }
        player = Player.from_dict(data)
        self.storage.save_player(player)
        return player