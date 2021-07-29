"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""

from simpleimage import SimpleImage

# The constant below controls the precision of green color.
THRESHOLD = 1.052

# The constant below controls the precision of black color.
BLACK_PIXEL = 230


def main():
    """
    -This photo is created based on the idea of
     attempting to distract focus from my self image xD,
     as well as providing fun looking for Wally with MASK!
    -The way to do it is to combine two images in one 
     and display the combined image.
    """
    selfie = SimpleImage('image_contest/self.jpg')
    background = SimpleImage('image_contest/find_wally_bg1.jpeg')
    product = integration(selfie, background)
    product.show()


def integration(figure, picture):
    """
    :param figure: SimpleImage, data of original image to be treated as pigment for a new combined image.
    :param picture: SimpleImage, data of original image where some part is to be maintained on a new canvas.
    :return figure: SimpleImage, data of combined image.
    """
    # Align the size of two images.
    picture.make_as_big_as(figure)

    for x in range(figure.width):
        for y in range(picture.height):

            # Get pixel from the one of the image.
            self_img = figure.get_pixel(x, y)

            # Get pigment from the other image.
            bg_img = picture.get_pixel(x, y)

            total = self_img.red + self_img.green + self_img.blue

            # The following determines which pixel is counted as green color
            # and replaces it with pigment got from the above.
            if self_img.green > total // 3 * THRESHOLD and total > BLACK_PIXEL:
                self_img.red = bg_img.red
                self_img.green = bg_img.green
                self_img.blue = bg_img.blue

    return figure


if __name__ == '__main__':
    main()
