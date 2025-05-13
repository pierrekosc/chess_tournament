from models.player_model import Player
from services.player_storage_service import PlayerStorageService


class PlayerController:
    def __init__(self):
        self.storage = PlayerStorageService()

    def create_player(
        self,
        first_name: str,
        last_name: str,
        birthdate: str,
        national_id: str
    ) -> Player:
        """
        Crée un joueur à partir des données fournies et le sauvegarde.
        birthdate doit être au format ISO 'YYYY-MM-DD'.
        national_id au format 'AB12345'.
        """
        player = Player(
            first_name=first_name,
            last_name=last_name,
            national_id=national_id,
            birthdate=birthdate
        )
        # Sauvegarde dans players.json
        self.storage.save_player(player)
        return player
