# services/tournament_storage_service.py

import logging
from services.json_service import JSONService
from models.tournament_model import Tournament

logger = logging.getLogger(__name__)


class TournamentStorageService:
    """Service dédié à la sauvegarde des tournois dans un fichier JSON."""

    FILE_PATH = "data/tournaments.json"

    @staticmethod
    def save_tournament(tournament):
        """Ajoute ou met à jour un tournoi dans le fichier JSON via to_dict()."""
        # Charge la liste existante de tournois (liste de dicts)
        data = JSONService.load(TournamentStorageService.FILE_PATH)

        # Sérialisation du tournoi en dict
        data.append(tournament.to_dict())

        # Persistance du JSON
        JSONService.save(TournamentStorageService.FILE_PATH, data)
        logger.info(
            "Tournoi '%s' sauvegardé dans %s",
            tournament.name,
            TournamentStorageService.FILE_PATH
        )

        @staticmethod
        def load_all():
            return JSONService.load(TournamentStorageService.FILE_PATH)

        @staticmethod
        def load_tournament(name):
            all_t = JSONService.load(TournamentStorageService.FILE_PATH)
            for d in all_t:
                if d['name'] == name:
                    return Tournament.from_dict(d)  # à ajouter dans ton modèle
            return None
