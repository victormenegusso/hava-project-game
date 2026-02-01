import arcade
from src import constants
from src.views.game_view import GameView

class MenuView(arcade.View):
    def on_show_view(self):
        self.window.background_color = arcade.color.DARK_BLUE

    def on_draw(self):
        self.clear()
        
        arcade.draw_text(
            "Aventura em Família",
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 2 + 50,
            arcade.color.WHITE,
            font_size=40,
            anchor_x="center",
            anchor_y="center"
        )
        
        arcade.draw_text(
            "Pressione ENTER para Jogar",
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 2 - 20,
            arcade.color.GRAY,
            font_size=20,
            anchor_x="center",
            anchor_y="center"
        )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            game_view = GameView()
            self.window.show_view(game_view)
