#!/usr/bin/python3
import time
from map import rooms
from player import *
from items import *
from gameparser import *
from people import *
input_counter = 0
event_inspector = False
event_lecture = False
event_basement = False
cctv_code = "0451"
code_correct = False


def list_of_items(items):
    item_list = ""
    item_count = len(items)
    for item in items:
        if (item_count > 1):
            item_list = item_list + item["name"] + ", "
            item_count -= 1
        else:
            item_list = item_list + item["name"]
    return item_list

def print_room_items(room):
    items_room = room["items"]
    x = list_of_items(items_room)
    if x != "":
        print("You can see: " + x + ".")
        
def print_room_people(room):
    global current_room
    Found = False
    for people in current_room["people"]:
        if people["name"] != "":
            Found = True
            break
    if Found == True:
        print("The " + people["name"].upper() + " is here.")
    else:
        print("There is no one here.")

def print_inventory_items(items):
    pass
    x = list_of_items(inventory)
    if x != "":
        print("You have: " + x + ".")
        print()
    else:
        print("Your inventory is empty.")

def print_room(room):
    # Display room name
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()
    print_room_items(room)
    print()
    print_room_people(room)
    print()

def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items):
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    print("What do you want to do?")

def help():
    print("HELP: Display this menu.")
    print("INVENTORY: Display your inventory items.")
    print("TAKE: Take an item from the room.")
    print("DROP: Place an item from your inventory into the room.")
    print("INSPECT: Check the description of a person.")
    print("EXAMINE: Check the description of an item.")
    print("TALK: Talk to a person in your current room.")
    print("COMBINE: Use two items to accomplish a purpose. (Use the separator word 'and' e.g. combine x and y)")
    print("INPUTCOUNT: Check how many inputs you've made (includes unaccepted commands!)")
#    print("TIME: Check how long you've been playing.")
    print("TRY: Enter a code. (Only works in a specific room.)")
    print("There is a weight limit of 5kg.")
    
def input_count(input_counter):
    print("Input count: ", input_counter)
    
def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits

def execute_go(direction):
    global current_room
    if is_valid_exit(current_room["exits"], direction):
        if (current_room["exits"][direction] == "Lab") and (event_inspector == False):  
            print("You need an ID card to access the lab.") 
        elif (current_room["exits"][direction] == "Basement") and (event_basement == False):
            print("You need the basement key.")
        else:
            current_room = rooms[current_room["exits"][direction]]
            return current_room
    else:
        print("You cannot go there.")

def execute_take(item_id):
    pass
    Found = False
    for item in current_room["items"]:
        if item["id"] == item_id:
            Found = True
            break
    if Found == True:
        if (current_carry(inventory) + item["mass"]) > 5:
            print("You're carrying too much! Try dropping some items.")
            print("You're currently carrying " + str(format(current_carry(inventory), '.3f')) + "kg.")
        else:
            inventory.append(item)
            current_room["items"].remove(item)
            print_inventory_items(inventory)
    else:
        print("You cannot take that.")

def execute_drop(item_id):
    pass
    Found = False
    for item in inventory:
        if (item["id"] == item_id) and item_id != "id":
            Found = True
            break
    if Found == True:    
        current_room["items"].append(item)
        inventory.remove(item)
        print_inventory_items(inventory)
    else:
        print("You cannot drop that.")
        
def execute_examine(item_id):
    Found = False
    for item in inventory:
        if item["id"] == item_id:
            Found = True
            break
    if Found == True:
        print(item["description"])
    else:
        print("You cannot examine that.")
        
def execute_inspect(person_name):
    Found = False
    for people in current_room["people"]:
        if people["name"] == person_name:
            Found = True
            break
    if Found == True:
        print(people["description"])
    else:
        print("Who are you inspecting?")
            
def execute_talk(person_name):
    global event_inspector
    Found = False
    for people in current_room["people"]:
        if people["name"] == person_name:
            Found = True
            break
    if (((Found == True) and (person_name == "inspector")) and (event_inspector == False)):
        print("Hello, Detective " + get_player_name() +", you can use this ID card to access the lab.")
        print("(The chief gave you an ID card.)")
        inventory.append(item_id)
        event_inspector = True
    elif (Found == True):
        print(people["speech"])
    else:
        print("Who are you talking to?")
        
