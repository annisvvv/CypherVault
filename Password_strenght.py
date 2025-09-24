import re
import string

# Check for password strenght
def check_password_strength(password):
    '''This function checks for password strength, 
    the Password must contain at least: 
    .14 characters
    .1 uppercase/lowercase letter
    .1 digit
    .1 special character
    and must not contains any dictionary words, 
    common passwords or repetitive characters'''

    alphabet_lower = r"string.ascii_lowercase"
    alphabet_upper = r"string.ascii_uppercase"
    digits = r"string.digits"
    special_chars = r"string.punctuation"

    match_lenght = len(password) > 13
    match_alphabet_lower = re.search(alphabet_lower, password)
    match_alphabet_upper = re.search(alphabet_upper, password)
    match_digits = re.search(digits, password)
    match_special_chars = re.search(special_chars, password)
    
    if match_alphabet_lower is None:
         match_alphabet_lower = False
    if match_alphabet_upper is None:
         match_alphabet_upper = False
    if match_digits is None:
         match_digits = False
    if match_special_chars is None:
         match_special_chars = False

    matches = [(match_lenght, "Password lenght must be of 14 minimum") ,
                (match_alphabet_lower, "Password must contain at least one lower case alphabet"), 
                (match_alphabet_upper, "password must contain at leaste one uper case alphabet"), 
                (match_digits, "passwod must contain at leaste one digit"), 
                (match_special_chars, "password must contain at leaste one special keyword")]

    for matche, context in matches:
            if matche == False:
                print(context)