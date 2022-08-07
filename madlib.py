#Import section
from sample_madlib import hp,code, zombie, hungergame
import random

#main code
print('***** Welcome to the madlib game *****')
print('Do you want a random template game or a choice one?')
print('For a selection of game template please input Select')
print('For a random game template please input Random')
initial = input('Answer:')
if initial == 'Select':
    print('For hp game,Please press 1')
    print('For code game,Please press 2')
    print('For zombie game,Please press 3')
    print('For hunger game,Please press 4')
    select = input('Enter the one of above number:')

    if select == 1:
        m = hp
        m.madlib()
    elif select == 2:
        m = code
        m.madlib()
    elif select == 3:
        m = zombie
        m.madlib()
    else:
        m = hungergame
        m.madlib()

elif initial == 'Random':
    m = random.choice([hp, code, zombie, hungergame])
    m.madlib()
else:
    print('Please check the spelling again.')