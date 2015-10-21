from items import *
from map import rooms

inventory = [item_money, item_badge, item_magnifying_glass]
# Start game at the reception
current_room = rooms["Parking"]

def current_carry(inventory):
    sum_mass = 0.0
    for item in inventory:
        sum_mass = sum_mass + item["mass"]
    return sum_mass