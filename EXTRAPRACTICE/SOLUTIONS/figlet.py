import random
import sys

from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
elif len(sys.argv) == 3 and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

s = input("Input: ")
print("Output:")
print(figlet.renderText(s))
