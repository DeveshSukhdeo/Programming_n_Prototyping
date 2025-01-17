import simplegui
import random

# Global variables
current_room = "Start"
inventory = []
health = 100
score = 0

# Room descriptions
rooms = {
    "Start": {
        "description": "You are in a dark room with two doors: one to the North and one to the East.",
        "actions": {"Go North": "Forest", "Go East": "Cave"},
    },
    "Forest": {
        "description": "You are in a dense forest. There's a strange chest here.",
        "actions": {"Open Chest": "open_chest", "Go South": "Start"},
    },
    "Cave": {
        "description": "You are in a damp cave. A monster blocks your path!",
        "actions": {"Fight Monster": "fight_monster", "Go West": "Start"},
    },
}

# Helper functions
def update_gui():
    #Update the GUI elements.
    frame.set_draw_handler(draw)
    update_labels()

def update_labels():
    #Update labels for room description, inventory, health, and score.
    description_label.set_text(f"Room: {current_room}\n{rooms[current_room]['description']}")
    inventory_label.set_text(f"Inventory: {', '.join(inventory) if inventory else 'None'}")
    health_label.set_text(f"Health: {health}")
    score_label.set_text(f"Score: {score}")

def go_to_room(room):
    #Navigate to a different room.
    global current_room
    current_room = room
    update_gui()

def open_chest():
    #Simulate opening a chest with a random event.
    global score
    global inventory
    if "Key" not in inventory:
        found = random.choice(["Key", "Gold", "Nothing"])
        if found == "Nothing":
            description_label.set_text("The chest is empty.")
        else:
            inventory.append(found)
            description_label.set_text(f"You found a {found}!")
            if found == "Gold":
                score += 10
    else:
        description_label.set_text("The chest is already empty!")
    update_labels()

def fight_monster():
    #Simulate fighting a monster with random outcomes.
    global health, score
    outcome = random.choice(["win", "lose"])
    if outcome == "win":
        description_label.set_text("You defeated the monster!")
        score += 20
    else:
        description_label.set_text("The monster hit you!")
        health -= 20
    check_game_over()
    update_labels()

def check_game_over():
    #Check for win or loss conditions.
    global current_room
    if health <= 0:
        description_label.set_text("You have died! Game Over!")
        current_room = "Game Over"
    elif "Key" in inventory and current_room == "Cave":
        description_label.set_text("You unlock the treasure and win the game!")
        current_room = "Victory"
    update_labels()

# Event handlers for buttons
def button_handler(action):
    if action in rooms[current_room]["actions"]:
        next_step = rooms[current_room]["actions"][action]
        if callable(globals().get(next_step)):
            globals()[next_step]()
        else:
            go_to_room(next_step)

# Draw handler
def draw(canvas):
    canvas.draw_text("Text Adventure Game", [50, 50], 24, "White")

# Frame and GUI elements
frame = simplegui.create_frame("Text Adventure Game", 600, 500)

description_label = frame.add_label("")
inventory_label = frame.add_label("")
health_label = frame.add_label("")
score_label = frame.add_label("")
frame.add_label("")

# Buttons for actions
for action in ["Go North", "Go East", "Go South", "Go West", "Open Chest", "Fight Monster"]:
    frame.add_button(action, lambda act=action: button_handler(act), 100)

# Initialize the game
update_gui()
frame.start()

