from tkinter import *
import time
import random

HEIGHT = 720
WIDTH = 1280

speedX = 0.1
speedY = 0.1
running = True

dvdLogo = []

def mouseEntering(event):
    global speedX
    global speedY
    if int(event.delta/120) > 0:   #MouseScrool event, it always returns a 120 or -120 value
        if (speedX < 1 and speedX >= 0):
            speedX += 0.1
            speedY += 0.1
        elif (speedX > -1 and speedX <= 0):
            speedX -= 0.1
            speedY -= 0.1
    else:
        if (speedX > 0):
            speedX -= 0.1
            speedY -= 0.1
        elif speedX < 0:
            speedX += 0.1
            speedY += 0.1
def mouseLeaving(event):
    running = False

window = Tk()
window.title("Screensaver - The Old Times")

canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg='black')
canvas.pack()

#bg = canvas.create_image(0,0,image=background,anchor=NW)
for i in range(0, 5): dvdLogo.append(PhotoImage(file='dvd-logo-{0}.png'.format(i)))   #Atribuição dos arquivos com elegância

dvd = canvas.create_image(0,0,image=dvdLogo[0],anchor=NW)   #Insere o DVD na posição inicial

canvas.bind('<MouseWheel>', mouseEntering)
#window.bind('<Leave>', mouseLeaving)

while running:
    coordinates = canvas.coords(dvd)
    if coordinates[0] > (WIDTH - dvdLogo[0].width()) or coordinates[0] < 0:
        speedX = -speedX
        (canvas.itemconfig(dvd,image=dvdLogo[random.randrange(0,5)]))
    if coordinates[1] > (HEIGHT - dvdLogo[0].height()) or coordinates[1] < 0:
        speedY = -speedY
        (canvas.itemconfig(dvd, image=dvdLogo[random.randrange(0, 5)]))
    canvas.move(dvd, speedX, speedY)
    window.update()    # ESSENCIAL, sem isso ele quebra

window.resizable(False, False)
window.mainloop()
# ---------------------------------------------------------------- #
