import configparser
import os.path
import os
import argparse

class Colors:
    def __init__(self, name, r, g, b):
        self.name = name
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"{self.name} ({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):
        if isinstance(other, Colors):
            return (self.r == other.r and
                    self.g == other.g and
                    self.b == other.b)
        return NotImplemented


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', nargs = '?', default='settings\settings.ini', help="Name of the settings file")
args = parser.parse_args()
print(args.file)

if os.path.isfile(args.file):
    config = configparser.ConfigParser()
    config.read(args.file, encoding="UTF-8")

    red_arr = config['COLORS']['RED'].split(', ')
    green_arr = config['COLORS']['GREEN'].split(', ')
    blue_arr = config['COLORS']['BLUE'].split(', ')

    red = Colors(red_arr[0], int(red_arr[1]),  int(red_arr[2]),  int(red_arr[3]))
    green = Colors(green_arr[0], int(green_arr[1]),  int(green_arr[2]),  int(green_arr[3]))
    blue = Colors(blue_arr[0], int(blue_arr[1]),  int(blue_arr[2]),  int(blue_arr[3]))

    f = open('instances.txt', 'w')
    f.write(str(red))
    f.write('\n')
    f.write(str(green))
    f.write('\n')
    f.write(str(blue))
    f.close

else:
    print('File not found')