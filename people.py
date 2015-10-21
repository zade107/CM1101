player_name = input("What is your name, detective?: ")

def get_player_name():
    return player_name

person_chief = {
    "name": "inspector",

    "description":
    """Inspecting the Inspector, huh?""",

    "speech":
    "Hello, Detective " + get_player_name() +"."
    
}

person_chef = {
    "name": "chef",
    
    "description":
    """Seems to be busy cooking up something good.
He doesn't notice you staring at him, you creep.""",
    
    "speech":
    get_player_name() + ", is there something you need?"
}

person_caretaker = {
    "name": "caretaker",
    
    "description":
    """Caretaker John has been working here for 15 years, 
    his shoes are as odd as his current mood.""",
    "speech":
    "Take this basement key, I think you may find it useful."
}

person_technician = {
    "name": "technician",
    
    "description":
    "Plain old Jane, the lab technician. Keeps the computers in working order.",
    
    "speech":
    """I know half of the CCTV access code, it's 04. You may find it useful.
I remember seeing the other half written down somewhere, but I can't seem to recall it, sorry!""" 
}