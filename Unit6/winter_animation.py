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
height = 400 
snow_flakes = 10 
snowfall_speed = 1

for i in range (snow_flakes): 
    snow_y.append(random.randint(0, height))
    
def draw(canvas):
    global snow_y
    #draw background (lignt blue for sky) 
    canvas.draw_polygon([(0,0), (width, 0), (width, height), (0, height)], 1, "white", "lightblue")
    for i in range(snow_flakes):
        snowflake_x = random.randint(0, width) 
        snowflake_y = random.randint(0, height) 
        canvas.draw_circle((snowflake_x, snow_y[i]), 5, 1, "white", "white")

        
frame = simplegui.create_frame("Winter Animation", width, height)
frame.set_canvas_background("white")
frame.set_draw_handler(draw)
frame.start()