def execute_try(cctv):
    if current_room["name"] == "Security Room":
        if (cctv == cctv_code):
            code_correct = True
        else:
            print("CODE INVALID, PLEASE TRY AGAIN.")
            code_correct = False
        if code_correct == True:
            #add caretaker to lab
            print("""The code was accepted. Rewinding the footage, you can see Kirill's body being taken to the basement.
You hear a noise coming from the lab behind you.""")
    else:
        print("You're in the wrong room for this command.")

def execute_combine(item_id1, item_id2): 
    if (("lighter" and "cigarettes") in (item_id1 + item_id2)):
        for item in inventory:
            if item["id"] == "lighter":
                for item in inventory:
                    if item["id"] == "cigarettes":
                        inventory.remove(item_cigarettes)
                        print("You light up a few cigarettes and hold them below the alarm, triggering it and overriding the automatically locked door. Nice job!")
                        current_room["description"] = "There's nothing useful around here. The fire alarm is starting to hurt your ears."
                        current_room["exits"].update({"east":"Andrew Jones' office"})
                        rooms["Andrew Jones' office"]["people"].append(person_technician)
                        rooms["Matts office"]["items"].append(item_cctv_note)
                        break
    elif (("batteries" and "flashlight") in (item_id1 + item_id2)):
        for item in inventory:
            if item["id"] == "batteries":
                for item in inventory:
                    if item["id"] == "flashlight":
                        inventory.remove(item_batteries)
                        inventory.remove(item_flashlight)
                        print("You made a working flashlight!")
                        inventory.append(item_working)
                        #make basement enterable
                        break                       
    else:
        print("You cannot seem to combine these items.")
        
def execute_command(command):
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
            
    elif command[0] == "examine":
        if len(command) > 1:
            execute_examine(command[1])
        else:
            print("Examine what?")
    
    elif command[0] == "inspect":
        if len(command) > 1:
            execute_inspect(command[1])
        else:
            print("Inspect what?")
    elif command[0] == "help":
        help()
        
    elif command[0] == "inventory":
        print_inventory_items(inventory)
        
    elif command[0] == "inputcount":
        input_count(input_counter)
        
    elif command[0] == "talk":
        if len(command) > 1:
            execute_talk(command[1])
        else:
            print("Talk to who?")
            
    elif command[0] == "combine":
        if len(command) == 4:
            execute_combine(command[1],command[3])
        else:
            print("Use the following form: 'combine x and y'")
            
    elif command[0] == "try":
        if len(command) > 1:
            execute_try(command[1])
        else:
            print("Try what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    print_menu(exits, room_items, inv_items)
    user_input = input("> ")
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input

def move(exits, direction):
    return rooms[exits[direction]]

def main():
    global input_counter
    print(" _    _ _   _ _____   _   _______ _     _     ___________   _   _____________ _____ _     _    ___")  
    print("| |  | | | | |  _  | | | / |_   _| |   | |   |  ___|  _  \ | | / |_   _| ___ |_   _| |   | |  |__ \\")
    print("| |  | | |_| | | | | | |/ /  | | | |   | |   | |__ | | | | | |/ /  | | | |_/ / | | | |   | |     ) |")
    print("| |/\| |  _  | | | | |    \  | | | |   | |   |  __|| | | | |    \  | | |    /  | | | |   | |    / /")
    print("\  /\  | | | \ \_/ / | |\  \_| |_| |___| |___| |___| |/ /  | |\  \_| |_| |\ \ _| |_| |___| |___|_|")
    print(" \/  \/\_| |_/\___/  \_| \_/\___/\_____\_____\____/|___/   \_| \_/\___/\_| \_|\___/\_____\_____(_) ")
    print("Welcome to 'Who Killed Kirill?', type help (or HELP) for some ideas.")
    while True:
        print_room(current_room)
        command = menu(current_room["exits"], current_room["items"], inventory)
        execute_command(command)
        input_counter += 1
            
if __name__ == "__main__":
    main()