from tkinter import *
import tkinter as tk
from Chat import get_response, bot_name

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202a"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 12"
FONT_BOLD = "Helvetica 12 bold"

root = tk.Tk()
root.title("HelpR")
root.geometry("470x550+320+100")
root.resizable(width=False, height=False)
root.configure(width=470, height=550, bg="#F8EDE3")
root.iconbitmap(r'icon.ico')

button1 = PhotoImage(file="send_button.png")

# HEAD LABEL
head_label = Label(root, bg='#967E76', fg='white', text='Hello!', font="Helvetica 12 bold", pady=10)
head_label.place(relwidth=1)

# tiny divider
line = Label(root, width=450, bg='#B9FFF8')
line.place(relwidth=1, rely=0.07, relheight=0.020)

# text widget
text_widget = Text(root, width=20, height=2, bg='#EEEEEE', fg='black', font=FONT, padx=15, pady=10)
text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
text_widget.configure(cursor="arrow", state=DISABLED)

# scrollbar
scrollbar = Scrollbar(text_widget)
scrollbar.place(relheight=1, relx=0.974)
scrollbar.configure(command=text_widget.yview)
text_widget.configure(yscrollcommand=scrollbar.set)

# bottom label
bottom_label = Label(root, bg=BG_GRAY, height=80)
bottom_label.place(relwidth=1, rely=0.825)

# send button
send_button = Button(bottom_label, image=button1, bg=BG_GRAY, command=lambda: _on_enter_pressed(None), relief=FLAT)
send_button.place(relx=0.76, rely=0.012)


def _on_enter_pressed(event):
    message = message_entry.get()
    _insert_message(message, "You")


def _insert_message(message, sender):
    if not message:
        return
    message_entry.delete(0, END)
    message1 = f"{sender}: {message}\n\n"
    text_widget.configure(state=NORMAL)
    text_widget.insert(END, message1)
    text_widget.configure(state=DISABLED)

    message2 = f"{bot_name}: {get_response(message)}\n\n"
    text_widget.configure(state=NORMAL)
    text_widget.insert(END, message2)
    text_widget.configure(state=DISABLED)

    text_widget.see(END)


# message entry
message_entry = Entry(bottom_label, bg="#B9FFF8", fg='#472D2D', font=FONT)
message_entry.place(relwidth=0.724, relheight=0.04, rely=0.008, relx=0.011)
message_entry.focus()
message_entry.bind("<Return>", _on_enter_pressed)

root.mainloop()
