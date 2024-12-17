# Devesh Sukhdeo
# Period 1-2 
# 12/12/24
# Create a winter themed animation using the simplegui library in python

import simplegui 
import random 

#Global varibale for the snow
snow_y = []
# Snowman parts global variable 
snowman_parts = []
snowman_sticks = []
snowman_squares = []
#Constants for window frame (size), snow
width = 600
height = 600 
snow_flakes = 5 
# Count variable for timer
count = 0
text_move = 1

for i in range (snow_flakes): 
    snow_y.append(random.randint(0, height))

# Draw function (What appears on the canvas)    
def draw(canvas):
    global snow_y
    global text_move
    text_move += 0.8
    
    # Draw Background (ground) 
    canvas.draw_polygon([(0,450), (0, 600), (600, 600), (600, 450)], 1, "#ededed", "#ededed")
    
    # Draw Spruce tree
    canvas.draw_polygon([(480,300), (480, 450), (500, 450), (500, 400)], 1, "#7d5839", "#7d5839")
    canvas.draw_polygon([(490,280), (400, 400), (580, 400)], 1, "black", "#05ce64")
    canvas.draw_polygon([(490,230), (420, 330), (560, 330)], 1, "black", "#05d667")
    canvas.draw_polygon([(490,190), (435, 270), (545, 270)], 1, "black", "#05de6b")
   
    # Draw Snowfall
    for i in range(snow_flakes):
        snowflake_x = random.randint(0, width) 
        snowflake_y = random.randint(0, height - 150) 
        canvas.draw_circle((snowflake_x, snowflake_y), 5, 1, "white", "white")
    
    # Start list of snowman parts
    for part in snowman_parts:
        canvas.draw_circle(part["center"], part["radius"], 2, part["color"], part["color"])
    # Start list for arms
    for part in snowman_sticks:
        canvas.draw_line(part["start"], part["end"], 7, part["color"])
    # Start list for top hat    
    for part in snowman_squares: 
        canvas.draw_polygon((part["point1"], part["point2"], part["point3"], part["point4"]), 1, part["color"], part["color"])
    
    # Add moving text
    canvas.draw_text("Giant Snowman!", (text_move, 50), 30, "black", "monospace") 
        
# First timer, will contin all circles        
def timer_handler1():
    global count
    count += 1
    
    if count == 1: 
        # First snow ball
        snowman_parts.append({"center": (220, 400), "radius": 50, "color": "White"})
    elif count == 2:
        # Add eyes
        snowman_parts.append({"center": (205, 390), "radius": 7, "color": "black"})
        snowman_parts.append({"center": (235, 390), "radius": 7, "color": "black"})
    elif count == 3: 
        # Add bigger snow ball for body
        snowman_parts.append({"center": (220, 370), "radius": 80, "color": "White"})
    elif count == 4: 
        # Add face and eyes above body
        snowman_parts.append({"center": (220, 255), "radius": 50, "color": "White"})
        snowman_parts.append({"center": (205, 235), "radius": 7, "color": "black"})
        snowman_parts.append({"center": (235, 235), "radius": 7, "color": "black"})
    elif count == 7:
        # Add smile
        snowman_parts.append({"center": (195, 260), "radius": 4, "color": "black"})
        snowman_parts.append({"center": (210, 275), "radius": 4, "color": "black"})
        snowman_parts.append({"center": (230, 275), "radius": 4, "color": "black"})
        snowman_parts.append({"center": (245, 260), "radius": 4, "color": "black"})

# Second timer, will contain all lines        
def timer_handler2():
    global count
    
    if count == 5:
        # Add right arms
        snowman_sticks.append({"start": (270, 345), "end": (340, 320), "color": "brown"})
        snowman_sticks.append({"start": (310, 330), "end": (315, 300), "color": "brown"})
        snowman_sticks.append({"start": (320, 325), "end": (350, 340), "color": "brown"})  
    elif count == 6: 
        # Add left arms
        snowman_sticks.append({"start": (180, 345), "end": (105, 320), "color": "brown"})
        snowman_sticks.append({"start": (135, 328), "end": (125, 300), "color": "brown"})  
        snowman_sticks.append({"start": (125, 325), "end": (100, 340), "color": "brown"})  

# Third timer, will contain all polygons        
def timer_handler3():
    global count 
    
    if count == 8: 
        # Added the black part of the top hat
        snowman_squares.append({"point1": (190, 150), "point2": (190, 200), "point3": (250, 200), "point4": (250, 150), "color": "black"})
        snowman_squares.append({"point1": (170, 200), "point2": (170, 215), "point3": (270, 215), "point4": (270, 200), "color": "black"})
    elif count == 9: 
        # Added red band to top hat (for more detail) 
        snowman_squares.append({"point1": (190, 190), "point2": (190, 200), "point3": (250, 200), "point4": (250, 190), "color": "red"})
        
# Create timer for circles
timer = simplegui.create_timer(1000, timer_handler1)
timer.start()
# Create timer for lines
timer = simplegui.create_timer(1000, timer_handler2)
timer.start()
#Create timer for squares / polygons
timer = simplegui.create_timer(1000, timer_handler3)
timer.start()
# Create and start the frame
frame = simplegui.create_frame("Winter Animation", width, height)
frame.set_canvas_background("#26beff")
frame.set_draw_handler(draw)
frame.start()
