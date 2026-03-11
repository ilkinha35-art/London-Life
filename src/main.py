import arcade
from game_logic import Vehicle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "London Life - Arcade"

class LondonLife(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Lista de veículos: carro, ônibus e caminhão
        self.vehicles = [
            Vehicle(100, 200, 80, 40, arcade.color.RED, 3),     # carro
            Vehicle(300, 300, 120, 50, arcade.color.BLUE, -2), # ônibus
            Vehicle(500, 400, 160, 60, arcade.color.GRAY, 2),  # caminhão
            Vehicle(200, 500, 80, 40, arcade.color.GREEN, 4),  # carro
        ]

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("London Life - Trânsito fluindo", 10, 570, arcade.color.BLACK, 20)
        # Desenha veículos
        for v in self.vehicles:
            v.draw()

    def on_update(self, delta_time):
        for v in self.vehicles:
            v.update()

def main():
    window = LondonLife()
    arcade.run()

if __name__ == "__main__":
    main()
