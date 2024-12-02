# Devesh Sukhdeo
# Period 1-2
# 12/2/24

import simplegui 

def draw(canvas):
    canvas.draw_circle((300, 280), 90, 5, "yellow", "brown")
    canvas.draw_circle((300, 180), 55, 5, "yellow", "brown")
    canvas.draw_circle((280, 165), 10, 1, "yellow", "white")
    canvas.draw_circle((320, 165), 10, 1, "yellow", "white")
   
    
 
#Create the frame 
frame = simplegui.create_frame("Thanksgiving Drawing", 600, 400) 
frame.set_canvas_background("white")
frame.set_draw_handler(draw) 
frame.start()
