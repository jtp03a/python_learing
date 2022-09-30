import json
from tkinter import *
from tkinter import messagebox
import re
import random
import pyperclip

# ---------------------------- PASSWORD MANAGER  ------------------------------- #

class Password_Manager:
    def __init__(self, website_input, email_input, password_input):
      self.website_input = website_input
      self.email_input = email_input
      self.password_input = password_input

    def new_password(self):
    
      new_password = Password(self.website_input.get(), self.email_input.get(), self.password_input.get())

      self.password_dict = {
        'Website': new_password.website,
        'Email': new_password.email,
        'Password': new_password.password
      }

      input_validator = InputValidator()

      input_validator.cant_be_empty(self.password_dict)

      input_validator.valid_email(self.password_dict['Email'])

      input_validator.password_complexity(8, self.password_dict['Password'])
      
      if len(input_validator.errors) == 0:
        is_okay = messagebox.askokcancel(title=new_password.website, message=f'You Entered:\nEmail: {new_password.email}\nPassword: {new_password.password}\nIs this okay?')

        if is_okay: 
          self.save_pw()
      else:
        error_string = ''
        for error in input_validator.errors:
          error_string = error_string + error + '\n'
        
        messagebox.showerror(title='Errors', message=error_string)

    def random_password(self):
      letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
      numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

      letter_list = [random.choice(letters) for _ in range(random.randint(8, 10))]

      number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

      password_list = letter_list + number_list

      random.shuffle(password_list)

      password = ''.join(password_list)

      self.password_input.delete(0, END)
      self.password_input.insert(0, password)
      pyperclip.copy(password)
    
    def save_pw(self):
      with open('data.json', mode='r') as data:
        content = json.load(data)
        content['passwords'].append(self.password_dict)
        
      with open('data.json', mode='w') as data:
        data.write(json.dumps(content))
      
      self.reset_form()

    def reset_form(self):
      self.website_input.delete(0, END)
      self.password_input.delete(0, END)

class InputValidator:
  def __init__(self):
    self.errors = []

  def cant_be_empty(self, dict):
    for key, value in dict.items():
      if len(value) == 0:
        self.errors.append(f'{key} cannot be empty')

  def valid_email(self, email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if not re.fullmatch(regex, email):
      self.errors.append(f'Email is not a valid email format')

  def password_complexity(self, req_len, password):
    string_pattern = f'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{{{req_len},}}$'
    regex = re.compile(string_pattern)
    if not re.fullmatch(regex, password):
      self.errors.append(f'Password does not meet complexity requirements')


class Password:
  def __init__(self, website, email, password):
    self.website = website
    self.email = email
    self.password = password


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)

# Labels
website_lbl = Label(text='Website:')
email_lbl = Label(text='Email/Username:')
password_lbl = Label(text='Password:')

# Inputs
website_input = Entry(width=50)
email_input = Entry(width=50)
password_input = Entry(width=32)

password_manager = Password_Manager(website_input, email_input, password_input)

# Buttons
generate_pw_btn = Button(text='Generate Password', command= lambda: password_manager.random_password())
add_btn = Button(text='Add', width=43, command= lambda: password_manager.new_password())

# Render
# col 0
website_lbl.grid(column=0, row=1)
email_lbl.grid(column=0, row=2)
password_lbl.grid(column=0, row=3)
# col 1
canvas.grid(column=1, row=0)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'a3sir86@gmail.com')
password_input.grid(column=1, row=3)
add_btn.grid(column=1, row=4, columnspan=2)
# col 2
generate_pw_btn.grid(column=2, row=3)



window.mainloop()
