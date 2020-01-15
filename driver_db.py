import login_db
import tkinter


def new():
    mes = login_db.new_login(user_entry.get(), pas_entry.get())
    if mes is not None:
        message.configure(text=mes, width=1000)
    else:
        message.configure(text="New User " + user_entry.get() + " Created", width=1000)


def log():
    word = login_db.search_for(user_entry.get())
    if isinstance(word, bool):
        message.configure(text="No Username Match: Create a New Account", width=1000)
        return
    if word != pas_entry.get():
        message.configure(text="Wrong Password", width=1000)
    else:
        message.configure(text="Welcome " + user_entry.get() + '!', width=1000)


window = tkinter.Tk()
window.title("Login Terminal")
window.configure(bg="dark grey")

message = tkinter.Message(window, bg="dark grey", text="Login or Create a New Account:", font="white", width=1000)
message.grid(row=0, column=0)

frame1 = tkinter.Frame(window)
frame1.grid(row=1, column=0)
tkinter.Label(frame1, text="User Name:", bg="dark grey", width=10).pack(side="left")
user_entry = tkinter.Entry(frame1, width=15)
user_entry.pack()

frame2 = tkinter.Frame(window)
frame2.grid(row=2, column=0)
tkinter.Label(frame2, text="Password:", bg="dark grey", width=10).pack(side="left")
pas_entry = tkinter.Entry(frame2, width=15)
pas_entry.pack()

tkinter.Label(bg="dark grey").grid(row=3, column=0)

frame3 = tkinter.Frame(window)
frame3.grid(row=4, column=0)
new_button = tkinter.Button(frame3, text="New Login", bg="light blue", fg="black", width=9, command=new)
new_button.pack(side="left")
tkinter.Button(frame3, text="Login", bg="light blue", fg="black", width=9, command=log).pack(side="left")

window.mainloop()
