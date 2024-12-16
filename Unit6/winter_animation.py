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
#Constants for window frame (size), snow
width = 600
height = 600 
snow_flakes = 5 

# Count variable for timer
count = 0

for i in range (snow_flakes): 
    snow_y.append(random.randint(0, height))
    
def draw(canvas):
    global snow_y
    
    # Draw Background (ground) 
    canvas.draw_polygon([(0,450), (0, 600), (600, 600), (600, 450)], 1, "grey", "grey")
    
    # Draw Spruce tree
    canvas.draw_polygon([(480,300), (480, 450), (500, 450), (500, 400)], 1, "brown", "brown")
    canvas.draw_polygon([(490,280), (400, 400), (580, 400)], 1, "black", "green")
    canvas.draw_polygon([(490,230), (420, 330), (560, 330)], 1, "black", "green")
    canvas.draw_polygon([(490,190), (435, 270), (545, 270)], 1, "black", "green")
   
    # Draw Snowfall
    for i in range(snow_flakes):
        snowflake_x = random.randint(0, width) 
        snowflake_y = random.randint(0, height - 150) 
        canvas.draw_circle((snowflake_x, snowflake_y), 5, 1, "white", "white")
    
    # Start list of snowman parts
    for part in snowman_parts:
        canvas.draw_circle(part["center"], part["radius"], 2, part["color"], part["color"])
  
def timer_handler():
    global count
    count += 1
    
    if count == 1: 
        snowman_parts.append({"center": (220, 400), "radius": 50, "color": "White"})
    elif count == 2:
        snowman_parts.append({"center": (200, 390), "radius": 8, "color": "black"})
        snowman_parts.append({"center": (240, 390), "radius": 8, "color": "black"})
    elif count == 3: 
        snowman_parts.append({"center": (220, 370), "radius": 80, "color": "White"})
    elif count == 4: 
        snowman_parts.append({"center": (220, 255), "radius": 50, "color": "White"})
        snowman_parts.append({"center": (200, 245), "radius": 8, "color": "black"})
        snowman_parts.append({"center": (240, 245), "radius": 8, "color": "black"})
        
        
# Create timer 
timer = simplegui.create_timer(100, timer_handler)
timer.start()
# Create and start the frame
frame = simplegui.create_frame("Winter Animation", width, height)
frame.set_canvas_background("lightblue")
frame.set_draw_handler(draw)
frame.start()
