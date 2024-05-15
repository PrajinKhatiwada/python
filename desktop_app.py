from tkinter import *

root = Tk()
root.title('Prajin khatiwada')
root.geometry("800x600")
def hello():
    hello_label=Label(root,text="hello" + myTextbox.get())
    hello_label.pack()

myLabel = Label(root,text="enter your name:")
myLabel.pack()
myTextbox=Entry(root,width=30)
myTextbox.pack()
myButton=Button(root,text="Submit", command=hello)
myButton.pack()






root.mainloop()