from Agent import checkScreen
import tkinter as tk
from tkinter import messagebox
import time

def show_message(message):
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.title("Benkosan")
    
    label = tk.Label(root, text=message, font=('微软雅黑', 18), wraplength=800)
    label.pack(padx=20, pady=20)
    
    def close_window():
        root.destroy()
    
    root.mainloop()

while True:
    time.sleep(1200)
    reply = checkScreen()
    if reply:
        show_message(reply)

