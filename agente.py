import tkinter as tk
import random
import time

# configurar la ventana
window = tk.Tk()
window.title("Aspiradora")
window.geometry("900x900")
window.resizable(False, False)  # desactivar botón de maximizar

# crear un lienzo para dibujar
canvas = tk.Canvas(window, width=900, height=900)

# dibujar la cuadrícula
for i in range(0, 901, 30):
    canvas.create_line(i, 0, i, 900, fill="#ccc")
    canvas.create_line(0, i, 900, i, fill="#ccc")

# agregar unos puntos
#for i in range(random.randrange(5, 15)):
#    x = (random.randrange(0, 30)) * 30 + 15 #Centro del punto
#    y = (random.randrange(0, 30)) * 30 + 15 #Centro del punto
#    r = 14
    
#    canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")

# cargar la imagen basura
basura = []

imagebasura = tk.PhotoImage(file="imagenes/basura.png")
imagebasura = imagebasura.subsample(imagebasura.height() // 30 )  # reducir a 30 x **

for i in range(random.randrange(5, 15)):
    x = (random.randrange(0, 30)) * 30 #Esquina izquierda
    y = (random.randrange(0, 30)) * 30 #Esquina izquierda

    basura.append((x, y))

    img_obj_basura = canvas.create_image(x, y, image=imagebasura, anchor="nw")

# cargar la imagen
image = tk.PhotoImage(file="imagenes/aspiradora.png")
image = image.subsample(image.width() // 30)  # reducir a 30 x **
x, y = 120, 30 #Esquina izquierda

img_obj = canvas.create_image(x, y, image=image, anchor="nw")
inicio = False

# mover la imagen con clics
def move_image(event):
    global inicio

    inicio = not inicio
    print("CLIC", inicio)

canvas.bind("<Button-1>", move_image)
print("CLIC", inicio)
while inicio:

    x += (random.randrange(-1, 1)) * 30
    y += (random.randrange(-1, 1)) * 30

    if x < 0:
        x = 870

    if x > 870:
        x = 0

    if y < 0:
        y = 870

    if y > 870:
        y = 0
    
    print(x, y)

    canvas.coords(img_obj, x, y)
    time.sleep(0.5)



# mostrar el lienzo
canvas.pack()

# iniciar el bucle de eventos
window.mainloop()
