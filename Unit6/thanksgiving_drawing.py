# Devesh Sukhdeo
# Period 1-2
# 12/2/24

import simplegui 
#Frame Setup 
frame = simplegui.create_frame("Thanksgiving Drawing", 600, 400)
#Set Frame Background 
frame.set_canvas_background("skyblue")

def draw(canvas):
    #Polygons (Feathers)
    canvas.draw_polygon([(280, 220), (100, 230), (270, 340)], 2, "black", "blue")
    canvas.draw_polygon([(290, 150), (130, 80), (280, 280)], 2, "black", "yellow")
    canvas.draw_polygon([(250, 150), (300, 20), (350, 150)], 2, "black", "pink")
    canvas.draw_polygon([(310, 150), (470, 80), (320, 280)], 2, "black", "red")
    canvas.draw_polygon([(320, 220), (500, 230), (330, 340)], 2, "black", "green")
   
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
     
#Assign draw handler to frame 
frame.set_draw_handler(draw)
#Start Frame 
frame.start()
