from tkinter import Tk, Canvas, PhotoImage, mainloop

WIDTH = 640
HEIGHT = 480
window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

img.put("#ffffff", (13, 2))
img.put("#ffffff", (13, 3))
img.put("#ffffff", (13, 4))
img.put("#ffffff", (13, 5))
img.put("#ffffff", (13, 6))
img.put("#ffffff", (13, 7))
img.put("#ffffff", (13, 8))
img.put("#ffffff", (13, 9))
img.put("#ffffff", (13, 10))
img.put("#ffffff", (13, 11))


mainloop()
