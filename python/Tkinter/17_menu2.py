
import tkinter as tk
from tkinter import Label, LabelFrame, Menu, ttk
from tkinter.constants import PAGES
from typing import Text
win=tk.Tk()
win.title('Meanu bar')

# _____--------_____________------------=========>>>
def func():
    print('func is called')
# _____--------_____________------------=========>>>
# # simple
# menubar=tk.Menu(win)

# menubar.add_command(label='save', command=func)
# menubar.add_command(label='copy', command=func)
# menubar.add_command(label='paste', command=func)
# menubar.add_command(label='cut', command=func)

# win.config(menu=menubar)


# _____--------_____________------------=========>>>
# cascade
# main_meanu
 
main_meanu=tk.Menu(win)
file_Menu=tk.Menu(main_meanu, tearoff=0)
file_Menu.add_command(label='newfile', command=func)
file_Menu.add_command(label='save as', command=func)
file_Menu.add_separator()
file_Menu.add_command(label='delete', command=func)
#edit menu
edit_menu=tk.Menu(main_meanu,tearoff=0)
edit_menu.add_command(label='redo',command=func)
edit_menu.add_command(label='undo',command=func)
edit_menu.add_separator()
edit_menu.add_command(label='edo',command=func)


main_meanu.add_cascade(label='file',menu=file_Menu)#file
main_meanu.add_cascade(label='edit',menu=edit_menu)#edit





win.config(menu=main_meanu)

win.mainloop()