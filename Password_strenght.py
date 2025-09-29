import re
import string
from Banner import typing_print

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

     match_lenght = len(password)
     match_alphabet_lower = re.search(alphabet_lower, password)
     match_alphabet_upper = re.search(alphabet_upper, password)
     match_digits = re.search(digits, password)
     match_special_chars = re.search(special_chars, password)

     x = 0
     if match_lenght >= 14:
          x = x + 1
     if match_alphabet_lower is None:
          match_alphabet_lower = True
          x = x + 1
     if match_alphabet_upper is None:
          match_alphabet_upper = True
          x = x + 1
     if match_digits is None:
          match_digits = True
          x = x + 1
     if match_special_chars is None:
          match_special_chars = True
          x = x + 1

     matches = [(match_alphabet_lower, "- Password must contain at least one lower case alphabet"), 
                 (match_alphabet_upper, "- Password must contain at leaste one uper case alphabet"), 
                 (match_digits, "- Passwod must contain at leaste one digit"), 
                 (match_special_chars, "- Password must contain at leaste one special keyword")]
     
     if x == 5:
          stars = '\nPassword strenght |#-#-#-#-#|>'
     elif x == 4:
          stars = '\nPassword strenght |#-#-#-#- |>'
     elif x == 3:
          stars = '\nPassword strenght |#-#-#- - |>'
     elif x == 2:
          stars = '\nPassword strenght |#-#- - - |>'
     elif x == 1:
          stars = '\nPassword strenght |#- - - - |>'
     elif x== 0:
          stars = '\nPassword strenght | - - - - |>'


     typing_print(f'{stars}\n', delay=0.01)

     for case, prblm in matches:
          if case is None:
               typing_print(f'{prblm}', delay=0.01)
     if match_lenght < 14 :
          print('- Lenght has to be minimum of 14 digits')

     print('\n')
     choice = input(typing_print('Do you want to use this password ? (y/n) : '))

     if choice == 'y':
          print()
     elif choice == 'n':
          print()
     else:
          typing_print('you did a mistake!')
     
     return choice