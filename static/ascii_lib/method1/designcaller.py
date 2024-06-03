"""
Call by Name: Use the dictionary to access and call specific functions like this:

drawing_functions["house"]()
"""

import random
from testascii import Canvas

class CanvasManager(Canvas):
    def get_drawing_functions(self):
        """Returns a dictionary mapping drawing function names to the functions themselves."""
        return {
            "horse": self.draw_horse,
            "rabbit": self.draw_rabbit,
            "house": self.draw_house,
            "cat": self.draw_cat,
            "dog": self.draw_dog,
            "tree": self.draw_tree,
            "car": self.draw_car,
            "sun": self.draw_sun,
            "cloud": self.draw_cloud,
            "star": self.draw_star,
            "heart": self.draw_heart,
            "smiley": self.draw_smiley,
            "fish": self.draw_fish,
            "bird": self.draw_bird,
            "butterfly": self.draw_butterfly,
            "moon": self.draw_moon,
            "mountain": self.draw_mountain,
            "river": self.draw_river,
            "boat": self.draw_boat,
            "plane": self.draw_plane,
            "flower": self.draw_flower,
            "mushroom": self.draw_mushroom,
        }

if __name__ == "__main__":
    canvas_manager = CanvasManager()
    drawing_functions = canvas_manager.get_drawing_functions()

    while True:
        canvas_manager.clear_canvas()

        # Example 1: Draw all figures
        # canvas_manager.draw_all() 

        # Example 2: Draw specific figures by name
        figures_to_draw = ["horse", "sun", "cloud"]
        for figure in figures_to_draw:
            if figure in drawing_functions:
                drawing_functions[figure]()
            else:
                print(f"Invalid figure: {figure}")

        # Example 3: Draw a random subset of figures
        # random_figures = random.sample(list(drawing_functions.keys()), 3)
        # for figure in random_figures:
        #     drawing_functions[figure]()

        canvas_manager.render_canvas()
        input("Press Enter for new art, or type 'q' to quit: ")
        if input().lower() == 'q':
            break
