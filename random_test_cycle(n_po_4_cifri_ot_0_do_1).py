import random


def loto():
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    win1 = random.choice(tickets)
    win2 = random.choice(tickets)
    win3 = random.choice(tickets)
    rnd = float(f'0.{win1}{win2}{win3}')
    return rnd


def rnd_4(a):
    rnd4 = [loto(), loto(), loto(), loto()]
    print(f'{a}', rnd4)


while 1 > 0:
    count = int(input('сколько четверок надо?'))
    if count > 100:
        print('многовато, давай поменьше')
        continue
    else:
        for i in range(count):
            rnd_4(i + 1)
        else:
            continue
