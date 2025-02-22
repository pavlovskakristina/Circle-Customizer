from turtle import Turtle, Screen
import tkinter as tk
from tkinter import ttk
import random


def take_parameters():
    degrees = entry_int.get()
    if degrees.isdigit():
        degrees = int(degrees)
        output_string.set(f"Data extracted: {degrees}")
        window.destroy()

        draw_circle(degrees)

    else:
        output_string.set("Please enter a valid data")


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_color = (red, green, blue)
    return random_color


def draw_circle(step_degrees):
    turtle = Turtle()
    screen = Screen()
    turtle.speed(0)
    screen.colormode(255)

    start_position = turtle.heading()
    contin = True

    while contin:
        turtle.color(random_color())
        turtle.circle(100)

        turtle.setheading(turtle.heading() + step_degrees)
        if (turtle.heading() % 360) == start_position:
            break

    screen.exitonclick()


window = tk.Tk()
window.title("Circle Settings Panel")
window.geometry('400x230')


style = ttk.Style(window)
style.theme_use('clam')

main_frame = ttk.Frame(window, padding=20)
main_frame.pack(expand=True)

title_label = ttk.Label(window, text="Circle Customizer", font="Calibri 24 bold")
title_label.pack(pady=10)



entry_int = tk.StringVar()
entry = ttk.Entry(window, textvariable=entry_int)
entry.pack(pady=5)

instruction_label = ttk.Label(main_frame, text="Please enter a value between 1 and 180", font="Calibri 14 bold")
instruction_label.pack(pady=5)

button = ttk.Button(window, text="Draw Circle", command=take_parameters, takefocus=False, style="TButton")
button.pack(pady=10)


output_string = tk.StringVar()
output_label = ttk.Label(window, textvariable=output_string)
output_label.pack(pady=5)


window.mainloop()











