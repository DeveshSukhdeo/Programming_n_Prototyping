# Devesh Sukhdeo 
# Period 1-2
# CFU 17
# Use functions to draw text and shapes 

import simplegui

#Global Variables for Frame Size
frame_width = int(input("Initial Width?")) 
frame_height = int(input("Initial Height?")) 

frame = None #Global reference to the frame

#Shape visibility toggles                         
show_square = True
show_circle = True                            
show_triangle = True                            
show_ellipse = True                            

# Shape drawing Functions
def draw_triangle(canvas, cx, cy, size):
    half_size = size / 2
    canvas.draw_polygon([(cx, cy - half_size), (cx - half_size, cy + half_size), (cx + half_size, cy + half_size)], 2, "Blue", "Blue") #Blue Triangle
    
def draw_square(canvas, cx, cy, size):
    half_size = size / 2
    canvas.draw_polygon([(cx, cy - half_size), (cx - half_size, cy + half_size), (cx + half_size, cy + half_size)], 2, "Green", "Green") #Green Square
    
def draw_circle(canvas, cx, cy, size):
    half_size = size / 2
    canvas.draw_polygon([(cx, cy - half_size), (cx - half_size, cy + half_size), (cx + half_size, cy + half_size)], 2, "Red", "Red") #Red Circle
    
def draw_ellipse(canvas, cx, cy, size):
    half_size = size / 2
    canvas.draw_polygon([(cx, cy - half_size), (cx - half_size, cy + half_size), (cx + half_size, cy + half_size)], 2, "Yellow", "Yellow") #Yellow Ellipse

# Draw Function
def draw(canvas):
    #Calculate the quadrants 
    quadrant_width = frame_width / 2 
    quadrant_height = frame_height / 2 
                         
    #Draw each shape in a different quadrant if toggled 
    if show_triangle:
        draw_triangle(canvas, quadrant_width / 2, frame_height - quadrant_height / 2, 100) #Triangle in bottom-left      
    elif show_square: 
        draw_square(canvas, quadrant_width / 2, frame_height - quadrant_height, 100)
    
                         
# Button Handlers
def toggle_square():
    global show_square
    show_triangle = not show_square
    
def toggle_circle():
    global show_circle
    show_triangle = not show_circle
    
def toggle_triangle():
    global show_triangle
    show_triangle = not show_triangle
       
def toggle_ellipse():
    global show_ellipse
    show_triangle = not show_ellipse 

# Frame Creation
def create_frame():
    global frame
    frame = simplegui.create_frame("Shape Drawing Guide with Toggles", frame_width, frame_height)
    frame.set_draw_handler(draw)
                         
    frame.add_button("Toggle Square", toggle_square, 150)
    frame.add_button("Toggle Circle", toggle_circle, 150)
    frame.add_button("Toggle Triangle", toggle_triangle, 150)
    frame.add_button("Toggle Ellipse", toggle_ellipse, 150)
                         
    frame.start()
                         
# Start the Program
create_frame()                         
                         
                         
                         
