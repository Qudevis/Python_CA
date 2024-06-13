from tkinter import *

main_window = Tk()
main_window.geometry("500x500")

sb = Scrollbar(main_window)

box = Listbox(main_window, yscrollcommand=sb.set, selectmode=SINGLE) # yscrollcommand prisirisa prie scrolbaor pasukimo (sukasi, kai judiname scrollbara)
sb.config(command=box.yview) # scrollbaras prisirisa prie box ir juda kai judiname box

# box.insert(END,"Justas")

numbers = range(1,50)

box.insert(END,*numbers)

sb.pack(side=RIGHT, fill=Y)
box.pack(side=LEFT)

def print_list_item(x):
    print(box.curselection())
    print(box.curselection()[0])
    print(numbers[box.curselection()[0]])
    pass

box.bind("<Button-3>",lambda x: print(numbers[box.curselection()[0]]))

def sum(a,b):
    print(a+b)

but = Button(main_window,command= lambda: sum(4,9))

but.pack()

main_window.mainloop()

