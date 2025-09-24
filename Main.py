from Profil import profilcheckcreation
from Password_strenght import check_password_strength
from Password_handling import add_password, save_file, view_file, search_password, delect_password

login_person = profilcheckcreation()

while True:
        print("what do you want to perform :\n" \
        "1 - Add a new password.\n" \
        "2 - search for password.\n" \
        "3 - delete a password.\n" \
        "4 - view passwords.\n" \
        "5 - exit")

        y = input("Your choice : ")

        if y == "1":
                application, profil_name, encrypted_password = add_password(login_person)
                save_file(profil_name, application, login_person, encrypted_password)   
        elif y == "2":
                search_password(login_person)
        elif y == "3":
                delect_password(login_person)
        elif y == '4':
                view_file(login_person)
        elif y == '5':
                input('exiting program...')
                break