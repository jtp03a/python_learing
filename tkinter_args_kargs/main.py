import tkinter

window = tkinter.Tk()
window.title('GUI learning with TKinter')
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text='A label', font=(('Ariel', 24, 'bold')))
my_label.pack()

my_label['text'] = 'New Text'


def button_clicked(txt):
  my_label.config(text = txt)

# button
button = tkinter.Button(text='Click Me', command= lambda: button_clicked('Test'))
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()

window.mainloop()