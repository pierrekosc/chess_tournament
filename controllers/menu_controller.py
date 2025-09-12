"""
Controller du menu principal (MVC strict).

Responsabilités :
- Orchestrer la navigation (boucle de menu) et appeler les services.
- Récupérer/valider les choix utilisateur via la vue, transmettre les données aux vues spécialisées.
- Ne réalise AUCUNE I/O directe (pas de input/print) : tout passe par les vues.
"""
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from controllers.tournament_controller import TournamentController
from services.tournament_storage_service import TournamentStorageService
from services.player_storage_service import PlayerStorageService
from controllers.player_controller import PlayerController
from views.menu_view import MenuView



class MenuController:
    def __init__(self):
        """
        Initialise le contrôleur de menu.
        Effets :
            - Crée une instance de vue de menu.
            - Initialise la collection de tournois chargés en mémoire.
        """   
        self.tournaments = []
        self.view = MenuView()

    def _select_tournament(self, prompt: str):
        # Affiche la liste des tournois et retourne celui choisi, ou None.
        if not self.tournaments:
            TournamentView.display_tournament_choices(self.tournaments)
            return None
        idx = TournamentView.choose_tournament(self.tournaments)
        if idx is None:
            return None
        return self.tournaments[idx]


    def run(self):
        """Boucle principale dans le Controller (MVC strict)."""
        while True:
            self.view.render_menu()
            choice = self.view.ask_choice()

            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.add_players_to_tournament()
            elif choice == "3":
                self.run_rounds_for_tournament()
            elif choice == "4":
                self.display_tournament_report()
            elif choice == "5":
                self.list_tournaments()
            elif choice == "6":
                self.list_players()
            elif choice == "7":
                self.charger_tournoi_depuis_json()
            elif choice == "8":
                self.view.show_goodbye()
                break
            else:
                self.view.notify("Choix invalide.")

    def create_tournament(self):
        """Crée un nouveau tournoi et y ajoute des joueurs."""
        name, location, description = TournamentView.ask_tournament_info()
        tournament = TournamentController.create_tournament(name, location, description)
        count = TournamentView.ask_number_of_players()
        pc = PlayerController()
        players = []
        for i in range(1, count + 1):
            TournamentView.display_player_creation_progress(i, count)
            first, last, birth, nid = PlayerView.ask_player_info()
            players.append(pc.create_player(first, last, birth, nid))

        TournamentController.add_multiple_players(tournament, players)
        TournamentView.confirm_tournament_created(tournament)
        self.tournaments.append(tournament)


    def add_players_to_tournament(self):
        """Ajoute des joueurs à un tournoi existant."""
        tournoi = self._select_tournament("Choisissez un tournoi : ")
        if not tournoi:
            return

        count = TournamentView.ask_number_of_players()
        for i in range(1, count + 1):
            TournamentView.display_player_creation_progress(i, count)
            data = PlayerView.ask_player_info()
            player = PlayerController().create_and_save_player(data)
            TournamentController.add_player(tournoi, player)

    def run_rounds_for_tournament(self):
        """Joue tous les rounds d'un tournoi puis génère un rapport."""
        tournoi = self._select_tournament("Choisissez un tournoi à jouer : ")
        if not tournoi:
            return
        TournamentController.play_all_rounds(tournoi)
        players_sorted, rounds = TournamentController.get_tournament_report(tournoi)
        TournamentView.display_tournament_report(tournoi, players_sorted)
        report_path = TournamentStorageService.save_report(tournoi)
        self.view.notify(f"Rapport sauvegardé : {report_path}")

    def list_tournaments(self):
        """Affiche la liste des tournois chargés en mémoire."""
        if not self.tournaments:
            self.view.notify("Aucun tournoi disponible.")
        else:
            self.view.show_tournaments_list(self.tournaments)

    def list_players(self):
        """Affiche la liste de tous les joueurs connus (stockage)."""
        players = PlayerStorageService.load_all()
        if not players:
            self.view.show_no_players()
        else:
            self.view.show_players_list(players)

    def display_tournament_report(self):
        """Affiche le rapport d'un tournoi."""
        tournoi = self._select_tournament("Choisissez un tournoi à afficher : ")
        if not tournoi:
            return
        players_sorted, rounds = TournamentController.get_tournament_report(tournoi)
        TournamentView.display_tournament_report(tournoi, players_sorted)
        report_path = TournamentStorageService.save_report(tournoi)
        self.view.notify(f"Rapport sauvegardé : {report_path}")

    def charger_tournoi_depuis_json(self):
        """Affiche la liste de tous les tournois connus (stockage)."""
        items = TournamentStorageService.load_all()
        if not items:
            self.view.notify("Aucun tournoi à charger depuis JSON.")
            return

        idx = TournamentView.choose_tournament(items)
        if idx is None:
            return

        name = items[idx]['name']
        t = TournamentStorageService.load_tournament(name)
        if t:
            self.tournaments.append(t)
            self.view.notify(f"Tournoi '{t.name}' chargé en mémoire.")
        else:
            self.view.notify("Erreur lors du chargement du tournoi.")