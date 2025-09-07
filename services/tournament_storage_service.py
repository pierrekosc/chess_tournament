from services.json_service import JSONService
from models.tournament_model import Tournament
from models.round_model import Round
from services.player_storage_service import PlayerStorageService
from config import DATA_DIR


class TournamentStorageService:
    """Service dédié à la sauvegarde des tournois dans un fichier JSON."""

    FILE_PATH = str(DATA_DIR / "tournaments.json")

    @staticmethod
    def load_all() -> list[dict]:
        """Retourne tous les tournois sous forme de dicts JSON-friendly."""
        return JSONService.load(TournamentStorageService.FILE_PATH)

    @staticmethod
    def load_tournament(name: str) -> Tournament | None:
        """Charge un tournoi par son nom et reconstruit les objets Player/Round/Match."""
        items = JSONService.load(TournamentStorageService.FILE_PATH)
        for item in items:
            if item.get("name") == name:
                # 1) Construire l'objet Tournament de base (ids + dicts)
                tournament = Tournament.from_dict(item)

                # 2) Resolver pour convertir un id joueur -> objet Player
                def _resolve_player(pid: str):
                    return PlayerStorageService.load_by_id(pid)

                # 3) Reconstituer la liste de joueurs si elle contient des ids
                if tournament.players and isinstance(tournament.players[0], str):
                    tournament.players = [
                        _resolve_player(pid) for pid in tournament.players
                    ]

                # 4) Reconstituer les rounds (dict -> Round avec Match et Players)
                if tournament.rounds and isinstance(tournament.rounds[0], dict):
                    tournament.rounds = [
                        Round.from_dict(rdict, _resolve_player) for rdict in tournament.rounds
                    ]

                return tournament
        return None

    
    @staticmethod
    def save_tournament(tournament: Tournament) -> None:
        """Sauvegarde un tournoi par son nom : remplace s'il existe,sinon on l'ajoute"""
        items = JSONService.load(TournamentStorageService.FILE_PATH)
        data = tournament.to_dict()

        # Cherche une entrée existante avec le même nom
        index = next((i for i, it in enumerate(items) if it.get("name") == data.get("name")), None)
        if index is None:
            items.append(data)
        else:
            items[index] = data

        JSONService.save(TournamentStorageService.FILE_PATH, items)

    @staticmethod
    def delete_tournament(name: str) -> bool:
        """Supprime un tournoi par son nom. Retourne True si quelque chose a été supprimé."""
        items = JSONService.load(TournamentStorageService.FILE_PATH)
        new_items = [it for it in items if it.get("name") != name]
        changed = len(new_items) != len(items)
        if changed:
            JSONService.save(TournamentStorageService.FILE_PATH, new_items)
        return changed
    @staticmethod
    def save_report(tournament: Tournament) -> str:
        """Génère et sauvegarde le rapport du tournoi en JSON."""
        return JSONService.save_report(tournament)