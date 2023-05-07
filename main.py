import math
from statistics import median

import numpy as np
from PIL import Image as im
import matplotlib.pyplot as plt

#   Loading first picture
img1 = im.open("imag1.png").convert("RGB")
img1.resize((300, 300))

#   Loading second picture
img2 = im.open("imag2.jpg").convert("RGB")
img2.resize((300, 300))


def brightness(img, bright, powered):
    w, h = img.size
    mod_img = im.new('RGB', (w, h))
    for x in range(w):
        for y in range(h):
            r, g, b = img.getpixel((x, y))
            r /= 255
            g /= 255
            b /= 255

            if powered:
                r **= bright
                if r > 1: r = 1
                if r < 0: r = 0

                g **= bright
                if g > 1: g = 1
                if g < 0: r = 0

                b **= bright
                if b > 1: b = 1
                if b < 0: r = 0
            else:
                r *= bright
                if r > 1: r = 1
                if r < 0: r = 0

                g *= bright
                if g > 1: g = 1
                if g < 0: r = 0

                b *= bright
                if b > 1: b = 1
                if b < 0: r = 0

            r *= 255
            g *= 255
            b *= 255
            mod_img.putpixel((x, y), (int(r), int(g), int(b)))

    plt.imshow(mod_img)
    plt.show()


def negative(img):
    w, h = img.size
    mod_img = im.new('RGB', (w, h))
    for x in range(w):
        for y in range(h):
            r, g, b = img.getpixel((x, y))
            r = 255 - r
            g = 255 - g
            b = 255 - b
            mod_img.putpixel((x, y), (r, g, b))
    plt.imshow(mod_img)
    plt.show()


def contrast(img, hue):
    w, h = img.size
    mod_img = im.new('RGB', (w, h))
    for x in range(w):
        for y in range(h):
            r, g, b = img.getpixel((x, y))
            r_new = int((r - 128) * hue + 128)
            g_new = int((g - 128) * hue + 128)
            b_new = int((b - 128) * hue + 128)
            mod_img.putpixel((x, y), (r_new, g_new, b_new))
    plt.imshow(mod_img)
    plt.show()


def blending(img1, img2, blend):
    w, h = img1.size
    mod_img = im.new('RGB', (w, h))
    if blend == 1:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                r = min(r1 + r2, 255)
                g = min(g1 + g2, 255)
                b = min(b1 + b2, 255)
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 2:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                r = max(r1 + r2 - 1, 0)
                g = max(g1 + g2 - 1, 0)
                b = max(b1 + b2 - 1, 0)
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 3:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                r = abs(r1 - r2)
                g = abs(g1 - g2)
                b = abs(b1 - b2)
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 4:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                r = int(max(r1 * r2, 255) / 255)
                g = int(max(g1 * g2, 255) / 255)
                b = int(max(b1 * b2, 255) / 255)
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 5:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                r = int(255 - (255 - r1) * (1 - r2)) // 255
                g = int(255 - (255 - g1) * (1 - g2)) // 255
                b = int(255 - (255 - b1) * (1 - b2)) // 255
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 6:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                r = 255 - abs(255 - r1 - r2)
                g = 255 - abs(255 - g1 - g2)
                b = 255 - abs(255 - b1 - b2)
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 7:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                r = min(r1, r2)
                g = min(g1, g2)
                b = min(b1, b2)
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 8:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                r = max(r1, r2)
                g = max(g1, g2)
                b = max(b1, b2)
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 9:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                r = int(r1 + r2 - 2 * r1 * r2 / 255)
                g = int(g1 + g2 - 2 * g1 * g2 / 255)
                b = int(b1 + b2 - 2 * b1 * b2 / 255)
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 10:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                if (r1 / 255 < 0.5):
                    r = int(2 * r1 * r2 / 255)
                else:
                    r = int(255 - 2 * (255 - r1) * (255 - r2))
                if (g1 / 255 < 0.5):
                    g = int(2 * g1 * g2 / 255)
                else:
                    g = int(255 - 2 * (255 - g1) * (255 - g2))
                if (b1 / 255 < 0.5):
                    b = int(2 * b1 * b2 / 255)
                else:
                    b = int(255 - 2 * (255 - b1) * (255 - b2))
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 11:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                if (r2 / 255 < 0.5):
                    r = int(2 * r1 * r2 / 255)
                else:
                    r = int(255 - 2 * (255 - r1) * (255 - r2))
                if (g2 / 255 < 0.5):
                    g = int(2 * g1 * g2 / 255)
                else:
                    g = int(255 - 2 * (255 - g1) * (255 - g2))
                if (b2 / 255 < 0.5):
                    b = int(2 * b1 * b2 / 255)
                else:
                    b = int(255 - 2 * (255 - b1) * (255 - b2))
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 12:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                if (r1 / 255 < 0.5):
                    r = int((2 * r1 * r2 + pow(r1, 2) + (1 - 2 * r2)) / 255)
                else:
                    r = int((math.sqrt(r1) * (2 * r2 - 1) + (2 * r1) * (1 - r2)) / 255)
                if (g1 / 255 < 0.5):
                    g = int((2 * g1 * g2 + pow(g1, 2) + (1 - 2 * g2)) / 255)
                else:
                    g = int((math.sqrt(g1) * (2 * g2 - 1) + (2 * g1) * (1 - g2)) / 255)
                if (b1 / 255 < 0.5):
                    b = int((2 * b1 * b2 + pow(b1, 2) + (1 - 2 * b2)) / 255)
                else:
                    b = int((math.sqrt(b1) * (2 * b2 - 1) + (2 * b1) * (1 - b2)) / 255)
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 13:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                r = int(r1/(255-r2))
                g = int(g1/(255-g2))
                b = int(b1/(255-b2))
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 14:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                if r1 == 0 or g1 == 0 or b1 == 0 or r2==0 or b2==0 or g2==0:
                    r = r1
                    b = b1
                    g = g1
                else:
                    r = int(1 - (1 - r1) / r2)
                    g = int(1 - (1 - g1) / g2)
                    b = int(1 - (1 - b1) / b2)
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 15:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                r = int(pow(r1,2)/(255-r2))
                g = int(pow(g1,2)/(255-g2))
                b = int(pow(b1,2)/(255-b2))
                mod_img.putpixel((x, y), (r, g, b))
    elif blend == 16:
        for x in range(w):
            for y in range(h):
                r1, g1, b1 = img1.getpixel((x, y))
                r2, g2, b2 = img2.getpixel((x, y))
                r = int(0.5 * r2 + 0.5 * r1)
                g = int(0.5 * g2 + 0.5 * g1)
                b = int(0.5 * b2 + 0.5 * b1)
                mod_img.putpixel((x, y), (r, g, b))
    plt.imshow(mod_img)
    plt.show()


