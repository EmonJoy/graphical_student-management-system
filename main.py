from tkinter import *
root = Tk()
root.geometry("744x354")
root.configure(bg='grey')
root.title("Student management system develop by Emon Joy")

# Saving the submitted value as a txt file in the current program directory.
def store():
    print('****Submitting form*****')
    print(f'{dateValue.get(), nameValue.get(), classValue.get(), rollValue.get()}')
    with open('my_management.text', 'a') as f:
        f.write(f'{dateValue.get(), nameValue.get(), classValue.get(), rollValue.get()}\n')



Label(root, text='Student Management System', bg='gray', fg='black', font='arial 24 bold').grid(row=1, column=4)
Label(root, text='date: ', bg='gray', fg='black', font='arial 20 bold').grid(row=2, column=1, pady=8)
Label(root, text='Name: ', bg='gray', fg='black', font='arial 20 bold').grid(row=3, column=1, pady=8)
Label(root, text='Class: ', bg='gray', fg='black', font='arial 20 bold').grid(row=4, column=1, pady=8)
Label(root, text='Roll: ', bg='gray', fg='black', font='arial 20 bold').grid(row=5, column=1, pady=8)

dateValue = StringVar()
nameValue = StringVar()
classValue = StringVar()
rollValue = StringVar()

#----Creating entry------

dateEnt= Entry(root, textvariable=dateValue,font='arial 20 bold')
nameEnt= Entry(root, textvariable=nameValue,font='arial 20 bold')
classEnt= Entry(root, textvariable=classValue,font='arial 20 bold')
rollEnt= Entry(root, textvariable=rollValue,font='arial 20 bold')

dateEnt.grid(row=2, column=2)
nameEnt.grid(row=3, column=2)
classEnt.grid(row=4, column=2)
rollEnt.grid(row=5, column=2)

Button(root, text='Submit',font='arial 20 bold', bg='red', command=store).grid(row=6, column=2)



root.mainloop()
