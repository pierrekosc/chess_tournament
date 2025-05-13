# main.py

import logging
from controllers.tournament_controller import TournamentController
from views.tournament_view import TournamentView
from views.player_view import PlayerView
from views.console_view import ConsoleView

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def main():
    tournaments = []  # tournois créés ou chargés en mémoire

    while True:
        choice = ConsoleView.show_main_menu()

        if choice == '1':
            # Créer un nouveau tournoi
            name, location, description = TournamentView.ask_tournament_info()
            tournament = TournamentController.create_tournament(name, location, description)
            nb = TournamentView.ask_number_of_players()
            for i in range(1, nb + 1):
                TournamentView.display_player_creation_progress(i, nb)
                first, last, birth, nid = PlayerView.ask_player_info()
                TournamentController.add_player(tournament, first, last, birth, nid)
            TournamentView.confirm_tournament_created(tournament)
            tournaments.append(tournament)

        elif choice == '2':
            # Ajouter des joueurs à un tournoi existant
            if not tournaments:
                print("Aucun tournoi en mémoire.")
            else:
                for idx, t in enumerate(tournaments, start=1):
                    print(f"{idx}. {t.name}")
                sel = int(input("Choisissez un tournoi : ")) - 1
                if 0 <= sel < len(tournaments):
                    t = tournaments[sel]
                    nb = TournamentView.ask_number_of_players()
                    for i in range(1, nb + 1):
                        TournamentView.display_player_creation_progress(i, nb)
                        first, last, birth, nid = PlayerView.ask_player_info()
                        TournamentController.add_player(t, first, last, birth, nid)
                else:
                    print("Sélection invalide.")

        elif choice == '3':
            # Lancer les rounds d’un tournoi
            if not tournaments:
                print("Aucun tournoi en mémoire.")
            else:
                for idx, t in enumerate(tournaments, start=1):
                    print(f"{idx}. {t.name}")
                sel = int(input("Choisissez un tournoi à jouer : ")) - 1
                if 0 <= sel < len(tournaments):
                    t = tournaments[sel]
                    TournamentController.play_all_rounds(t)
                    TournamentView.display_tournament_report(t)
                else:
                    print("Sélection invalide.")

        elif choice == '4':
            # Afficher le rapport d’un tournoi
            if not tournaments:
                print("Aucun tournoi en mémoire.")
            else:
                for idx, t in enumerate(tournaments, start=1):
                    print(f"{idx}. {t.name}")
                sel = int(input("Choisissez un tournoi à afficher : ")) - 1
                if 0 <= sel < len(tournaments):
                    TournamentView.display_tournament_report(tournaments[sel])
                else:
                    print("Sélection invalide.")

        elif choice == '5':
            # Lister tous les tournois (en mémoire)
            if not tournaments:
                print("Aucun tournoi en mémoire.")
            else:
                print("\nTournois en mémoire :")
                for t in tournaments:
                    print(f"- {t.name} ({t.start_date} → {t.end_date or '…'})")

        elif choice == '6':
            # Lister tous les joueurs (globaux)
            from services.player_storage_service import PlayerStorageService
            players = PlayerStorageService.load_all()
            if not players:
                print("Aucun joueur enregistré.")
            else:
                print("\nJoueurs enregistrés :")
                for p in sorted(players, key=lambda x: x['last_name']):
                    print(f"- {p['first_name']} {p['last_name']} ({p['national_id']})")

        elif choice == '7':
            # Charger un tournoi depuis JSON
            from services.tournament_storage_service import TournamentStorageService
            name = input("Nom du tournoi à charger : ")
            t = TournamentStorageService.load_tournament(name)
            if t:
                tournaments.append(t)
                print(f"Tournoi '{t.name}' chargé en mémoire.")
            else:
                print(f"Tournoi '{name}' non trouvé.")

        elif choice == '8':
            print("Au revoir !")
            break

        else:
            print("Option invalide, réessayez.")


if __name__ == "__main__":
    main()
