import tkinter as tk
import tkinter.messagebox as messagebox

def button_click():
    user_input = entry.get()
    try:
        miles = float(user_input)
        kilometer = 1.60934 * miles
        label_widget.config(text=kilometer)
    except ValueError:
        messagebox.showerror("Error", "Invalid input: " + user_input)

def key_pressed(event):
    if event.keysym == "Return":
        button_click()

window = tk.Tk()
window.geometry("300x100")
window.title("MILE to KILOMETER")


label = tk.Label(window, text="is equal to")
label.place(x=5, y=40)
# label.grid(row=1, column=0, padx=20)

Miles = tk.Label(window, text="Miles")
Miles.place(x=240, y=20)
# Miles.grid(row=0, column=2, padx=10, pady=10)

kilo = tk.Label(window, text='Km')
kilo.place(x=240, y=50)
# kilo.grid(row=1, column=2)

entry = tk.Entry(window)
entry.place(x=100, y=20)
# entry.grid(row=0, column=1)

label_widget = tk.Label(window)
label_widget.place(x=100, y=50)
# label_widget.grid(row=1, column=1, padx=10)

window.bind("<KeyPress>", key_pressed)

button = tk.Button(window, text="Convert", command=button_click)
button.place(x=140, y=70)
# button.grid(row=2, column=1, pady=10)

window.mainloop()
