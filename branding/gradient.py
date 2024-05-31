from PIL import Image, ImageDraw
import numpy as np

def interpolate_color(color1, color2, ratio):
    return tuple(int(c1 + (c2 - c1) * ratio) for c1, c2 in zip(color1, color2))

def generate_gradient(width, height, color_tl, color_tr, color_bl, color_br, output_file):
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    for y in range(height):
        for x in range(width):
            ratio_x = x / (width - 1)
            ratio_y = y / (height - 1)
            color_top = interpolate_color(color_tl, color_tr, ratio_x)
            color_bottom = interpolate_color(color_bl, color_br, ratio_x)
            color = interpolate_color(color_top, color_bottom, ratio_y)
            draw.point((x, y), fill=color)

    img.save(output_file, 'PNG')

if __name__ == '__main__':
    width = 400
    height = 400
    color_tl = (198, 252, 187)   # #C6FCBB
    color_tr = (247, 243, 157)   # #F7F39D
    color_bl = (180, 178, 255)   # #B4B2FF
    color_br = (231, 163, 232)   # #E7A3E8
    output_file = 'gradient.png'

    generate_gradient(width, height, color_tl, color_tr, color_bl, color_br, output_file)
