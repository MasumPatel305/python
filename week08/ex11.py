# 11. Extend world with "garden" connected to "bar". Print description.

world = {
    "rooms": {
        "bar": {"description": "You are in a dark bar.", "connections": ["sauna", "gym"]},
        "sauna": {"description": "You are in the sauna.", "connections": ["bar"]}
    },
    "room": "bar"
}

world["rooms"]["garden"] = {"description": "You are in a lush, green garden.", "connections": ["bar"]}

world["rooms"]["bar"]["connections"].append('garden')

print(world["rooms"]["garden"]["description"])