#Devesh Sukhdeo
#Period 1-2
#11/26/24
'''
Draw a canvas of 200 by 200 px
Use the method #canvas.draw_line([point1], [point2], line_with, Line_color) to draw a happy face.
Change the title of the frame to CFU14 Happy Lines

'''
#CFU #14

import simplegui

def cfu14_happy_lines(canvas):
    # create the drawing
    # canvas.draw_point([x, y], color)
    # canvas.draw_line([point1], [point2], line_with, Line_color)
    # canvas.draw_line([x1, y1], [x2, y2], line_with, Line_color)
    canvas.draw_line([90, 40], [90, 60], 3, "black")
    canvas.draw_line([110, 40], [110, 60], 3, "black")
    canvas.draw_line([92, 80], [108, 80], 3, "black")
    canvas.draw_line([82, 70], [92, 80], 3, "black")
    canvas.draw_line([108, 80], [118, 70], 3, "black")
   

frame = simplegui.create_frame("Python Drawing", 200, 200) 
frame.set_canvas_background("cyan")
frame.set_draw_handler(cfu14_happy_lines) 
frame.start()
