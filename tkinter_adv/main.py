from math import floor
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER ------------------------------- # 

class Timer:
  def __init__(self, window):
    self.window = window
    self.start_seconds = 15
    self.break_count = 0
    self.status = 'work'
    self.running = True
    self.workcycles = ''
    self.timer()

  def timer(self):
    minutes = floor(self.start_seconds / 60)
    seconds = self.start_seconds % 60
    
    if seconds < 10:
      seconds = f'0{seconds}'

    if minutes < 10:
      minutes = f'0{minutes}'

    canvas.itemconfig(timer_txt, text=f'{minutes}:{seconds}')

    if self.start_seconds > 0:
      self.start_seconds -= 1
    else:
      if self.status == 'work':
        self.workcycles += '✓'
        check_mark.config(text=self.workcycles)
        self.break_count += 1
        self.status = 'break'
        if self.break_count < 4:
          main_lbl.config(text = 'Break', fg=PINK)
          self.start_seconds = 5
        else:
          main_lbl.config(text = 'Break', fg=RED)
          self.start_seconds = 10
          self.break_count = 0
          self.workcycles = ''
          check_mark.config(text=self.workcycles)
      elif self.status == 'break':
        self.status = 'work'
        main_lbl.config(text = 'Work', fg=GREEN)
        self.start_seconds = 15
    
    self.after_id = self.window.after(1000, self.timer)


timer = None

def start_timer():
  global timer
  timer = Timer(window)
  main_lbl.config(text = 'Work', fg=GREEN)

def reset_timer():
  global timer
  if timer != None:
    timer.window.after_cancel(timer.after_id)
    timer = None
  canvas.itemconfig(timer_txt, text='00:00')
  check_mark.config(text='')
  main_lbl.config(text = 'Timer', fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Activity Alerts')
window.config(padx=25,pady=50,bg=YELLOW)

main_lbl = Label(text='Timer', bg=YELLOW, fg=GREEN, font=((FONT_NAME, 50)))
main_lbl.grid(column=1, row=0)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=tomato_img)
timer_txt = canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 35))
canvas.grid(column=1, row=1)

start_btn = Button(text='Start', highlightthickness=0, command = start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text='Reset', highlightthickness=0, command = reset_timer)
reset_btn.grid(column=2, row=2)

check_mark = Label(text='', fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()