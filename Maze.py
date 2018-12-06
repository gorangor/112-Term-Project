import random
def lstMaker(x):
    lst = []
    for num in range(0,x):
        lst.append([False]*x)
    return lst

def maze(lst, x, row = 1, col = 1):
    directions = [1,2,3,4]
    random.shuffle(directions)
    for dir in directions:
        lst[row][col] = True
        if dir == 1:
            if col - 2 > 0 and lst[row][col-2] is False:
                col = col - 2
                lst[row][col+1] = True
                lst = maze(lst, x, row, col)
        if dir == 2:
            if row + 2 < x-1 and lst[row+2][col] is False:
                row = row + 2
                lst[row -1][col] = True
                lst = maze(lst, x, row, col)
        if dir == 3:
            if col + 2 < x - 1 and lst[row][col+2] is False:
                col = col + 2
                lst[row][col - 1] = True
                lst = maze(lst, x, row, col)
        if dir == 4:
            if row - 2 > 0 and lst[row-2][col] is False:
                row = row - 2
                lst[row + 1][col] = True
                lst = maze(lst, x, row, col)
    return lst

def mazeDraw(lst):
    string = ""
    for rows in lst:
        for items in rows:
            if items == False:
                string += "X"
            else:
                string += "_"
        string += "\n"
    return string

print(mazeDraw(maze(lstMaker(15), 16)))
