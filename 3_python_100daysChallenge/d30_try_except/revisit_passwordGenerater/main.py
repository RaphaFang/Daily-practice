from tkinter import*
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

str = "3_python_100daysChallenge/d30_try_except/revisit_passwordGenerater/data.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # join
    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    # password += char
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
         website:{"email": email, "password": password}
    }

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showerror(title="Oops", message="Some fields empty!")
    else:
        try:
            with open(str, "r") as data_file:
            # read old data
                data = json.load(data_file)
        except FileNotFoundError:
            # file not exit, write a file
            with open(str, "w") as data_file:
                json.dump(new_datadata, data_file, indent=4)
        else:
            data.update(new_data)
            # update data
            with open(str, "w") as data_file:
            # save data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- 
def search():
    website = website_entry.get()
    try:
        with open(str) as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
        # this for the exact file not found
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Data for {website}.")
        # this for the actual pice of info not found


# ---------------------------- UI SETUP ------------------------------- 
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="3_python_100daysChallenge/d29_passwordManager/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# label
website = Label(text="website")
website.grid(column=0, row=1)
Email_Username = Label(text="Email/Username")
Email_Username.grid(column=0, row=2)
password = Label(text="password")
password.grid(column=0, row=3)

# entry
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)

email_entry.insert(0, "fangsihyu0211@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4 , columnspan=2)

search_button = Button(text="Search", width=13, command=search)
search_button.grid(column=2, row=1, columnspan=1)


window.mainloop()

#-----