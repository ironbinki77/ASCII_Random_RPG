import random

class Canvas:
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.canvas = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def render_canvas(self):
        for row in self.canvas:
            print("".join(row))

    def draw_cat(self):
        cat_art = [
            " /\\___/\\",
            " (=' w '=)",
            " (\\( )/)",
            "  \\__/",
        ]
        self._draw_art(cat_art)

    def draw_dog(self):
        dog_art = [
            " __",
            "U^..^U",
            " /____\\",
            "/______\\",
        ]
        self._draw_art(dog_art)

    def draw_tree(self):
        tree_art = [
            "  /\\ ",
            " /  \\ ",
            " /____\\ ",
            "  ||",
        ]
        self._draw_art(tree_art)

    def draw_car(self):
        car_art = [
            "   _",
            " ____| |____",
            "O  _|_  O",
            "'-'--' '--'--'",
        ]
        self._draw_art(car_art)

    def draw_sun(self):
        sun_art = [
            "  \\  /  ",
            "  .-.  ",
            " ---(-)----",
            "  '-'  ",
            "  /  \\  ",
        ]
        self._draw_art(sun_art)

    def draw_cloud(self):
        cloud_art = [
            "  ____  ",
            " _(  )_ ",
            " (__   __)",
            "(____  ____)",
        ]
        self._draw_art(cloud_art)

    def draw_star(self):
        star_art = [
            "  *  ",
            "  ***  ",
            " ***** ",
            "*******",
            " ***** ",
            "  ***  ",
            "  *  ",
        ]
        self._draw_art(star_art)

    def draw_heart(self):
        heart_art = [
            " *** ",
            " ***** ",
            "*******",
            " ***** ",
            " *** ",
            "  *  ",
        ]
        self._draw_art(heart_art)

    def draw_smiley(self):
        smiley_art = [
            "  ____  ",
            " |  | ",
            " | :) | ",
            " |____| ",
        ]
        self._draw_art(smiley_art)

    def draw_fish(self):
        fish_art = [
            "  ><(((('>",
            " <'  -  '>",
            "  ><)))'>",
        ]
        self._draw_art(fish_art)

    def draw_bird(self):
        bird_art = [
            " ___",
            " ('v')",
            "((___))",
            " ^^ ",
        ]
        self._draw_art(bird_art)

    def draw_butterfly(self):
        butterfly_art = [
            "  \\ /  ",
            "  \\|/  ",
            " --o*o--",
            "  /|\\  ",
            "  \\/  ",
        ]
        self._draw_art(butterfly_art)

    def draw_moon(self):
        moon_art = [
            "  ** ",
            " *  * ",
            "*   *",
            " *  * ",
            "  ** ",
        ]
        self._draw_art(moon_art)

    def draw_mountain(self):
        mountain_art = [
            "  /\\  ",
            "  /  \\  ",
            " / /\\ \\ ",
            " /_/  \\_\\",
        ]
        self._draw_art(mountain_art)

    def draw_river(self):
        river_art = [
            "~~~~~~~~~",
            "~    ~",
            "~~~~~~~~~",
        ]
        self._draw_art(river_art)

    def draw_boat(self):
        boat_art = [
            "  |__| ",
            " \\____/ ",
            "~~~~~~~~~",
        ]
        self._draw_art(boat_art)

    def draw_plane(self):
        plane_art = [
            "   * ",
            "  /|\\",
            "===*---*",
            "  | ",
            "  / \\",
        ]
        self._draw_art(plane_art)

    def draw_flower(self):
        flower_art = [
            "  .  ",
            "  \\|/ ",
            " --@--",
            "  /|\\ ",
            "  | | ",
        ]
        self._draw_art(flower_art)

    def draw_mushroom(self):
        mushroom_art = [
            "  __ ",
            " _||_|_",
            " |_| |_|"
        ]
        self._draw_art(mushroom_art)

    def _draw_art(self, art):
        start_x = random.randint(0, self.width - len(art[0]))
        start_y = random.randint(0, self.height - len(art))
        for i, line in enumerate(art):
            for j, char in enumerate(line):
                if start_x + j < self.width and start_y + i < self.height:  
                    self.canvas[start_y + i][start_x + j] = char

    def clear_canvas(self):
        self.canvas = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def draw_all(self):
        self.draw_horse()
        self.draw_rabbit()
        self.draw_house()

if __name__ == "__main__":
    canvas = Canvas()  # Default size is now 30x20

    while True:
        canvas.clear_canvas()
        canvas.draw_all() 
        canvas.render_canvas()
        input("Press Enter for new art, or type 'q' to quit: ")
        if input().lower() == 'q':
            break

