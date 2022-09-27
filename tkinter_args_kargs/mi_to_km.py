from tkinter import *

window = Tk()

window.title('Mile to Km Converter')
window.minsize(width=200, height=100)
window.config(padx=25, pady=25)

def calculate_km():
  km_label.config(text=f'{(float(mi_input.get()) * 1.60934)}')

label1 = Label(text='is equal to', font=(('Ariel', 12)))
label1.grid(column=0, row=1)

mi_input = Entry(width=10)
mi_input.grid(column=1, row=0)

km_label = Label(text=0, font=(('Ariel', 12)))
km_label.grid(column=1, row=1)

calc_btn = Button(text='Calculate', command=calculate_km)
calc_btn.grid(column=1, row=2)

mi_label = Label(text='Miles', font=(('Ariel', 12)))
mi_label.grid(column=2, row=0)

km_label2 = Label(text='Km', font=(('Ariel', 12)))
km_label2.grid(column=2, row=1)

window.mainloop()
