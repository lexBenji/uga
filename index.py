from time import sleep as delay

x=1
y=1
py=y
px=x

l = [
'11111111',
'10000001',
'10000001',
'13300001',
'11110111',
'55510155',
'11110111',
'10000031',
'11111111'
]
m = [list(x) for x in l]
items = ['sword','shield']
citem = ''
while True:
    print('\033c',end='')
    m[py][x] = m[py][x].replace('2','0')
    m[y][px] = m[y][px].replace('2','0')
    m[y][x] = '2'
    print(y,x)
    print(py,px)
    print(m[y-1])
    print(m[y])
    print(m[y+1])
    for i in m:
        for j in i:
            if j == '0':
                print('.',end='')
            elif j == '1':
                print('#',end='')
            elif j == '2':
                print('@',end='')
            elif j == '3':
                print('=',end='')
            elif j == '5':
                print(' ',end='')
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
            if m[y-1][x] == '3' and citem == 'sword':
                m[y-1][x] = m[y-1][x].replace('3','0')
            else:
                pass
        else:
            py = y
            y = y - 1
    elif move == 's':
        if m[y+1][x] == '3' or m[y+1][x] == '1':
            if m[y+1][x] == '3' and citem == 'sword':
                m[y+1][x] = m[y+1][x].replace('3','0')
            else:
                pass
        else:
            py = y
            y = y + 1
    elif move == 'd':
        if m[y][x+1] == '3' or m[y][x+1] == '1':
            if m[y][x+1] == '3' and citem == 'sword':
                m[y][x+1] = m[y][x+1].replace('3','0')
            else:
                pass
        else:
            px = x
            x = x + 1
    elif move == 'a':
        if m[y][x-1] == '3' or m[y][x-1] == '1':
            if m[y][x-1] == '3' and citem == 'sword':
                m[y][x-1] = m[y][x-1].replace('3','0')
            else:
                pass
        elif x-1 == 0:
            pass
        else:
            px = x
            x = x - 1
    elif move == 'i':
        print('\033c',end='')
        print(f'Current item: {citem}')
        g = False
        while True:
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
        print(f'Item {item} chose.')
        citem = item
        delay(1)