import json

from PIL import Image


# Reads an image and translates it to a world map in world.json
def generate_world():
    map_image = Image.open('world.png', 'r') # Must be a square image
    world_width = 1000  # Set this to the size of the map being generated, should match the pixel width of the image
    pixels = list(map_image.getdata())
    row = []
    world = []
    for pixel_enum in enumerate(pixels):
        pixel = pixel_enum[1]
        pixel_total = pixel[0]+pixel[1]+pixel[2]
        if pixel_total <= 50:
            output = 2
        elif 51 <= pixel_total <= 400:
            if 300 < pixel_total < 350:
                output = 3
            else:
                output = 1
        elif 400 <= pixel_total < 550:
            output = 4
        else:
            output = 0
        row.append(output)
        if len(row) % world_width == 0:
            world.append(row)
            row = []

    output = open('../world.json', 'w')
    json.dumps(world)
    output.write(world.__str__())
    print('Finished generating world.json file.')


generate_world()