def edge(img, type):
    w, h = img.size
    mod_img = im.new('RGB', (w, h))
    if type == "rv":
        matrix = [[0, 0, 0], [0, 1, 0], [0, -1, 0]]
    elif type == "rh":
        matrix = [[0, 0, 0], [0, 1, -1], [0, 0, 0]]
    elif type == "pv":
        matrix = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
    elif type == "ph":
        matrix = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
    elif type == "sv":
        matrix = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    elif type == "sh":
        matrix = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
    elif type == "l":
        matrix = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            temp_r = 0
            temp_g = 0
            temp_b = 0

            for k in range(-1, 2):
                for l in range(-1, 2):
                    r, g, b = img.getpixel((i + k, j + l))
                    temp_r += r * matrix[k + 1][l + 1]
                    temp_g += g * matrix[k + 1][l + 1]
                    temp_b += b * matrix[k + 1][l + 1]
            mod_img.putpixel((i, j), (temp_r, temp_g, temp_b))
    plt.imshow(mod_img)
    plt.show()


def stat(img, type):
    w, h = img.size
    mod_img = im.new('RGB', (w, h))
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            static = []
            for k in range(-1, 2):
                for l in range(-1, 2):
                    static.append(img.getpixel((i + k, j + l)))
            if type == "min":
                nstatic = min(static)
            elif type == "max":
                nstatic = max(static)
            elif type == "med":
                nstatic = median(static)
            mod_img.putpixel((i, j), nstatic)
    plt.imshow(mod_img)
    plt.show()


def histogram(img):
    r, g, b = img.split()

    r_histogram = r.histogram()
    g_histogram = g.histogram()
    b_histogram = b.histogram()

    max_count = max(max(r_histogram), max(g_histogram), max(b_histogram))

    r_hist = [x / max_count * 200 for x in r_histogram]
    g_hist = [x / max_count * 200 for x in g_histogram]
    b_hist = [x / max_count * 200 for x in b_histogram]

    plt.plot(r_hist, color='red', label='Red Channel')
    plt.plot(g_hist, color='green', label='Green Channel')
    plt.plot(b_hist, color='blue', label='Blue Channel')
    plt.legend()
    plt.show()


# 1, 2)
# brightness(img1, 2, False) # (image.png, brightness multiplication, is powered?)
# negative(img1)
# contrast(img1, 3)

# 3)

# blending(img1, img2, 4) # (image1.png, image2.png, 1-16 types of blending

# 4)
# edge(img1, "ph")  # (image.png, (r - roberts, p - prewitt, l - laplace, v - vertival, h - horizontal, or s-sobel))
# eg. "ph" - horizontal prewitt method

# 5)
# stat(img1, "max")  # (image.png, (min, max, med))

# 6)
# histogram(img1)


# +   1. Linear (brightness, darkness, negative, contrast)
# +   2. Powered (brightness, darkness)
#    3. Blending (16 algorithms)
# +   4. Edge-detection (Roberts, Prewitt, Sobel)X(horizontal and vertical) + (Laplacian)
# +   5. Statistics (minimum, maximum, median)
# +   6. Histogram
