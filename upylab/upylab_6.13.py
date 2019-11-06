########################
## checking functions ##
########################

def checkset(s):
    res = True
    for n in range(1,10):
        if n not in s:
            res = False
    return res


def check_rows(grid):
    for r in grid:
        if checkset(r) == False:
            return False
    return True

def check_cols(grid):
    for c in range(9):
        g = []
        for r in range(9):
            g.append(grid[r][c])
        if checkset(g) == False:
            return False
    return True

def check_regions(grid):
    for c in range(0,9,3):
        for r in range(0,9,3):
            g = []
            for cc in range(3):
                for rr in range(3):
                    g.append(grid[c+cc][r+rr])
            if checkset(g) == False:
                return False
    return True

def check_sudoku(grid):
    if check_rows(grid) and check_cols(grid) and check_regions(grid):
        return True
    return False

####################
## code functions ##
####################

def concat(set1, set2, set3):
    res = set()
    for i in set1:
        res.add(i)
    for i in set2:
        res.add(i)
    for i in set3:
        res.add(i)
    return res


def getrowcontent(grid, r):
    res = set()
    for c in range(9):
        if grid[r][c] != 0:
            res.add(grid[r][c])
    return res

def getcolcontent(grid, c):
    res = set()
    for r in range(9):
        if grid[r][c] != 0:
            res.add(grid[r][c])
    return res

def getsqcontent(grid, r, c):
    res = set()

    for i in range((r // 3) * 3, ((r // 3) * 3) + 3):
        for j in range((c // 3) * 3, ((c // 3) * 3) + 3):
            if grid[i][j] != 0:
                res.add(grid[i][j])
    return res


def naked_single(grid):
    resg = grid
    ccontent = set()
    rcontent = set()
    scontent = set()
    fcontent = set()
    finish = False
    update = 1
    while finish == False and update != 0:
        update = 0
        finish = True
        for r in range(len(resg)):
            rcontent = getrowcontent(resg, r)
            for c in range(len(resg[r])):
                if resg[r][c] == 0:
                    finish = False
                    ccontent = getcolcontent(resg, c)
                    scontent = getsqcontent(resg, r, c)
                    fcontent = concat(rcontent, ccontent, scontent)
                    if len(fcontent) == 8:
                        miss = {1,2,3,4,5,6,7,8,9} - fcontent
                        resg[r][c] = miss.pop()
                        update += 1
    if finish == True:
        return (True, resg)
    else:
        return (False, None)


# print(naked_single([[4, 0, 3, 0, 9, 6, 0, 1, 0],
#                     [0, 0, 2, 8, 0, 1, 0, 0, 3],
#                     [0, 1, 0, 0, 0, 0, 0, 0, 7],
#                     [0, 4, 0, 7, 0, 0, 0, 2, 6],
#                     [5, 0, 7, 0, 1, 0, 4, 0, 9],
#                     [1, 2, 0, 0, 0, 3, 0, 8, 0],
#                     [2, 0, 0, 0, 0, 0, 0, 7, 0],
#                     [7, 0, 0, 2, 0, 9, 8, 0, 0],
#                     [0, 6, 0, 1, 5, 0, 3, 0, 2]]))

res = naked_single([[4, 0, 3, 0, 9, 6, 0, 1, 0],
                     [0, 0, 2, 8, 0, 1, 0, 0, 3],
                     [0, 1, 0, 0, 0, 0, 0, 0, 7],
                     [0, 4, 0, 7, 0, 0, 0, 2, 6],
                     [5, 0, 7, 0, 1, 0, 4, 0, 9],
                     [1, 2, 0, 0, 0, 3, 0, 8, 0],
                     [2, 0, 0, 0, 0, 0, 0, 7, 0],
                     [7, 0, 0, 2, 0, 9, 8, 0, 0],
                     [0, 6, 0, 1, 5, 0, 3, 0, 2]])
print(check_sudoku(res[1]))

# (True, [[4, 7, 3, 5, 9, 6, 2, 1, 8],
#        [6, 5, 2, 8, 7, 1, 9, 4, 3],
#        [9, 1, 8, 3, 2, 4, 5, 6, 7],
#        [3, 4, 9, 7, 8, 5, 1, 2, 6],
#        [5, 8, 7, 6, 1, 2, 4, 3, 9],
#        [1, 2, 6, 9, 4, 3, 7, 8, 5],
#        [2, 9, 5, 4, 3, 8, 6, 7, 1],
#        [7, 3, 1, 2, 6, 9, 8, 5, 4],
#        [8, 6, 4, 1, 5, 7, 3, 9, 2]])

print(naked_single([[0, 0, 6, 0, 4, 0, 1, 0, 0],
                    [0, 5, 0, 0, 9, 0, 0, 6, 0],
                    [8, 0, 0, 0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 3, 0, 4, 0, 0, 0],
                    [3, 1, 0, 0, 0, 0, 0, 4, 8],
                    [0, 0, 0, 8, 0, 7, 0, 0, 0],
                    [6, 0, 0, 0, 0, 0, 0, 0, 9],
                    [0, 2, 0, 0, 3, 0, 0, 5, 0],
                    [0, 0, 1, 0, 5, 0, 7, 0, 0]]))

# (False, None)