age: int
name: str
height: float
is_human: bool

age = "test"

# doesnt work

def police_check(age):
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

print(police_check(19))

if police_check("twelve"):
    print('You may pass')
else:
    print('Pay a fine')

