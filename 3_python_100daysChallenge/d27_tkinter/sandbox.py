import tkinter

window = tkinter.Tk()
## beaware the "Tk()" not both uppercase
window.title("GUI surface")
window.minsize(width=500, height=300)

## my_lable
my_lable = tkinter.Label(text="new text", font=('Arial', 30))
my_lable.pack(expand=True)
## pack the lable on the screen

window.mainloop()
