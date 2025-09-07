from datetime import datetime

class PlayerView:
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
    def ask_birthdate() -> str:
        while True:
            birth_input = input("Date de naissance (JJ/MM/AAAA) : ")
            try:
                return datetime.strptime(birth_input, "%d/%m/%Y").strftime("%Y-%m-%d")
            except ValueError:
                print("Date invalide. Utilisez JJ/MM/AAAA.")

    @staticmethod
    def ask_player_info():
        """Retourne juste les infos saisies, sans connaître Player.from_dict()."""
        print("\n=== Création d’un nouveau joueur ===")
        first = PlayerView.ask_first_name()
        last = PlayerView.ask_last_name()
        birth = PlayerView.ask_birthdate()
        nid = PlayerView.ask_national_id()
        return first, last, birth, nid

    @staticmethod
    def confirm_player_created(player):
        print(f"Joueur créé : {player.full_name()} ({player.national_id})")

    @staticmethod
    def show_player_score(player):
        print(f"{player.full_name()} - Score : {player.score}")