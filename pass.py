import random
import string

def generate_password(min_len,numbers=True,special_char=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters=letters
    if numbers:
       characters+=digits
    if special_char:
        characters+=special
    
    pwd=""
    meet_criteria=False
    has_num=False
    has_special=False

    while not meet_criteria or len(pwd)<min_len:
        new_char=random.choice(characters)
        pwd+=new_char

        if new_char in digits:
            has_num=True
        elif new_char in special:
            has_special=True

        meet_criteria=True
        if numbers:
            meet_criteria=has_num
        if special_char:
            meet_criteria=meet_criteria and has_special
        
    return pwd

min_len=int(input('Enter the minum length: '))
has_num=input('Do you want to have numbers (Y/N)?').lower() =='y'
has_special=input('Do you want to have special characters (Y/N)?').lower()=='y'

pwd=generate_password(min_len,has_num,has_special)
print("The generated password =" ,pwd)