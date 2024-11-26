import simplegui

def cfu13_happy_dots(canvas):
    # create the drawing
    # canvas.draw_point([x, y], color)
    # canvas.draw_point([100, 100], "red")
    
    # canvas.draw_line([point1], [point2], line_width, line_color)
    # canvas.draw_line([x1, y1], [x2, y2], line_width, line_color)
    # canvas.draw_line([0, 0], [200, 200], 5, "purple")
    
    canvas.draw_line([85, 25], [85, 35], 3, "purple")
    canvas.draw_line([115, 25], [115, 35], 3, "purple")
    canvas.draw_line([90, 50], [103, 50], 3, "purple")
    
   

frame = simplegui.create_frame("Python Drawing", 200, 200) 
frame.set_canvas_background("cyan")
frame.set_draw_handler(cfu13_happy_dots) 
frame.start()
