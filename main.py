#name = 'Никита'
#id = 'MD20001432432552'
#balance = -290
#balance2 = 34.2
#boolean = False #True
# print(bool(0))
# variable
#print('Hello ' + 'Никита')
#print ('Ur id is ' + id)
import random

#score = int(input('Enter ur score'))
#if score == 66:
# print('U win')
#else:
#    print('U need more points')

lives = 3
You_win = random.randint( 0, 100)
check = int(input('19'))

while lives != 0:
    check = int(input('19'))
    if check == You_win:
        print('You win')
        break
    elif check > You_win:
        print('Ur number is more than need')
    elif check < You_win :
        print('Ur number is more than need')
    else:
        print('Wrong data input')
    lives = lives - 1
else:
    print('You_died')



