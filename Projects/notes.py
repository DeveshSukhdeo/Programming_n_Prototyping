# Devesh Sukhdeo
# Period 1-2

import simplegui
import random

# Global Variables
width = 400
height = 400
face1 = False
face2 = False
face3 = False
face4 = False
show_all = False

# Event Handlers
def all_false():
    global face1, face2, face3, face4, show_all
    face1 = face2 = face3 = face4 = show_all = False

def toggle_face1():
    global face1, face2, face3, face4, show_all
    all_false()
    face1 = True

def toggle_face2():
    global face1, face2, face3, face4, show_all
    all_false()
    face2 = True

def toggle_face3():
    global face1, face2, face3, face4, show_all
    all_false()
    face3 = True

def toggle_face4():
    global face1, face2, face3, face4, show_all
    all_false()
    face4 = True

def toggle_all():
    global show_all
    all_false()
    show_all = True

def clear_all():
    all_false()

def draw_face(canvas, x, y, size, face_type):
    if face_type == 1:  
        canvas.draw_circle((x, y), size, 10, "Yellow", "Yellow") 
    elif face_type == 2:  
        canvas.draw_circle((x, y), size, 10, "Skyblue", "Skyblue")
    elif face_type == 3: 
        canvas.draw_circle((x, y), size, 10, "#c0c0bf","#c0c0bf")
    elif face_type == 4: 
        canvas.draw_circle((x, y), size, 10, "#ffde34", "#ffde34")

def draw(canvas):
    quad_size = min(width, height) / 2.5
    if show_all:
        draw_face(canvas, width/4, height/4, quad_size/2, 1)
        draw_face(canvas, 3*width/4, height/4, quad_size/2, 2)
        draw_face(canvas, width/4, 3*height/4, quad_size/2, 3)
        draw_face(canvas, 3*width/4, 3*height/4, quad_size/2, 4)
    else:
        if face1:
            draw_face(canvas, width/4, height/4, quad_size/2, 1)
        elif face2:
            draw_face(canvas, 3*width/4, height/4, quad_size/2, 2)
        elif face3:
            draw_face(canvas, width/4, 3*height/4, quad_size/2, 3)
        elif face4:
            draw_face(canvas, 3*width/4, 3*height/4, quad_size/2, 4)
            

frame = simplegui.create_frame("Peace Formers Game", width, height)
frame.set_draw_handler(draw)
frame.add_button("Start", toggle_face1, 100)
frame.add_button("Go North", toggle_face2, 100)
frame.add_button("Interact", toggle_face3, 100)
frame.add_button("Fight", toggle_face4, 100)

frame.add_button("Show All", toggle_all, 100)
frame.add_button("Clear All", clear_all, 100)

frame.start()
