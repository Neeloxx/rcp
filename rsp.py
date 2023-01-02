import random
computer1 = 0
user1 = 0
while computer1 < 3 and user1 < 3:
    user = input('vvedite deistvie')
    computer = random.choice(['r', 's', 'p'])
    print('comp vibral', computer)
    if user == computer:
            print('rovno')
    elif user == 'r':
        if computer == 's':
                print('igrok pobedil')
                user1 += 1
        elif computer == 'p':
                print('comp pobedil')
                computer1 += 1
    elif user == 's':
        if computer == 'r':
                print('comp pobedil')
                computer1 += 1
        elif computer == 'p':
                print('Igrok pobedil')
                user1 += 1
    elif user == 'p':
        if computer == 'r':
                print('Igrok pobedil')
                user1 += 1
        elif computer == 's':
                print('Comp pobedil')
                computer1 += 1
    print('s4et', user1,  ':', computer1)
if user1 > computer1:
    print('igrok pobedil')
else:
    print('igrok proigral')
