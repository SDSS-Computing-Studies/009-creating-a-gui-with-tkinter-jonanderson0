import tkinter as tk
from tkinter import *

window=tk.Tk()
window.geometry('575x200')

dogp = PhotoImage(file='dog.png')
p=tk.Label(window,image=dogp)


entry1=tk.Entry(window,width=17,borderwidth=1)

entry2=tk.Entry(window,width=17,borderwidth=1)

entry3=tk.Entry(window,width=17,borderwidth=1)

entry4=tk.Entry(window,width=17,borderwidth=1)

entry5=tk.Entry(window,width=17,borderwidth=1)

name=tk.Label(window,text='Name')

typ=tk.Label(window,text='Type')

breed=tk.Label(window,text='Breed')

owner=tk.Label(window,text='Owner')

birth=tk.Label(window,text='Birthdate')

cldat=tk.Label(window,text='Client Database')

search=tk.Button(window,text='Search by Name')

sav=tk.Button(window,text='Save Entry',height=2,width=10)

pre=tk.Button(window,text='< Previous',height=1)

nex=tk.Button(window,text='Next >',height=1)

search2=tk.Entry(window,width=25)


p.grid(row=1,column=1)

cldat.grid(row=1,column=3)

name.grid(row=2,column=1)

typ.grid(row=2,column=2)

breed.grid(row=2,column=3)

owner.grid(row=2,column=4)

birth.grid(row=2,column=5)

entry1.grid(row=3,column=1)

entry2.grid(row=3,column=2)

entry3.grid(row=3,column=3)

entry4.grid(row=3,column=4)

entry5.grid(row=3,column=5)

pre.place(x=0,y=160)

sav.place(x=250,y=150)

nex.place(x=520,y=160)

search.place(x=315,y=0)

search2.place(x=415,y=5)

window.mainloop()
