with open("./Input/Names/invited_names.txt", "r") as invited_names_txt:
    names_list = invited_names_txt.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as starting_letter_txt:
    template = starting_letter_txt.read()

for name in names_list:
    stripped_name = name.strip("\n")
    f = open(f"./Output/ReadyToSend/{stripped_name}_letter.txt", "w+")        
    f.write(template.replace('[name]', stripped_name))




