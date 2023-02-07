from time import sleep as delay

x=1
y=1
py=y
px=x

l = [
'1111111111111',
'1000000100001',
'1000000100001',
'1000000300001',
'1450006100001',
'1111311100001',
'0001000100001',
'0001000100001',
'0001000000001',
'0001111111111'
]
m = [list(x) for x in l]
items = ['hands','axe','shield']
citem = 'hands'
hp=10
k = 0
char = ['@',
        '%',
        '&',
        '$',
        'P'
        ]
while True:
    print('\033c',end='')
    if hp == 0:
        print('+-----------+')
        print('| You lose! |')
        print('+-----------+')
        break
    else:
        pass
    m[py][x] = m[py][x].replace('2','0')
    m[y][px] = m[y][px].replace('2','0')
    m[y][x] = '2'
    print(f'Health: {hp}/10')
    print('Current item:',citem)
    if hp <= 5:
        print('Don\'t punch doors!')
    else:
        print()
    for i in m:
        for j in i:
            if j == '0':
                print(' ',end='')
            elif j == '1':
                print('#',end='')
            elif j == '2':
                print(char[k],end='')
            elif j == '3':
                print('=',end='')
            elif j == '4' or j == '5' or j == '6':
                print('T',end='')
            else:
                print(j)
        print()
    move = input('').lower()
    if move == 'p':
        print('\033c',end='')
        print('      +-------------------------+')
        print('+-----| Press ENTER to continue |-----+')
        print('|     +-------------------------+     |')
        print('+---------+                +----------+')
        input()
    elif move == 'x':
        print('\033c',end='')
        exit()
    elif move == 'w':
        if m[y-1][x] == '3' or m[y-1][x] == '1':
            if m[y-1][x] == '3' and citem == 'axe':
                m[y-1][x] = m[y-1][x].replace('3','0')
            elif m[y-1][x] == '3' and citem == 'hands':
                hp = hp - 1
            else:
                continue
        elif m[y-1][x] == '4':
            print('\033c',end='')
            print('Tip: Press I to open item menu')
            delay(1)
        elif m[y-1][x] == '5':
            print('\033c',end='')
            print('Tip: Attack doors (=) with an axe to destroy them')
            delay(1)
        elif m[y-1][x] == '6':
            print('\033c',end='')
            print('Tip: Good luck')
            delay(1)
        else:
            py = y
            y = y - 1
    elif move == 's':
        if m[y+1][x] == '3' or m[y+1][x] == '1':
            if m[y+1][x] == '3' and citem == 'axe':
                m[y+1][x] = m[y+1][x].replace('3','0')
            elif m [y+1][x] == '3' and citem == 'hands':
                hp = hp - 1
            else:
                continue
        elif m[y+1][x] == '4':
            print('\033c',end='')
            print('Tip: Press I to open item menu')
            delay(1)
        elif m[y+1][x] == '5':
            print('\033c',end='')
            print('Tip: Attack doors (=) with an axe to desteoy them')
            delay(1)
        elif m[y+1][x] == '6':
            print('\033c',end='')
            print('Tip: Good luck')
            delay(1)
        else:
            py = y
            y = y + 1
    elif move == 'd':
        if m[y][x+1] == '3' or m[y][x+1] == '1':
            if m[y][x+1] == '3' and citem == 'axe':
                m[y][x+1] = m[y][x+1].replace('3','0')
            elif m[y][x+1] == '3' and citem == 'hands':
                hp = hp - 1
            else:
                continue
        elif m[y][x+1] == '4':
            print('\033c',end='')
            print('Tip: Press I to open item menu')
            delay(1)
        elif m[y][x+1] == '5':
            print('\033c',end='')
            print('Tip: Attack doors (=) with an axe to destroy them')
            delay(1)
        elif m[y][x+1] == '6':
            print('\033c',end='')
            print('Tip: Good luck')
            delay(1)
        else:
            px = x
            x = x + 1
    elif move == 'a':
        if m[y][x-1] == '3' or m[y][x-1] == '1':
            if m[y][x-1] == '3' and citem == 'axe':
                m[y][x-1] = m[y][x-1].replace('3','0')
            elif m[y][x-1] == '3' and citem == 'hands':
                hp = hp - 1
            else:
                continue
        elif m[y][x-1] == '4':
            print('\033c',end='')
            print('Tip: Press I to open item menu')
            delay(1)
        elif m[y][x-1] == '5':
            print('\033c',end='')
            print('Tip: Attack doors (=) with an axe to destroy them')
            delay(1)
        elif m[y][x-1] == '6':
            print('\033c',end='')
            print('Tip: Good luck')
            delay(1)
        else:
            px = x
            x = x - 1
    elif move == 'i':
        print('\033c',end='')
        print(f'Current item: {citem}')
        g = False
        while True:
            print('Shop: ',end='')
            for i in items:
               print(i,' ',end='')
            print()
            item = input('Choose your item: ')
            if item in items:
                for j in items:
                    if j == item:
                        g = True
                        break
            if g == True:
                break
        print('\033c',end='')
        print(f'Item {item} chosen.')
        citem = item
        delay(1)
    elif move == 'c':
        if k+1 == len(char):
            k = 0
        else:
            k+=1
