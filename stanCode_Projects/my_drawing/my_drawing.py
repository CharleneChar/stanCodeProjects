"""
File: My Drawing
Name: Charlene
----------------------
This file displays a drawing similar to an aeriel image of Taiwan in a window,
and when clicking on specific bottoms on the top left corner of the map,
some pictures of recommended food and places will randomly pop up near the region
where we can find them (like the northern, middle, or southern region).
PS Pictures downloaded from the Internet are used only for homework and won't be used for commercial use.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel
from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
import random

# The following creates a window called my_drawing.py
window = GWindow(700, 700, title='my_drawing.py')
# The following controls whether to display an image
no_eat_image = True
no_go_image = True
# The following determines which picture to display
random_img_eat = -1
random_img_place = -1


def main():
    """
    - Feeling lazy or tired of planning a trip?
    - This program makes decisions for hesitant people
      by randomly picking what to eat and where to go in Taiwan for a user
      when they click on the top left bottoms in the window.
    - With the first click, a picture will pop up,
      and with the second click, the picture will get cleared,
      and with the third click, a picture (which might be the same as or different than the first one)
      will pop up.
    """
    background = GRect(700, 700)
    background.filled = True
    background.fill_color = 'lightblue'
    window.add(background)
    button_eat()
    button_place()
    taiwan()
    mountain()
    waves()
    onmouseclicked(change)


def change(m):
    # The following declares the global variables
    global no_eat_image, no_go_image, random_img_eat, random_img_place
    # The following shows what to eat by displaying a random food picture
    if m.x < 60 and m.y < 60:
        if no_eat_image:
            # The following images are food that user can find in the northern region
            image_a = GImage('brunch.jpg')
            image_b = GImage('dim_sum.jpg')
            # The following images are food that user can find in the middle region
            image_c = GImage('hotpot.jpg')
            image_d = GImage('grill.jpg')
            # The following images are food that user can find in the southern region
            image_e = GImage('drink.jpg')
            image_f = GImage('sashimi.jpg')
            random_img_eat = random.randrange(0, 6, 1)
            if random_img_eat == 0:
                window.add(image_a, 160, 40)
            elif random_img_eat == 1:
                window.add(image_b, 160, 40)
            elif random_img_eat == 2:
                window.add(image_c, 50, 200)
            elif random_img_eat == 3:
                window.add(image_d, 50, 200)
            elif random_img_eat == 4:
                window.add(image_e, 80, 500)
            elif random_img_eat == 5:
                window.add(image_f, 80, 500)
            no_eat_image = False
        else:
            if random_img_eat == 0:
                clear_eat = window.get_object_at(160, 40)
                if clear_eat is not None:
                    window.remove(clear_eat)
            elif random_img_eat == 1:
                clear_eat = window.get_object_at(160, 40)
                if clear_eat is not None:
                    window.remove(clear_eat)
            elif random_img_eat == 2:
                clear_eat = window.get_object_at(50, 200)
                if clear_eat is not None:
                    window.remove(clear_eat)
            elif random_img_eat == 3:
                clear_eat = window.get_object_at(50, 200)
                if clear_eat is not None:
                    window.remove(clear_eat)
            elif random_img_eat == 4:
                clear_eat = window.get_object_at(80, 500)
                if clear_eat is not None:
                    window.remove(clear_eat)
            elif random_img_eat == 5:
                clear_eat = window.get_object_at(80, 500)
                if clear_eat is not None:
                    window.remove(clear_eat)
            no_eat_image = True
    # The following shows where to go by displaying a random place picture
    elif 60 <= m.x < 120 and m.y < 60:
        if no_go_image:
            # The following images are places that user can find in the northern region
            image_a = GImage('amusement_park.jpg')
            image_b = GImage('zoo.jpg')
            # The following images are places that user can find in the middle region
            image_c = GImage('roller_skating.jpg')
            image_d = GImage('mountain.jpeg')
            # The following images are places that user can find in the southern region
            image_e = GImage('beach.jpg')
            image_f = GImage('aquarium.jpg')
            random_img_place = random.randrange(0, 6, 1)
            if random_img_place == 0:
                window.add(image_a, 500, 110)
            elif random_img_place == 1:
                window.add(image_b, 500, 110)
            elif random_img_place == 2:
                window.add(image_c, 480, 280)
            elif random_img_place == 3:
                window.add(image_d, 480, 280)
            elif random_img_place == 4:
                window.add(image_e, 450, 520)
            elif random_img_place == 5:
                window.add(image_f, 450, 520)
            no_go_image = False
        else:
            if random_img_place == 0:
                clear_go = window.get_object_at(500, 110)
                if clear_go is not None:
                    window.remove(clear_go)
            elif random_img_place == 1:
                clear_go = window.get_object_at(500, 110)
                if clear_go is not None:
                    window.remove(clear_go)
            elif random_img_place == 2:
                clear_go = window.get_object_at(480, 280)
                if clear_go is not None:
                    window.remove(clear_go)
            elif random_img_place == 3:
                clear_go = window.get_object_at(480, 280)
                if clear_go is not None:
                    window.remove(clear_go)
            elif random_img_place == 4:
                clear_go = window.get_object_at(450, 520)
                if clear_go is not None:
                    window.remove(clear_go)
            elif random_img_place == 5:
                clear_go = window.get_object_at(450, 520)
                if clear_go is not None:
                    window.remove(clear_go)
            no_go_image = True


def taiwan():
    """
    The function creates and displays Taiwan in the window.
    """
    # The following uses several triangles to build up a simple image of Taiwan
    block_a = GPolygon()
    block_a.add_vertex((330, 120))
    block_a.add_vertex((450, 50))
    block_a.add_vertex((490, 75))
    window.add(block_a)
    block_b = GPolygon()
    block_b.add_vertex((330, 120))
    block_b.add_vertex((500, 140))
    block_b.add_vertex((490, 75))
    window.add(block_b)
    block_c = GPolygon()
    block_c.add_vertex((490, 75))
    block_c.add_vertex((520, 80))
    block_c.add_vertex((525, 110))
    window.add(block_c)
    block_d = GPolygon()
    block_d.add_vertex((490, 75))
    block_d.add_vertex((500, 140))
    block_d.add_vertex((525, 110))
    window.add(block_d)
    block_e = GPolygon()
    block_e.add_vertex((330, 120))
    block_e.add_vertex((180, 330))
    block_e.add_vertex((500, 140))
    window.add(block_e)
    block_f = GPolygon()
    block_f.add_vertex((485, 250))
    block_f.add_vertex((180, 330))
    block_f.add_vertex((500, 140))
    window.add(block_f)
    block_g = GPolygon()
    block_g.add_vertex((485, 250))
    block_g.add_vertex((510, 170))
    block_g.add_vertex((500, 140))
    window.add(block_g)
    block_h = GPolygon()
    block_h.add_vertex((485, 250))
    block_h.add_vertex((510, 170))
    block_h.add_vertex((505, 220))
    window.add(block_h)
    block_i = GPolygon()
    block_i.add_vertex((180, 330))
    block_i.add_vertex((485, 250))
    block_i.add_vertex((175, 470))
    window.add(block_i)
    block_j = GPolygon()
    block_j.add_vertex((175, 470))
    block_j.add_vertex((485, 250))
    block_j.add_vertex((470, 410))
    window.add(block_j)
    block_k = GPolygon()
    block_k.add_vertex((175, 470))
    block_k.add_vertex((470, 410))
    block_k.add_vertex((410, 510))
    window.add(block_k)
    block_l = GPolygon()
    block_l.add_vertex((175, 470))
    block_l.add_vertex((410, 510))
    block_l.add_vertex((220, 540))
    window.add(block_l)
    block_m = GPolygon()
    block_m.add_vertex((410, 510))
    block_m.add_vertex((220, 540))
    block_m.add_vertex((300, 580))
    window.add(block_m)
    block_n = GPolygon()
    block_n.add_vertex((410, 510))
    block_n.add_vertex((300, 580))
    block_n.add_vertex((370, 640))
    window.add(block_n)
    block_a.color = block_b.color = block_c.color = block_d.color\
        = block_e.color = block_f.color = block_g.color = block_h.color\
        = block_i.color = block_j.color = block_k.color = block_l.color\
        = block_m.color = block_n.color = 'darkseagreen'
    block_a.filled = block_b.filled = block_c.filled = block_d.filled\
        = block_e.filled = block_f.filled = block_g.filled = block_h.filled\
        = block_i.filled = block_j.filled = block_k.filled = block_l.filled\
        = block_m.filled = block_n.filled = True
    block_a.fill_color = block_b.fill_color = block_c.fill_color = block_d.fill_color\
        = block_e.fill_color = block_f.fill_color = block_g.fill_color = block_h.fill_color\
        = block_i.fill_color = block_j.fill_color = block_k.fill_color = block_l.fill_color\
        = block_m.fill_color = block_n.fill_color = 'darkseagreen'


def mountain():
    """
    The function creates and displays mountains as a whole in the window.
    """
    # The following uses a triangle to draw a simple image of mountains as a whole
    block_a = GPolygon()
    block_a.add_vertex((430, 120))
    block_a.add_vertex((380, 350))
    block_a.add_vertex((280, 520))
    window.add(block_a)
    block_a.color = 'darkkhaki'
    block_a.filled = True
    block_a.fill_color = 'darkkhaki'


def waves():
    """
    The function creates and displays waves in two places in the window.
    """
    # The following uses several triangles to draw simple images of wave in two places
    block_a = GPolygon()
    block_a.add_vertex((100, 180))
    block_a.add_vertex((125, 170))
    block_a.add_vertex((125, 160))
    window.add(block_a)
    block_b = GPolygon()
    block_b.add_vertex((150, 180))
    block_b.add_vertex((125, 170))
    block_b.add_vertex((125, 160))
    window.add(block_b)
    block_c = GPolygon()
    block_c.add_vertex((550, 520))
    block_c.add_vertex((575, 510))
    block_c.add_vertex((575, 500))
    window.add(block_c)
    block_d = GPolygon()
    block_d.add_vertex((600, 520))
    block_d.add_vertex((575, 510))
    block_d.add_vertex((575, 500))
    window.add(block_d)
    block_a.color = block_b.color = block_c.color = block_d.color = 'white'
    block_a.filled = block_b.filled = block_c.filled = block_d.filled = True
    block_a.fill_color = block_b.fill_color = block_c.fill_color = block_d.fill_color = 'white'


def button_eat():
    """
    The function creates and displays a pink bottom for generating result of food to eat in the window.
    """
    # The following uses a circle to draw a pink bottom
    circle = GOval(50, 50)
    window.add(circle, 10, 10)
    circle.color = 'darksalmon'
    circle.fill_color = 'darksalmon'
    eat_label = GLabel('EAT')
    eat_label.font = '-11'
    eat_label.color = 'white'
    click_label = GLabel('CLICK')
    click_label.font = '-11'
    click_label.color = 'white'
    emoji_me = GLabel('⁎˃◡˂⁎')
    emoji_me.font = '-16'
    emoji_me.color = 'white'
    window.add(eat_label, 25, eat_label.height + 17)
    window.add(click_label, 20, click_label.height + 29)
    window.add(emoji_me, 20, emoji_me.height + 41)


def button_place():
    """
    The function creates and displays a grey bottom for generating result of place to go in the window.
    """
    # The following uses a circle to draw a grey bottom
    circle = GOval(50, 50)
    window.add(circle, 10+60, 10)
    circle.color = 'dimgrey'
    circle.fill_color = 'dimgrey'
    go_label = GLabel('GO')
    go_label.font = '-11'
    go_label.color = 'white'
    click_label = GLabel('CLICK')
    click_label.font = '-11'
    click_label.color = 'white'
    emoji_me = GLabel('⁎❛ᴗ❛⁎')
    emoji_me.font = '-14'
    emoji_me.color = 'white'
    window.add(go_label, 87, go_label.height + 17)
    window.add(click_label, 80, click_label.height + 29)
    window.add(emoji_me, 78, emoji_me.height + 41)


if __name__ == '__main__':
    main()
