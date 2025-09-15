# 12. Write can_move(world, from_room, to_room) returning True/False.

world = {
    "rooms": {
        "bar": {"description": "You are in a dark bar.", "connections": ["sauna", "gym", "garden"]},
        "sauna": {"description": "You are in the sauna.", "connections": ["bar"]},
        "garden": {"description": "You are in a lush, green garden.", "connections": ["bar"]}
    },
    "room": "bar"
}

def can_move(world, from_room, to_room):
    if to_room in world["rooms"][from_room]["connections"]:
        return True
    else:
        return False
    
print(can_move(world, "bar", "garden"))  
print(can_move(world, "sauna", "gym")) 