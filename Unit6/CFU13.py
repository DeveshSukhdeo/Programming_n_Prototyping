#Devesh Sukhdeo
#Period 1-2
#11/26/24
'''
Draw a canvas of 200 by 200 px
Use the method .draw_point([x,y],"color") to draw a happy face
Change the title of the frame to CFU13 Happy Dots

'''
#CFU #13

import simplegui

def cfu13_happy_dots(canvas):
    # create the drawing
    # canvas.draw_point([x, y], color)
    
    #eyes
    canvas.draw_point([90, 50], "red")
    canvas.draw_point([110, 50], "red")
    canvas.draw_point([90, 52], "red")
    canvas.draw_point([110, 52], "red")
    canvas.draw_point([90, 54], "red")
    canvas.draw_point([110, 54], "red")
    canvas.draw_point([90, 56], "red")
    canvas.draw_point([110, 56], "red")
    canvas.draw_point([90, 58], "red")
    canvas.draw_point([110, 58], "red")
    #mouth 
    canvas.draw_point([85, 70], "red")
    canvas.draw_point([87, 72], "red")
    canvas.draw_point([89, 74], "red")
    canvas.draw_point([91, 76], "red")
    canvas.draw_point([93, 77], "red")
    canvas.draw_point([95, 77], "red")
    canvas.draw_point([97, 77], "red")
    canvas.draw_point([99, 77], "red")
    canvas.draw_point([101, 77], "red")
    canvas.draw_point([103, 77], "red")
    canvas.draw_point([105, 77], "red")
    canvas.draw_point([107, 77], "red")
    canvas.draw_point([109, 76], "red")
    canvas.draw_point([111, 74], "red")
    canvas.draw_point([113, 72], "red")
    canvas.draw_point([115, 70], "red")
    
    
frame = simplegui.create_frame("Python Drawing", 200, 200) 
frame.set_canvas_background("cyan")
frame.set_draw_handler(cfu13_happy_dots) 
frame.start()
