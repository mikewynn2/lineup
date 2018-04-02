import random

# barge knowledge
a = ['acro 2', 'acro 3', 'acro 4', 'acro 11', 'acro 14']
b = ['acro 1', 'acro 5', 'acro 9', 'acro 10', 'acro 12', 'acro 15']
c = ['acro 4', 'acro 6', 'acro 9', 'acro 11', 'acro 13', 'acro 14']
d = ['acro 5', 'acro 6', 'acro 7', 'acro 8', 'acro 10', 'acro 15']
e = ['acro 5', 'acro 6', 'acro 8', 'acro 10', 'acro 11']
f = ['acro 2', 'acro 3', 'acro 4', 'acro 6', 'acro 9', 'acro 11', 'acro 13', 'acro 14']
g = ['acro 1', 'acro 5', 'acro 9', 'acro 10', 'acro 12', 'acro 15']
h = ['acro 2', 'acro 5', 'acro 7', 'acro 9', 'acro 10', 'acro 13']


# poles knowledge
r1 = ['acro 1', 'acro 2', 'acro 3', 'acro 4', 'acro 5', 'acro 6', 'acro 7',
      'acro 8', 'acro 9', 'acro 10', 'acro 11', 'acro 12',
      'acro 13', 'acro 14', 'acro 15']

l1 = ['acro 1', 'acro 2', 'acro 3', 'acro 4', 'acro 5', 'acro 6', 'acro 7',
      'acro 8', 'acro 9', 'acro 10', 'acro 11', 'acro 12',
      'acro 13', 'acro 14', 'acro 15']

r2 = ['acro 1', 'acro 2', 'acro 3', 'acro 4', 'acro 5', 'acro 6', 'acro 7',
      'acro 8', 'acro 9', 'acro 10', 'acro 11', 'acro 12',
      'acro 13', 'acro 14', 'acro 15']

l2 = ['acro 1', 'acro 2', 'acro 3', 'acro 4', 'acro 5', 'acro 6', 'acro 7',
      'acro 8', 'acro 9', 'acro 10', 'acro 11', 'acro 12',
      'acro 13', 'acro 14', 'acro 15']

flag = ['acro 1', 'acro 5', 'acro 8', 'acro 10', 'acro 13', 'acro 15']
shoulder = ['acro 3', 'acro 4', 'acro 5', 'acro 9', 'acro 10', 'acro 15']
circle = ['acro 1', 'acro 5', 'acro 8', 'acro 10']
jump = ['acro 1', 'acro 6', 'acro 8', 'acro 9', 'acro 13', 'acro 14']

# barge scheduler


def tramp(a, b, c, d, e, f, g, h):
    barge = []
    while len(barge) < 8:
        barge = []
        used = {}

        alpha = random.choice(a)
        if alpha not in used:
            barge.append(alpha)
            used[alpha] = True

        bravo = random.choice(b)
        if bravo not in used:
            barge.append(bravo)
            used[bravo] = True

        charlie = random.choice(c)
        if charlie not in used:
            barge.append(charlie)
            used[charlie] = True

        delta = random.choice(d)
        if delta not in used:
            barge.append(delta)
            used[delta] = True

        echo = random.choice(e)
        if echo not in used:
            barge.append(echo)
            used[echo] = True

        foxtrot = random.choice(f)
        if foxtrot not in used:
            barge.append(foxtrot)
            used[foxtrot] = True

        golf = random.choice(g)
        if golf not in used:
            barge.append(golf)
            used[golf] = True

        hotel = random.choice(h)
        if hotel not in used:
            barge.append(hotel)
            used[hotel] = True
    return barge


barge = tramp(a, b, c, d, e, f, g, h)


def poles(r1, r2, l1, l2, flag, shoulder, circle, jump):
    poles = []
    tries = 0
    while len(poles) < 8:
        poles = []
        used2 = {}

        flag_track = random.choice(flag)
        if flag_track not in used2 and flag_track in barge:
            poles.append(flag_track)
            used2[flag_track] = True

        shoulder_hop_track = random.choice(shoulder)
        if shoulder_hop_track not in used2 and shoulder_hop_track in barge:
            poles.append(shoulder_hop_track)
            used2[shoulder_hop_track] = True

        circle_climb_track = random.choice(circle)
        if circle_climb_track not in used2 and circle_climb_track in barge:
            poles.append(circle_climb_track)
            used2[circle_climb_track] = True

        jump_track = random.choice(jump)
        if jump_track not in used2 and jump_track in barge:
            poles.append(jump_track)
            used2[jump_track] = True

        r1_track = random.choice(r1)
        if r1_track not in used2 and r1_track in barge:
            poles.append(r1_track)
            used2[r1_track] = True

        l1_track = random.choice(l1)
        if l1_track not in used2 and l1_track in barge:
            poles.append(l1_track)
            used2[l1_track] = True

        r2_track = random.choice(r2)
        if r2_track not in used2 and r2_track in barge:
            poles.append(r2_track)
            used2[r2_track] = True

        l2_track = random.choice(l2)
        if l2_track not in used2 and l2_track in barge:
            poles.append(l2_track)
            used2[l2_track] = True
        # tries += 1
        # print(tries)
    return poles

# output schedule


def output(tramp):
    print('Alpha: ', barge[0])
    print('Bravo: ', barge[1])
    print('Charlie: ', barge[2])
    print('Delta: ', barge[3])
    print('Echo: ', barge[4])
    print('Foxtrot: ', barge[5])
    print('Golf: ', barge[6])
    print('Hotel: ', barge[7])


def output2(poles):
    print('Flag: ', poles[0])
    print('Shoulder Hop: ', poles[1])
    print('Circle Climb: ', poles[2])
    print('Jump: ', poles[3])
    print('R1: ', poles[4])
    print('L1: ', poles[5])
    print('R2: ', poles[6])
    print('L2: ', poles[7])


# output(tramp(a, b, c, d, e, f, g, h))
output2(poles(r1, r2, l1, l2, flag, shoulder, circle, jump))
output(tramp(a, b, c, d, e, f, g, h))
