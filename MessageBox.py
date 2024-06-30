from Agent import checkScreen
import tkinter as tk
from tkinter import messagebox
import time

while True:
    time.sleep(1200)
    reply = checkScreen()
    if reply:
        root = tk.Tk()
        root.withdraw()
        root.lift()
        root.attributes('-topmost', True)
        messagebox.showinfo("Benkosan", reply)
        root.attributes('-topmost', False)


