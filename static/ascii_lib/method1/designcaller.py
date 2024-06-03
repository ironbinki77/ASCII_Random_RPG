"""
Call by Name: Use the dictionary to access and call specific functions like this:

drawing_functions["house"]()
"""

import random
from testasciigen import Canvas  # Assuming testasciigen.py is in the same directory

if __name__ == "__main__":
    canvas = Canvas()  # Create an instance of the Canvas class from testasciigen.py
    drawing_functions = canvas.get_drawing_functions()

    while True:
        canvas.clear_canvas()

        # Example 1: Draw all figures
        # canvas.draw_all() 

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

        canvas.render_canvas()
        input("Press Enter for new art, or type 'q' to quit: ")
        if input().lower() == 'q':
            break