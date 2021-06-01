# Goal : A script that can be used to take images one folder which are in JPEG format, convert them into PNG format
# and put them into another folder through command line.
# Example usage : python3 JPGtoPNGConverter.py Pokedex\ newFolder

import sys
import os
from PIL import Image

# grab the first and second arguments using the sys module
input_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new folder exists, if not, create it.
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# loop through Pokedex
for filename in os.listdir(input_folder):
    img = Image.open(f'{input_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}\\{clean_name}{filename}', 'png')
    print('all done!')

