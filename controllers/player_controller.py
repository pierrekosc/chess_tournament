"""
Contrôleur des joueurs (MVC).

Responsabilités :
- Orchestrer la création des joueurs.
- Déléguer la persistance au service de stockage (`PlayerStorageService`).
- Retourner des objets `Player` prêts à être utilisés par les autres contrôleurs.

"""
from models.player_model import Player
from services.player_storage_service import PlayerStorageService

class PlayerController:
    """Controller responsable de la gestion des joueurs."""
    def __init__(self):
        self.storage = PlayerStorageService()

    def create_player(self, first_name: str, last_name: str, birthdate: str, national_id: str) -> Player:
        """Crée un joueur et le sauvegarde via le service de stockage."""
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "birthdate": birthdate,
            "national_id": national_id,
        }
        player = Player.from_dict(data)
        self.storage.save_player(player)
        return player