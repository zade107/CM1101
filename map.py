from items import *
from people import *

room_reception = {
    "name": "Reception",

    "description":
    """The computers are on and emails have been left open.
There's a bunch of keys lying on the desk.
You also notice a small pool of blood on the stairs.""",

    "exits": {"up": "Lab", "east": "Cafe", "down": "Basement"},

    "items": [item_pen, item_batteries],
    
    "people": [person_chief]
}

room_cafe = {
    "name": "Cafe",

    "description":
    """This room is a mess! Tables, chairs and cutlery everywhere. 
In amongst the clutter you spot a clump of hair, it is short and dark.
You can tell that the victim was here.""",

    "exits":  {"west": "Reception", "north": "Kitchen"},

    "items": [item_biscuits, item_walking_stick],
    
    "people": [person_chef]

}

room_kitchen = {
    "name": "Kitchen",
    
    "description":
    """The kitchen seems deserted, there are the remains of some unidentifiable food.
Your stomach grumbles.""",
    
    "exits": {"south": "Cafe"},
    
    "items": [item_poison],

    "people": []

}

room_lab = {
    "name": "Lab",

    "description":
    """You enter the lab where the murder is suspected to have taken place. 
There is blood splattered on the glass windows.""",

    "exits": {"down": "Reception", "west": "Andrew Jones' office", "east": "Matts office", "north": "Security Room"},

    "items": [item_handbook, item_deodorant],

    "people": []

}

room_parking = {
    "name": "the parking lot",

    "description":
    """A bitter Tuesday, early morning, you have been called in to investigate the murder of a lecturer.
You are outside, alone in the car park. The solitude is interrupted by the chief, calling you from the reception.""",
    "exits": {"east": "Reception"},
    "items": [],

    "people": []

}

room_matts_office = {
    "name": "Matt's office",

    "description":
    """The door is slightly ajar, the lights are on but no one is around.
There is a desk and a filing cabinet. You see an open bag...""",

    "exits": {"west": "Lab"},

    "items": [item_nail_polish, item_heels],

    "people": []

}

room_lecture_theatre = {
    "name": "Lecture Theatre",

    "description":
    """This room is cold and dim. The automated door slams shut, locked behind you. 
You notice a fire alarm on the wall, but there seems to be no way out.""",

#    """You are in a run down lecture theatre, it is cold and dark.
#    There is a desk and a set of drawers. Nothing particularly useful here."""
    "exits": {},

    "items": [item_lighter, item_cigarettes],

    "people": []    
}

room_andrews_office = {
    "name": "Andrew Jones' office",

    "description":
    """All of the windows are open. Various papers are scattered on the floor and 
there's a half eaten sandwich on the desk.""",

    "exits": {"west": "Lecture Theatre", "east": "Lab"},

    "items": [item_laptop, item_tie],

    "people": []
}

room_basement = {
    "name": "Basement",
#if !flashlightwithbatteries 
#    "description":
#    """You open the basement door, it's too dark to see and the lights don't work. 
#    You need to find a source of light and then come back.""",
#else if have flashlight with batteries
    "description":
    """After pushing a heavy door open you are in a dark and damp room filled with clutter,
all you see is old computer equipment and various tools.
You then notice another door in front of you, but it's locked.""",
    "exits": {"up": "Reception", "north":"Inner Basement"}, 
    "items": [item_glasses],

    "people": []
}

room_security = {
    "name": "Security Room",
    "description":"""The terminal reads "ENTER PASSCODE FOR CCTV FOOTAGE", there's not much else to do here.
    (Use the command "try" e.g. try 12345)""",
    "exits": {"south": "Lab"},
    "items": [item_flashlight],
    "people": []
}

room_corpse = {
    "name": "Inner Basement",
    "description":
    """The body of the victim has been poorly hidden in this room. You feel uneasy.""",
    "exits": {"south": "Basement"},
    "items": [],
    "people": []
}

rooms = {
    "Reception": room_reception,
    "Cafe": room_cafe,
    "Lab": room_lab,
    "Parking": room_parking,
    "Matts office": room_matts_office,
    "Lecture Theatre": room_lecture_theatre,
    "Andrew Jones' office": room_andrews_office,
    "Basement": room_basement,
    "Inner Basement": room_corpse,
    "Kitchen": room_kitchen,
    "Security Room": room_security
}


