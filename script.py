import time #We import time for the time.sleep() function
import sys #We import sys for the sys.exit() function

def pause():
    program_pause = input("Press <Enter> for continue...")

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

print(' ')

print(f'Welcome to your temporal narrative, {user_name}. Remember that, unlike this modern world, here you will be responsible for every decision you make.')

print(' ')

pause()

print('Now choose your genre: (1, 2 or 3)')
print('1) Male')
print('2) Female')
print("3) I'm an unemployed indecisive hippie")

user_genre = input().lower()

if(user_genre == '1') or (user_genre == 'male'):
    print(f'The user genre is Male')

elif(user_genre == '2') or (user_genre == 'female'):
    print(f'The user gente is Female')

elif(user_genre == '3') or (user_genre == 'hippie'):
    print(f'The user genre is Neutral')

else:
    print(f'wrong')
    sys.exit()