# services/player_storage_service.py

from services.json_service import JSONService


class PlayerStorageService:
    """Service dédié à la sauvegarde des joueurs dans un fichier JSON."""

    FILE_PATH = "data/players.json"

    @staticmethod
    def save_player(player):
        """Ajoute un joueur au fichier JSON."""
        existing_players = JSONService.load(PlayerStorageService.FILE_PATH)

        # Vérifie si le joueur est déjà enregistré (via son ID)
        if any(p['national_id'] == player.national_id for p in existing_players):
            print(f"Joueur {player.full_name()} déjà enregistré.")
            return

        # Prépare le dictionnaire du joueur
        player_data = {
            "first_name": player.first_name,
            "last_name": player.last_name,
            "national_id": player.national_id,
            "birthdate": player.birthdate
        }

        existing_players.append(player_data)
        JSONService.save(PlayerStorageService.FILE_PATH, existing_players)
        print(f"Joueur sauvegardé dans {PlayerStorageService.FILE_PATH}")

    @staticmethod
    def load_all():
        return JSONService.load(PlayerStorageService.FILE_PATH)
