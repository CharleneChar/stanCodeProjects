"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This program lets user check rankings of babies' names
in specific years and displays the results in a line graph.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    total_width = width - 2 * GRAPH_MARGIN_SIZE
    # Calculate the same space distance between two vertical lines next to each other
    increment = total_width // len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * increment
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    # Delete all existing lines from the canvas
    canvas.delete('all')

    # Draw horizontal lines
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # Draw vertical lines and note years
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0,
                           get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    # Draw the fixed background grid
    draw_fixed_lines(canvas)

    # Calculate the scale used to fit all specific data
    # (esp. those that are above the canvas height but below the MAX_RANK)
    # into the graph
    scale = CANVAS_HEIGHT / MAX_RANK

    for i in range(len(lookup_names)):
        name = lookup_names[i]
        # Paint lines with a series of colors in turns
        color = COLORS[i % len(COLORS)]
        # Make sure data associated with the baby name entered exists
        if name in name_data:
            point_y = []
            for j in range(len(YEARS)):
                year = str(YEARS[j])
                # Determine which point on the vertical line to place the rank of the baby name
                # in the year and what should be noted next to the point besides the baby name
                if year not in name_data[name]:
                    point_y += [CANVAS_HEIGHT - GRAPH_MARGIN_SIZE]
                    text = str(name) + '*'
                else:
                    if int(name_data[name][year]) > MAX_RANK:
                        point_y += [CANVAS_HEIGHT - GRAPH_MARGIN_SIZE]
                        text = str(name) + '*'
                    else:
                        point_y += [GRAPH_MARGIN_SIZE + int(name_data[name][year]) * scale]
                        text = str(name) + ' ' + name_data[name][year]
                # Note the baby name and its rank (or other character representing rank beyond max)
                canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, j), point_y[j],
                                   text=text, anchor=tkinter.SW, fill=color)
            # Draw lines, each of which is between a rank at one year and a rank at the next year
            for j in range(len(YEARS)-1):
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), point_y[j],
                                   get_x_coordinate(CANVAS_WIDTH, j + 1), point_y[j + 1],
                                   width=LINE_WIDTH, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
