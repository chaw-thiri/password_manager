# ----------------------------- LIBRARIES -----------------------------------------#
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ----------------------------- CONSTANTS -----------------------------------------#
BLACK = "#000000"
WHITE = "#FFFFFF"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def getPW():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pw_letters = [random.choice(letters) for i in range(nr_letters)]
    pw_symbols = [random.choice(symbols) for y in range(nr_symbols)]
    pw_numbers = [random.choice(numbers) for x in range(nr_numbers)]
    pw_list = pw_letters + pw_symbols + pw_numbers
    random.shuffle(pw_list)

    password = "".join(pw_list)

    pwEntry.delete(0, END)
    pwEntry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = webEntry.get()
    mail = emailEntry.get()
    pw = pwEntry.get()
    new_data = {web:
        {
            "email": mail,
            "password": pw
        }
    }

    if len(web) == 0 or len(web) == 0:
        messagebox.showwarning(title="No Data", message="None of the fields can be empty.")
        return 0
    is_ok = messagebox.askyesno(title=web, message="Is your information correct?\n"
                                                   f"Website: {web}\nUsername/ mail: {mail}\nPassword: {pw}")
    if is_ok:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)  # copying the old data as data

        except FileNotFoundError as e:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)  # updating the data file with new information
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)  # writing old+ new data in the json file
        finally:
            messagebox.showinfo(title="Confirmation", message="Your password has been saved.")
            webEntry.delete(0, END)
            emailEntry.delete(0, END)
            pwEntry.delete(0, END)

        return


# ---------------------------- Search Account --------------------------------#
def search():
    website = webEntry.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError as e:
        messagebox.showinfo(title="Empty file", message="You haven't save any password yet.")
    else:
        if website in data:
            web = data[website]
            mail = web["email"]
            pw = web["password"]
            messagebox.showinfo(title="Result", message=f"Website: {website}\nGmail/Username: {mail}\nPassword: {pw}")
        else:
            messagebox.showinfo(title="Data not found", message="No such website in the database")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg=BLACK)

# add password background using canvas
canvas = Canvas(width=200, height=200, bg=BLACK, highlightthickness=0)
passwordImg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=passwordImg)
canvas.grid(row=0, column=1)

# LABELS
#  website label
webLabel = Label()
webLabel.config(text="Website: ", fg=WHITE, bg=BLACK)
webLabel.grid(row=1, column=0)
# username/email label
emailLabel = Label()
emailLabel.config(text="Username/ Email: ", fg=WHITE, bg=BLACK)
emailLabel.grid(row=2, column=0)
# pw label
pwLabel = Label()
pwLabel.config(text="Password: ", fg=WHITE, bg=BLACK)
pwLabel.grid(row=3, column=0)

# ENTRIES
webEntry = Entry(width=34)
webEntry.grid(row=1, column=1)
webEntry.focus()

emailEntry = Entry(width=53)
emailEntry.grid(row=2, column=1, columnspan=2)
emailEntry.insert(0, "@gmail.com")

pwEntry = Entry(width=34)
pwEntry.grid(row=3, column=1)

# BUTTONS
# search button
searchButton = Button(text="       Search       ", bg=BLACK, fg=WHITE, command=search)
searchButton.grid(row=1, column=2)

# generate password button
pwButton = Button(text="Generate Password", bg=BLACK, fg=WHITE, command=getPW)
pwButton.grid(row=3, column=2)

# add "ADD" button to add the username-pw pair into the text file
addButton = Button(text="Add", width=44, bg=BLACK, fg=WHITE, command=save)
addButton.grid(row=4, column=1, columnspan=2)

# ---------------------------------------------------------------------------------------------------------------------
window.mainloop()
