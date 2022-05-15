# hour : [0 - 23]
# trouble hours : (20 - 7)
def parrot_trouble(talking, hour):
    return talking and (hour > 20 or hour < 7)

assert(parrot_trouble(True, 6))
assert(not parrot_trouble(True, 7))
assert(not parrot_trouble(False, 6))
