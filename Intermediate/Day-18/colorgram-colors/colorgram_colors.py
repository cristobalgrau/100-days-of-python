import colorgram
# documentation: https://pypi.org/project/colorgram.py/

# **************** CODE TO EXTRACT COLORS WITH COLORGRAM LIB ****************
def extract_rgb(color_palette):
    rgb = color_palette.rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    color_extracted = (red, green, blue)
    return color_extracted


colors_quantity = 10
colors = colorgram.extract('image.jpg', colors_quantity)

color_list = []
for index in range(colors_quantity):
    color_rgb = extract_rgb(colors[index])
    color_list.append(color_rgb)

print(color_list)
