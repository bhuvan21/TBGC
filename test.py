import xml.etree.ElementTree as ET

from validation import validate_game
from Location import Location

print(validate_game())

game = ET.parse("game.xml")
root = Location(game.getroot()[0])
root.goto()