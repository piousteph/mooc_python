import random

def create_map(size, trapsNbr):
    res = {}
    i = 0

    while i <= trapsNbr:
        x = random.randint(1, size)
        y = random.randint(1, size)
        if res.get((x, y)) == None:
            if i == 0:
                res[(x, y)] = 1
            else:
                res[(x, y)] = -1
            i += 1
    return res

def play_game(map_size, treasure_map):
    finish = False
    res = False
    print(treasure_map)
    while finish == False:
        i = input().split()
        try:
            x = int(i[0])
            y = int(i[1])
        except:
            continue
        
        if len(i) == 2:
            r = treasure_map.get((x, y))
            if r == 1:
                finish = True
                res = True
            elif r == -1:
                finish = True
                res = False
    return res

print(create_map(4,5))
# {(3, 1): 1, (4, 2): -1, (1, 1): -1, (1, 4): -1, (2, 2): -1, (4, 4): -1}

# print(play_game(10, create_map(10, 5)))

