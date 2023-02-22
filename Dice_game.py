from tkinter import *


import random, time

def bros():
    x = random.choice(['icons/k1.png','icons/k2.png','icons/k3.png','icons/k4.png','icons/k5.png','icons/k6.png'])
    return x
def img(event):
    global b1, b2
    for i in range(10):
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        lab1['image']= b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.5)

root=Tk()
root.geometry('500x300')
root.title('Игра в кости . Сделай бросок!')
root.resizable(height=False,width=False)
root.iconphoto(True, PhotoImage(file=('icons/icon.png')))
font=PhotoImage(file=('icons/fon.png'))
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3,rely=0.5,anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7,rely=0.5,anchor=CENTER)
root.bind('<1>', img)
img("event")
root.mainloop()