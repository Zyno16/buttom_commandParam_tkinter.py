from tkinter import *
form = Tk()

form.geometry("700x500")

Label(form,text="Entry your name", bg = "green",font = "consolas 30 underline" ).pack()
svname = StringVar()
txtname =Entry(form ,bg ="yellow" ,fg = "blue" ,font ="consolas 30 bold",textvariable = svname)
def f (word):
    svname.set(word)
txtname.pack()
Button(form,text="ok",bg= "darkred" ,fg = "pink" ,font = "consolas 30 bold" ,command =lambda:f("hi")).pack()



form.mainloop()
 
