# views/player_view.py

from datetime import datetime


class PlayerView:
    """Vue pour interagir avec l'utilisateur concernant les joueurs."""

    @staticmethod
    def ask_first_name():
        return input("Prénom du joueur : ")

    @staticmethod
    def ask_last_name():
        return input("Nom du joueur : ")

    @staticmethod
    def ask_national_id():
        return input("ID Fédéral (ex: AB12345) : ")

    @staticmethod
    def ask_birthdate():
        return input("Date de naissance (JJ/MM/AAAA) : ")

    @staticmethod
    def ask_player_info():
        """Demande toutes les infos d'un joueur et retourne (first, last, birth_iso, national_id)."""
        print("\n=== Création d’un nouveau joueur ===")
        first = PlayerView.ask_first_name()
        last = PlayerView.ask_last_name()

        # Boucle de validation de la date
        while True:
            birth_input = PlayerView.ask_birthdate()
            try:
                # Conversion JJ/MM/AAAA → YYYY-MM-DD
                birth_iso = datetime.strptime(birth_input, "%d/%m/%Y").strftime("%Y-%m-%d")
                break
            except ValueError:
                print("Date invalide. Utilisez le format JJ/MM/AAAA (ex. 31/12/1990).")

        nid = PlayerView.ask_national_id()
        return first, last, birth_iso, nid

    @staticmethod
    def confirm_player_created(player):
        print(f"Joueur créé : {player.full_name()} ({player.national_id})")

    @staticmethod
    def show_player_score(player):
        print(f"{player.full_name()} - Score : {player.score}")
