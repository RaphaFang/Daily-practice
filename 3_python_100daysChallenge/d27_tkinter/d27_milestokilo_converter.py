from tkinter import *

def btn_click():
    print("click alert!!")
    new_text = float(miles_input.get())
    new_text*=1.609
    Km_output_label.config(text= new_text)

window = Tk()
window.title("d27_mile to kilo converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

Miles_label = Label(text="Miles", font=('Arial', 24, "bold"))
Miles_label.grid(column=2, row=0)

Km_label = Label(text="Km", font=('Arial', 24, "bold"))
Km_label.grid(column=2, row=1)

equal_label = Label(text="is equal to:", font=('Arial', 24, "bold"))
equal_label.grid(column=0, row=1)

Km_output_label = Label(text="0", font=('Arial', 24, "bold"))
Km_output_label.grid(column=1, row=1)

# btn
btn = Button(text="calculate", command=btn_click)
btn.grid(column=1, row=3)

#entry
miles_input = Entry(width=10)
print(miles_input.get())
miles_input.grid(column=1, row=0)

# 3 ways to place the item.
# pack(), place(), grid()
# but you can only choose 1 type in a project


window.mainloop()