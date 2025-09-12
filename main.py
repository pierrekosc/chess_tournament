from controllers.menu_controller import MenuController
from services.json_service import ensure_storage_ready


def main():
    """Point d'entrée principal de l'application."""
    try:
        ensure_storage_ready()
    except Exception as exc:
        print(f"[ERREUR] Impossible d'initialiser le stockage: {exc}")
        return 
    controller = MenuController()
    controller.run()

if __name__ == "__main__":
    main()
