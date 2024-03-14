from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json

FONT = ("Times New Roman", 15, "normal")

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for sym in range(randint(2, 4))]
    password_numbers = [choice(numbers) for numb in range(randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)
    gen_password = "".join(password_list)
    ent_password.insert(0, gen_password)
    pyperclip.copy(gen_password)


def save():

    website = ent_website.get()
    email = ent_user.get()
    password = ent_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            ent_website.delete(0, END)
            ent_password.delete(0, END)
            ent_website.focus()


def search():
    try:
        with open("data.json", "r") as data_file:
            web_to_find = ent_website.get()
            data = json.load(data_file)
            jsondata = data[web_to_find]
            messagebox.showinfo(title=f"{web_to_find}", message=f"{jsondata}")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found.")
    except KeyError:
        messagebox.showinfo(title="Oops", message="No details for the website exist.")


window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website = Label(text="Website:", font=FONT)
website.grid(row=1, column=0)
email_username = Label(text="Email/ Username:", font=FONT)
email_username.grid(row=2, column=0)
password = Label(text="Password:", font=FONT)
password.grid(row=3, column=0)

ent_website = Entry(width=21)
ent_website.grid(row=1, column=1)
ent_website.focus()
ent_user = Entry(width=38)
ent_user.grid(row=2, column=1, columnspan=2)
ent_user.insert(0, "nina.ceccatelli@icloud.com")
ent_password = Entry(width=21)
ent_password.grid(row=3, column=1)

add = Button(text="Add", width=40, font=FONT, command=save)
add.grid(row=4, column=1, columnspan=2)
gen_pass = Button(text="Generate Password", font=FONT, command=generate_password)
gen_pass.grid(row=3, column=2)
search_web = Button(text="Search", font=FONT, command=search, width=14)
search_web.grid(row=1, column=2)

window.mainloop()
