from tkinter import Tk, Canvas, PhotoImage, mainloop

WIDTH = 640
HEIGHT = 480
window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

img.put("#ffffff", (3, 2))
img.put("#ffffff", (3, 3))
img.put("#ffffff", (3, 4))
img.put("#ffffff", (3, 5))
img.put("#ffffff", (3, 6))
img.put("#ffffff", (3, 7))
img.put("#ffffff", (3, 8))

mainloop()
