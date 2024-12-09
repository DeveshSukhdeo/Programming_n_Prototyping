# Devesh Sukhdeo 
# Period 1-2
# CFU 17
# Use functions to draw text and shapes 

import simplegui

message = "Hello" 
color1 = input("Enter color")
frame_width = int(input("Initial Width?"))
frame_height = int(input("Initial Height?"))

def draw(canvas): 
    canvas.draw_line([0,0], [100, 100], 3, color1)
    canvas.draw_text(message, [frame_width/2, frame_height/2], 30, color1)
    
frame = simplegui.create_frame("CFU #17", frame_width, frame_height)
