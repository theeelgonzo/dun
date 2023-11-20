# define active scanning

def activeScan(scanRange, startCoordinates):
    xOne, yOne = startCoordinates[0], startCoordinates[1]

    levelOne = 12
    levelTwo = 23
    levelThree = 45

    print("What level scan will you perform?\n")
    level = input("1?\n2?\n3?\n")
    match level:
        case "1":
            theta = int(levelOne)
        case "2":
            theta = int(levelTwo)
        case "3":
            theta = int(levelThree)
        case _:
            "Try something else"


