from models.tournament_model import Tournament
from controllers.player_controller import PlayerController
from services.tournament_storage_service import TournamentStorageService
from services.json_service import JSONService


class TournamentController:
    """Contrôleur responsable de la logique du tournoi."""

    @staticmethod
    def create_tournament(name, location, description):
        """Crée un tournoi (sans joueurs) et le persiste immédiatement."""
        tournament = Tournament(name=name, location=location, description=description)
        # Sauvegarde initiale du tournoi (état sans joueurs)
        TournamentStorageService.save_tournament(tournament)
        return tournament

    @staticmethod
    def add_player(tournament, first_name, last_name, birthdate, national_id):
        """
        Crée un joueur, l'ajoute au tournoi, et persiste l'état.
        Renvoie l'objet Player créé.
        """
        # Création du joueur dans la base globale
        player = PlayerController().create_player(first_name, last_name, birthdate, national_id)
        # Ajout au tournoi
        tournament.add_player(player)
        # Persistance du tournoi mis à jour
        TournamentStorageService.save_tournament(tournament)
        return player

    @staticmethod
    def play_all_rounds(tournament):
        """
        Lance tous les rounds automatiquement jusqu'à ce que le tournoi soit fini,
        puis persiste le rapport et la version finale du tournoi.
        """
        from controllers.match_controller import MatchController  # pour éviter la circularité

        # Génère et joue tous les rounds
        MatchController.play_all_rounds(tournament)

        # Fixe la date de fin du tournoi
        tournament.end_tournament()

        # Met à jour le nombre réel de rounds joués
        tournament.number_of_rounds = len(tournament.rounds)

        # Sauvegarde du rapport JSON séparé
        JSONService.save_report(tournament)
        # Sauvegarde finale du tournoi
        TournamentStorageService.save_tournament(tournament)
