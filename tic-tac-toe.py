def tab_printing(ch_l):
    a = 0
    print('---------')
    final_list = list()
    for i in range(1, 4):
        temp_l = list()
        print('| ', end='')
        for j in range(0, 3):
            if ch_l[a] == '_':
                print(" ", end=' ')
                temp_l.append(ch_l[a])
                a = a + 1
            else:
                print(ch_l[a], end=' ')
                temp_l.append(ch_l[a])
                a = a + 1
        print('|')
        final_list.append(temp_l)
    print('---------')
    return final_list


def coordinates_range_check(co_l):
    co_list = co_l.split()
    for ch_x in co_list:
        t = int(ch_x)
        if t > 3:
            print('Coordinates should be from 1 to 3!')
            return -1
        if t not in numbers:
            print('You should enter numbers!')
            return -1


def empty_coordinates_check(co_l, f_m, s):
    # (1, 3) (2, 3) (3, 3)
    # (0, 0) (0, 1) (0, 2)

    # (1, 2) (2, 2) (3, 2)
    # (1, 0) (1, 1) (1, 2)

    # (1, 1) (2, 1) (3, 1)
    # (2, 0) (2, 1) (2, 2)
    co_list = co_l.split()
    x_co = int(co_list[0])
    y_co = int(co_list[1])
    x_final = 0
    y_final = 0
    if y_co == 3:
        x_final = 0
        y_final = x_co - 1
    if y_co == 2:
        x_final = 1
        y_final = x_co - 1
    if y_co == 1:
        x_final = 2
        y_final = x_co - 1
    if f_m[x_final][y_final] != '_':
        print('This cell is occupied! Choose another one!')
        return -1
    else:
        f_m[x_final][y_final] = s
        return f_m


def updated_matrix_printing(f_m):
    print("---------")
    for lists in f_m:
        print('|', end=' ')
        for char_1 in lists:
            if char_1 == '_':
                print(' ', end=' ')
            else:
                print(char_1, end=' ')
        print('|')
    print("---------")


def win_lose(ch):
    x = list()
    o = list()
    # Cases for X to win
    if ch[0] == 'X':
        if ch[0] == ch[1] and ch[1] == ch[2]:
            x.append('1')
        else:
            x.append('0')
    if ch[3] == 'X':
        if ch[3] == ch[4] and ch[4] == ch[5]:
            x.append('1')
        else:
            x.append('0')
    if ch[6] == 'X':
        if ch[6] == ch[7] and ch[7] == ch[8]:
            x.append('1')
        else:
            x.append('0')
    if ch[0] == 'X':
        if ch[0] == ch[3] and ch[3] == ch[6]:
            x.append('1')
        else:
            x.append('0')
    if ch[1] == 'X':
        if ch[1] == ch[4] and ch[4] == ch[7]:
            x.append('1')
        else:
            x.append('0')
    if ch[2] == 'X':
        if ch[2] == ch[5] and ch[5] == ch[8]:
            x.append('1')
        else:
            x.append('0')
    if ch[0] == 'X':
        if ch[0] == ch[4] and ch[4] == ch[8]:
            x.append('1')
        else:
            x.append('0')
    if ch[2] == 'X':
        if ch[2] == ch[4] and ch[4] == ch[6]:
            x.append('1')
        else:
            x.append('0')
    # Cases for win
    if ch[0] == 'O':
        if ch[0] == ch[1] and ch[1] == ch[2]:
            o.append('1')
        else:
            o.append('0')
    if ch[3] == 'O':
        if ch[3] == ch[4] and ch[4] == ch[5]:
            o.append('1')
        else:
            o.append('0')
    if ch[6] == 'O':
        if ch[6] == ch[7] and ch[7] == ch[8]:
            o.append('1')
        else:
            o.append('0')
    if ch[0] == 'O':
        if ch[0] == ch[3] and ch[3] == ch[6]:
            o.append('1')
        else:
            o.append('0')
    if ch[1] == 'O':
        if ch[1] == ch[4] and ch[4] == ch[7]:
            o.append('1')
        else:
            o.append('0')
    if ch[2] == 'O':
        if ch[2] == ch[5] and ch[5] == ch[8]:
            o.append('1')
        else:
            o.append('0')
    if ch[0] == 'O':
        if ch[0] == ch[4] and ch[4] == ch[8]:
            o.append('1')
        else:
            o.append('0')
    if ch[2] == 'O':
        if ch[2] == ch[4] and ch[4] == ch[6]:
            o.append('1')
        else:
            o.append('0')
    # conditions for win
    if x.count('1') in x > 1:
        print('Impossible')
        return 1
    elif o.count('1') in o > 1:
        print('Impossible')
        return 1
    elif '1' in x and '1' in o:
        print('Impossible')
        return 1
    elif '1' in x:
        print('X wins')
        return 1
    elif '1' in o:
        print('O wins')
        return 1
    elif ch[len(ch) - 1] == '_':
        return -1
    elif '_' in ch:
        return -1
    else:
        if '1' not in x and '1' not in o:
            print('Draw')


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = list("_________")
final_matrix = tab_printing(c)
f = 1
print_char = ['X', 'O']
pos = 0
while f > 0:
    count = 0
    co = input('Enter the coordinates: > ')
    r1 = coordinates_range_check(co)
    if r1 == -1:
        continue
    count = 0
    for ch_list in final_matrix:
        for ch_list_1 in ch_list:
            if ch_list_1 == '_':
                count = count + 1
    if count % 2 != 0:
        pos = 0
    else:
        pos = 1
    r2 = empty_coordinates_check(co, final_matrix, print_char[pos])
    if r2 == -1:
        continue
    else:
        final_matrix = r2
        updated_matrix_printing(final_matrix)
        final_ch = list()
        for temp_list in final_matrix:
            for char in temp_list:
                final_ch.append(char)
        result = win_lose("".join(final_ch))
        if result == 1:
            break
        x_1 = 0
        for li in final_matrix:
            if '_' in li:
                x_1 = -1
                continue
        if x_1 == 0:
            f = -1
