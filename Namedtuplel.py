from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 150, 250)

print (color.red)