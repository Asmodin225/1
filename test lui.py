from tkinter import *
from tkinter import ttk
win = Tk()
win.title('My project')
win.geometry('500x300')
win.resizable(False,False) # заборона зміни розміру вікна
#  елементи керування
# написи
nap = Label(win,text='текст для напису', font=('Comic Sans №5',20),bg = 'green' )
nap.place(relx=0.2,rely=0.1)
ent = Entry(win,font=('Comic Sans №5', 20), width=4)
ent.place(relx = 0.1, rely = 0.2)
# button
but = Button(win, text='Click', font=('Comic Sans №5',20), width=7, height=3, )
but.place(relx = 0.1, rely = 0.35)
comb =ttk.Combobox(win,font=('Comic Sans №5',20), width =10, values=('fwggreg', 'gergreger') )
comb.place(relx = 0.4 , rely = 0.35)


win.mainloop()