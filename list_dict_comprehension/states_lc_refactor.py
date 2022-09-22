from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title('US States Game')

image = 'blank_states_img.gif'
screen.addshape(image)

map = Turtle()
map.shape(image)
game_text = Turtle()
game_text.penup()
game_text.hideturtle()
 
def write_state(game_text_turtle, name, x, y):
  game_text_turtle.goto(x, y)
  game_text_turtle.write(name, align='center', font=('Ariel', 10, 'normal'))

data = pandas.read_csv('50_states.csv')
names = data['state'].to_list()
x = data['x'].to_list()
y = data['y'].to_list()

state_list = [(name, x[i], y[i]) for i, name in enumerate(names)]

# state_list = []
# for i, name in enumerate(names):
#   state_list.append((name, x[i], y[i]))

answer_count = 0

while len(state_list) > 0:
  answer_state = screen.textinput(title = f'{answer_count}/50 States Correct', prompt = 'What\'s another states name')
  answer_state = answer_state.lower()
  for state in state_list:
    lower_name = state[0].lower()
    if lower_name == answer_state:
      answer_count += 1
      write_state(game_text, state[0], state[1], state[2])
      state_list.remove(state)
  if answer_state == 'exit':
    break

# data = {
#   'state': []
# }

data = {'state':[state[0] for state in state_list]}

# for state in state_list:
#   data['state'].append(state[0])

state_data_frame = pandas.DataFrame(data)

state_data_frame.to_csv('states_to_learn.csv')

# screen.mainloop()