def make_bricks(small, big, goal):
    bigNeeded = goal // 5
    smallNeeded = goal % 5
    if big >= bigNeeded:
        return small >= smallNeeded
    else: 
        return (goal - big*5) <= small


assert(make_bricks(3, 1, 8) == True)
assert(make_bricks(3, 1, 9) == False)
assert(make_bricks(3, 2, 10) == True)
