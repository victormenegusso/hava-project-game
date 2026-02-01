import arcade
from src import constants
from src.views.game_view import GameView

def main():
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = GameView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
