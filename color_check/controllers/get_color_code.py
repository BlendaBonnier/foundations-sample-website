# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.

import json

def get_color_code(color_name):
   #reading the data from the file and loop through and comapre keys with color_name
   try:
       color_name = color_name.lower().strip()
   except AttributeError:
        pass

   try:
        with open('color_check/data/css-color-names.json') as f:
            data = json.load(f)
            for key in data.keys():
                if color_name == key:
                    hex = data[key]
                    return hex
                    break
            color_hex_code = None
        return color_hex_code
   except FileNotFoundError: 
       return "File can not be found"
