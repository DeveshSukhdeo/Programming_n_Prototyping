# Devesh Sukhdeo
# Period 1-2
# 11/27/24
'''
Draw a canvas of 200 by 200 px
Use the method canvas.draw_polygon([(x1,y1),(x2,y2),(x3,y3)], line_width, color) to draw a happy face
Change the title of the frame to CFU14 Happy Shapes

'''
# CFU#15

import simplegui 

def draw_handler(canvas):
    # canvas.draw_point([x, y], "color")
    # canvas.draw_point([100, 100], "red")
    
    # canvas.draw_line([point1], [point2], line_width, line_color)
    # canvas.draw_line([50, 50], [150, 150], 2, "purple")
    
    # canvas.draw_polygon([(x1, y1), (x2, y2), (x3, y3)], line_width, line_color)
    # canvas.draw_polygon([(1, 100), (10, 50), (10, 75)], 1, "black")
    
    canvas.draw_polygon([(60, 75), (70, 50), (80, 75)], 3, "yellow")
    canvas.draw_polygon([(110, 75), (120, 50), (130, 75)], 3, "yellow")
    canvas.draw_polygon([(60, 100), (95, 120), (130, 100)], 3, "yellow")
    
 
#Create the frame 
frame = simplegui.create_frame("CFU 15 Happy Shapes", 200, 200) 
frame.set_canvas_background("black")
frame.set_draw_handler(draw_handler) 
frame.start()
