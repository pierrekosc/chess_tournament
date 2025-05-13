import json
import os
from datetime import date, datetime as _datetime


class JSONService:
    """Service utilitaire pour lire et écrire des fichiers JSON."""

    @staticmethod
    def load(file_path):
        """Charge les données depuis un fichier JSON, retourne une liste vide si le fichier est vide ou manquant."""
        if not os.path.exists(file_path):
            return []
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                return data if isinstance(data, list) else []
            except json.JSONDecodeError:
                return []

    @staticmethod
    def save(file_path, data):
        """
        Sauvegarde les données dans un fichier JSON (et crée le dossier s’il n’existe pas).
        Convertit automatiquement :
         - les objets avec to_dict()
         - les date/datetime en chaîne ISO
        """
        # Crée le dossier parent si nécessaire
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        def _default(o):
            # Si l'objet a to_dict(), on l'utilise
            if hasattr(o, "to_dict"):
                return o.to_dict()
            # Si c'est une date ou datetime, on renvoie une chaîne ISO
            if isinstance(o, (date, _datetime)):
                return o.isoformat()
            raise TypeError(f"Objet de type {type(o).__name__} n'est pas JSON serializable")

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False, default=_default)

    @staticmethod
    def save_report(tournament):
        """Génère et sauvegarde un rapport JSON complet du tournoi."""
        from datetime import datetime

        os.makedirs("exports", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"exports/tournament_report_{timestamp}.json"

        # On convertit explicitement les dates en chaînes pour le rapport
        report = {
            "name": tournament.name,
            "location": tournament.location,
            "description": tournament.description,
            "start_date": str(tournament.start_date),
            "end_date": str(tournament.end_date) if tournament.end_date else None,
            "players": [
                {
                    "first_name": p.first_name,
                    "last_name": p.last_name,
                    "national_id": p.national_id,
                    "birthdate": p.birthdate,  # déjà ISO dans PlayerView
                    "score": p.score
                }
                for p in tournament.players
            ],
            "rounds": [
                {
                    "name": r.name,
                    "start_time": r.start_time,
                    "end_time": r.end_time,
                    "matches": [
                        {
                            "player1": m.player1.full_name(),
                            "score1": m.score1,
                            "player2": m.player2.full_name(),
                            "score2": m.score2,
                            "winner": m.get_winner().full_name() if m.get_winner() else "Égalité"
                        }
                        for m in r.matches
                    ]
                }
                for r in tournament.rounds
            ]
        }

        # Sauvegarde du rapport en utilisant le même mécanisme de sérialisation
        JSONService.save(filename, report)
        print(f"[✅] Rapport sauvegardé dans : {filename}")
