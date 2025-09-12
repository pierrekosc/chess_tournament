from models.tournament_model import Tournament
from models.player_model import Player
from services.tournament_storage_service import TournamentStorageService

class TournamentController:
    """Contrôleur responsable de la logique du tournoi."""

    @staticmethod
    def create_tournament(name: str, location: str, description: str) -> Tournament:
        """Créer un tournoi et le sauvegarde via le service de stockage."""
        tournament = Tournament(name=name, location=location, description=description)
        TournamentStorageService.save_tournament(tournament)
        return tournament

    @staticmethod
    def add_player(tournament: Tournament, player: Player) -> Player:
        """Ajoute un joueur déjà construit au tournoi et persiste l'état."""
        tournament.add_player(player)
        TournamentStorageService.save_tournament(tournament)
        return player

    @staticmethod
    def add_multiple_players(tournament: Tournament, players: list[Player]) -> int:
        """Ajoute une liste de joueurs déjà construits au tournoi et persiste.
        Ne fait aucune interaction IHM (pas de print/input).
        """
        for p in players:
            TournamentController.add_player(tournament, p)
        return len(players)

    @staticmethod
    def play_all_rounds(tournament: Tournament) -> None:
        """Joue tous les rounds du tournoi, met à jour l'état et persiste."""
        from controllers.match_controller import MatchController
        MatchController.play_all_rounds(tournament)
        tournament.end_tournament()
        tournament.num_rounds = len(tournament.rounds)
        TournamentStorageService.save_tournament(tournament)

    @staticmethod
    def get_tournament_report(tournament: Tournament):
        """Retourne les joueurs triés et les rounds du tournoi."""
        players_sorted = sorted(tournament.players, key=lambda p: p.full_name())
        return players_sorted, tournament.rounds
