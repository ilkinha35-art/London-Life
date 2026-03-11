import arcade
from game_logic import Vehicle, Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "London Life - Arcade"

class LondonLife(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Veículos: carro, ônibus e caminhão
        self.vehicles = [
            Vehicle(100, 200, 80, 40, arcade.color.RED, 3),     # carro
            Vehicle(300, 300, 120, 50, arcade.color.BLUE, -2), # ônibus
            Vehicle(500, 400, 160, 60, arcade.color.GRAY, 2),  # caminhão
        ]

        # Personagem controlável
        self.player = Player(400, 50)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("London Life - Atravessando a rua", 10, 570, arcade.color.BLACK, 20)

        # Desenha veículos
        for v in self.vehicles:
            v.draw()

        # Desenha personagem
        self.player.draw()

    def on_update(self, delta_time):
        for v in self.vehicles:
            v.update()
        self.player.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = 5
        elif key == arcade.key.DOWN:
            self.player.change_y = -5
        elif key == arcade.key.LEFT:
            self.player.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player.change_x = 5

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.DOWN):
            self.player.change_y = 0
        elif key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0

def main():
    window = LondonLife()
    arcade.run()

if __name__ == "__main__":
    main()
