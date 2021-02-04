import tkinter

main_window =tkinter.Tk()

def event_button():
    label2 = tkinter.Label(main_window, text="button pressed")
    label2.pack()

label = tkinter.Label(main_window, text="Hello World \n Hello Me")
tombol = tkinter.Button(main_window, text="button",command = event_button)



label.pack()
tombol.pack()
main_window.mainloop()


