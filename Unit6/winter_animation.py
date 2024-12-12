# Devesh Sukhdeo
# Period 1-2 
# 12/12/24
# Description

import simplegui 
import random 

#Global varibale for the snow
snow_y = []
#Constants for window frame (size), snow
width = 600
height = 600 
snow_flakes = 10 
snowfall_speed = 1

for i in range (snow_flakes): 
    snow_y.append(random.randint(0, height))
    
def draw(canvas):
    global snow_y
    # Draw Background (ground) 
    canvas.draw_polygon([(0,450), (0, 600), (600, 600), (600, 450)], 1, "grey", "grey")
    # Draw Spruce tree
    canvas.draw_polygon([(480,400), (480, 450), (500, 450), (500, 400)], 1, "brown", "brown")
    canvas.draw_polygon([(490,300), (440, 400), (540, 400)], 1, "black", "green")
    # Draw Snowfall
    for i in range(snow_flakes):
        snowflake_x = random.randint(0, width) 
        snowflake_y = random.randint(0, height - 150) 
        canvas.draw_circle((snowflake_x, snowflake_y), 5, 1, "white", "white")

        
frame = simplegui.create_frame("Winter Animation", width, height)
frame.set_canvas_background("lightblue")
frame.set_draw_handler(draw)
frame.start()


