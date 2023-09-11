import colorgram 

colors = colorgram.extract('Day 18\Painting Project\painting.jpg',38)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))
   


print(rgb_colors)