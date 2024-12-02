# Devesh Sukhdeo
# Period 1-2
# 11/27/24
'''
Draw a canvas of 200 by 200 px
Use the method #canvas.draw_circle(centerXY, radius, line_width, color) to draw a happy face
Change the title of the frame to CFU16 Happy circles

'''
# CFU#16

import simplegui 

def draw_handler(canvas):
    #Face
    canvas.draw_circle((100, 100), 70, 4, "yellow")
    #Eyes
    canvas.draw_circle((75, 75), 10, 4, "yellow")
    canvas.draw_circle((125, 75), 10, 4, "yellow")
    #Mouth 
    canvas.draw_circle((75, 115), 5, 2, "yellow")
    canvas.draw_circle((85, 125), 5, 2, "yellow")
    canvas.draw_circle((100, 130), 5, 2, "yellow")
    canvas.draw_circle((115, 125), 5, 2, "yellow")
    canvas.draw_circle((125, 115), 5, 2, "yellow")
 
#Create the frame 
frame = simplegui.create_frame("CFU16 Happy Circles", 200, 200) 
frame.set_canvas_background("black")
frame.set_draw_handler(draw_handler) 
frame.start()
