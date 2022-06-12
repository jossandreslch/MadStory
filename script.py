import time #We import time for the time.sleep() function
import sys #We import sys for the sys.exit() function

# function for the "Press Enter" parts of the script.
def pause():
    program_pause = input("Press <Enter> for continue...")

# Dictionary of random Words related to the user's profile.
# La idea es crear un diccionario por cada ideologia del user, y asi cuando el mismo seleccione su ideología post-nacimiento, las variables de los diccionarios se reemplacen correspondientemente

user_right = {
    'adjetives':['greedy', 'billionaire', 'corporate', 'capitalist', 'libertarian'],
    'countries':['USA', 'Canada', 'England', 'Germany', 'Poland'],
}

print('▄▄▌ ▐ ▄▌▄▄▄ .▄▄▌   ▄▄·       • ▌ ▄ ·. ▄▄▄ .    ▄▄▄▄▄      ')
print('██· █▌▐█▀▄.▀·██•  ▐█ ▌▪▪     ·██ ▐███▪▀▄.▀·    •██  ▪     ')
print('██▪▐█▐▐▌▐▀▀▪▄██▪  ██ ▄▄ ▄█▀▄ ▐█ ▌▐▌▐█·▐▀▀▪▄     ▐█.▪ ▄█▀▄ ')
print('▐█▌██▐█▌▐█▄▄▌▐█▌▐▌▐███▌▐█▌.▐▌██ ██▌▐█▌▐█▄▄▌     ▐█▌·▐█▌.▐▌')
print(' ▀▀▀▀ ▀▪ ▀▀▀ .▀▀▀ ·▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀      ▀▀▀  ▀█▄▀▪')

print(' ███▄ ▄███▓ ▄▄▄      ▓█████▄   ██████ ▄▄▄█████▓ ▒█████   ██▀███ ▓██   ██▓')
print('▓██▒▀█▀ ██▒▒████▄    ▒██▀ ██▌▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▒██  ██▒')
print('▓██    ▓██░▒██  ▀█▄  ░██   █▌░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒ ▒██ ██░')
print('▒██    ▒██ ░██▄▄▄▄██ ░▓█▄   ▌  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄   ░ ▐██▓░')
print('▒██▒   ░██▒ ▓█   ▓██▒░▒████▓ ▒██████▒▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒ ░ ██▒▓░')
print('░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ██▒▒▒ ')
print('░  ░      ░  ▒   ▒▒ ░ ░ ▒  ▒ ░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░▓██ ░▒░ ')
print('░      ░     ░   ▒    ░ ░  ░ ░  ░  ░    ░      ░ ░ ░ ▒    ░░   ░ ▒ ▒ ░░  ')
print('       ░         ░  ░   ░          ░               ░ ░     ░     ░ ░     ')
print('                      ░                                          ░ ░     ')

time.sleep(1.5)

print('Please, choose your name:')
user_name = str(input()).title()

time.sleep(1)

print(' ')

print(f'Welcome to your temporal narrative, {user_name}. Remember that, unlike in this modern world, here you will be responsible for every decision you make.')

print(' ')

time.sleep(2.5)


pause()

print(' ')
time.sleep(1)

print('Now choose your genre: (1, 2 or 3)')
print('1) Male')
print('2) Female')
print("3) I can be both ;)")

user_genre = input().lower()

#Secuencia de preguntas para input
i = 0
while (user_genre != '1') and (user_genre != 'male') and (user_genre != 'm') and (user_genre != '2') and (user_genre != 'female') and (user_genre != 'f') and (user_genre != '3') and (user_genre != 'hippie') and (user_genre != 'n') and (i<3):

    print(' ')
    time.sleep(1)

    print(f'Sorry, {user_name}, the selected option is invalid, please try again (1, 2 or 3):')
    user_genre = input().lower()
    i=i+1

if(user_genre == '1') or (user_genre == 'male') or (user_genre == 'm'):
    print(f'The user genre is Male')

elif(user_genre == '2') or (user_genre == 'female') or (user_genre == 'f'):
    print(f'The user genre is Female')

elif(user_genre == '3') or (user_genre == 'hippie') or (user_genre == 'n'):
    
    time.sleep(1)
    print(f'Oh...')
    time.sleep(1.5)
    print(f'You naughty {user_name}...')
    time.sleep(1)


else:
    print(f"Alright, {user_name}, I can see you can't read. Come back when you learn.")
    sys.exit()


time.sleep(1.5)

#Acá finaliza la Secuencia de preguntas para input

print(' ')

print(f'Alright, {user_name}, now tell me, how old are you?')

user_age = int(input())

i=0
while i<3 and user_age<14 or user_age>100:

    print(' ')
    time.sleep(1)

    print(f'You think you are funny, isn`t it?, come on {user_name}, stop the jokes and tell me your real age:')
    user_age = int(input())
    i=i+1
if (user_age < 25 and user_age > 14):
    time.sleep(1)
    print(f"Nice... young blood to the ring...")
    time.sleep(1.5)
elif (user_age > 25 and user_age < 100):
    time.sleep(1)
    print(f"Nice, I hope you are an experienced decision maker...")
    time.sleep(1.5)
# With this Else statement the script will cut out
else:
    time.sleep(1.5)
    print(f"{user_name}, I see that you can not read, that age is not allowed to this. See ya later.")
    sys.exit()

# In here the script continues

time.sleep(1.5)
print(f"Alright, {user_name}, so now I know that you have {user_age} years old, but I don't care anyways...")
time.sleep(4);
print(f'...because this is a new Mad Story...')
time.sleep(3);

pause()

# This is the START of the Story/Game



# User's Data Check
time.sleep(2);
print(f"User's Data Base:")
print(f"User's Name = {user_name}");
print(f"User's Genre = {user_genre}");
print(f"User's Age = {user_age}");