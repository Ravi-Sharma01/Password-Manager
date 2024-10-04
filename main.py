from tkinter import *
from tkinter import messagebox
from random import random, choice, randint, shuffle
import pyperclip
import json
# ---------------------------generate password --------------------#


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters+password_numbers+password_symbols

    shuffle(password_list)
    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)

# --------------------------- Save Password ----------------------- #


def save():
    website = web_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": user,
            "password": password,

        }
    }

    if len(user) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please dont leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title="Save", message=f"There is password:{password}\nEmail:{user}\nis it save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # update old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # save data
                    json.dump(data, data_file, indent=4)
            finally:
                web_entry.delete(0, END)
                user_entry.delete(0, END)
                pass_entry.delete(0, END)
                messagebox.showinfo(title="Message", message="saved successfully")

# --------------------------- search data ------------------------ #


def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email:{email}\npassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"no details for {website} exists.")


# --------------------------- UI DET UP --------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)
vendor_label = Label(text="Made by Ravi", font=("arial", 7, "bold"), fg="red")
vendor_label.grid(row=5, column=2)


# ENTRY
web_entry = Entry(width=22)
web_entry.grid(row=1, column=1)
web_entry.focus()
user_entry = Entry(width=40)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "xyz123@gmail.com")
pass_entry = Entry(width=22)
pass_entry.grid(row=3, column=1)

# BUTTONS
gen_pass_btn = Button(text="Generate Password", command=generate_password).grid(row=3, column=2)
add_btn = Button(text="Add", width=34, command=save).grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)




window.mainloop()