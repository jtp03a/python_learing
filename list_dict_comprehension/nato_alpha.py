import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def make_nato_word():
  user_input = input('Type a word: ').upper()
  try:
    nato_word = [data_dict[letter] for letter in user_input]
  except KeyError:
    print('Only letters allowd in the word')
    make_nato_word()
  else:
    print(nato_word)

make_nato_word()

# def convert_word(word):
#   nato_word = [get_nato_letter(letter.upper()) for letter in word]
#   return nato_word

# def get_nato_letter(inputletter):
#   for letter, nato_letter in data_dict.items():
#     if inputletter == letter:
#       return nato_letter

# print(convert_word(input('Enter a word to convert to the NATO alphabet: ')))