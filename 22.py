import webbrowser
import tkinter as tk

def open_google():
    webbrowser.open("https://www.google.com")

root = tk.Tk()
root.title("打开Google首页")

button = tk.Button(root, text="打开Google", command=open_google)
button.pack(padx=20, pady=20)

root.mainloop()
