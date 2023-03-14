import tkinter as tk
import random

# configurar la ventana
window = tk.Tk()
window.title("Aspiradora")
window.geometry("900x900")
window.resizable(False, False)  # desactivar botón de maximizar

# crear un lienzo para dibujar
canvas = tk.Canvas(window, width=900, height=900)

# dibujar la cuadrícula
for i in range(0, 901, 30):
    canvas.create_line(i, 0, i, 900, fill="#ddd")
    canvas.create_line(0, i, 900, i, fill="#ddd")

# agregar un punto
x, y = 75, 45 #Centro del punto
r = 14
canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")

# cargar la imagen
image = tk.PhotoImage(file="imagenes/aspiradora.png")
image = image.subsample(image.width() // 30)  # reducir a 60 x **
x, y = 120, 30 #Esquina izquierda

img_obj = canvas.create_image(x, y, image=image, anchor="nw")

# mover la imagen con clics
def move_image(event):
    global x, y
    x = random.randrange(0, 900/30) * 10
    y = random.randrange(0, 900/30) * 10
    canvas.coords(img_obj, x, y)

canvas.bind("<Button-1>", move_image)

# mostrar el lienzo
canvas.pack()

# iniciar el bucle de eventos
window.mainloop()
