# Devesh Sukhdeo
# Period 1-2
# 12/2/24

import simplegui 

def draw(canvas):
    #Polygons (Feathers)
    
    
    #Cirlces (Make the body)
    canvas.draw_circle((300, 280), 85, 5, "brown", "brown")
    canvas.draw_circle((300, 170), 55, 5, "brown", "brown")
    #Circles (Make eyes)
    canvas.draw_circle((280, 155), 10, 1, "white", "white")
    canvas.draw_circle((320, 155), 10, 1, "white", "white")
    
    #Circle & Points (Make the pupil of the eyes)
    canvas.draw_circle((281, 156), 5, 1, "black", "black")
    canvas.draw_circle((319, 156), 5, 1, "black", "black")
    canvas.draw_point([282, 154], "white")
    canvas.draw_point([320, 154], "white")
    
    #Polygon (Beak)
    canvas.draw_polygon([(290, 170), (300, 180), (310, 170)], 1, "yellow", "yellow")
   
    
 
#Create the frame 
frame = simplegui.create_frame("Thanksgiving Drawing", 600, 400) 
frame.set_canvas_background("skyblue")
frame.set_draw_handler(draw)
frame.start()
