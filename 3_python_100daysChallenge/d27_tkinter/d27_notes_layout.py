from tkinter import *

def btn_click():
    print("click alert!!")
    new_text = input.get()
    my_label.config(text= new_text)

window = Tk()
window.title("first GUI 'layout'.")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label
my_label = Label(text="I'm a label.", font=('Arial', 24, "bold"))
my_label.config(text= "just text")
my_label.grid(column=1, row=1)

# btn
btn = Button(text="click me", command=btn_click)
btn.grid(column=2, row=0)

#entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

# 3 ways to place the item.
# pack(), place(), grid()
# but you can only choose 1 type in a project


window.mainloop()