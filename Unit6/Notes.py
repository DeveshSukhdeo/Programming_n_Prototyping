# Devesh Sukhdeo
# Period 1-2
# 11/27/24

import simplegui 

def draw_handler(canvas):
    # canvas.draw_point([x, y], "color")
    canvas.draw_point([100, 10], "white")
    
    # canvas.draw_line([point1], [point2], line_width, line_color)
    canvas.draw_line([50, 50], [150, 150], 5, "purple")
    
    # canvas.draw_polygon([(x1, y1), (x2, y2), (x3, y3)], line_width, line_color)
    canvas.draw_polygon([(1, 100), (10, 50), (10, 75)], 1, "cyan")
    
    # canvas.draw_circle((center), radius, line_width, color)
    canvas.draw_circle((175, 50), 30, 3, "yellow")
    
   
    
 
#Create the frame 
frame = simplegui.create_frame("CFU 15 Happy Shapes", 200, 200) 
frame.set_canvas_background("black")
frame.set_draw_handler(draw_handler) 
frame.start()
