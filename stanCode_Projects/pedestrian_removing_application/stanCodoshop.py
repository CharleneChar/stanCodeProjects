"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
-----------------------------------------------
This program clears people as many as possible in a picture
through comparing pixels from a couple of pictures taken at the same place
,finding out color distance and coloring with RGB of the pixels with the smallest color distance.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    dist = int(((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**(1/2))
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    # rgb = [0, 0, 0]
    [r, g, b] = [0, 0, 0]
    for pix in pixels:
        # rgb[0] += pix.red
        # rgb[1] += pix.green
        # rgb[2] += pix.blue
        r += pix.red
        g += pix.green
        b += pix.blue
    # for i in range(len(rgb)):
    #     rgb[i] = rgb[i] // len(pixels)
    # return rgb
    return [e//len(pixels) for e in [r, g, b]]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    closet = float('inf')
    index = 0
    [r, g, b] = get_average(pixels)
    for i in range(len(pixels)):
        # dis = get_pixel_dist(pixels[i], get_average(pixels)[0], get_average(pixels)[1], get_average(pixels)[2])
        dis = get_pixel_dist(pixels[i], r, g, b)
        if dis < closet:
            closet = dis
            index = i
    best = pixels[index]
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # Populate image and create the 'ghost' effect
    for i in range(width):
        for j in range(height):
            img_pixels = []
            # Get pixel in the same position in each image from a list of images to create lists of pixels
            for image in images:
                img_pixels.append(image.get_pixel(i, j))
            # Use RGB of the pixels with the smallest color distance to color the result
            pigment = get_best_pixel(img_pixels)
            canvas = result.get_pixel(i, j)
            canvas.red = pigment.red
            canvas.green = pigment.green
            canvas.blue = pigment.blue
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    """
    Clear people in images given and show the cleared image
    """
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
