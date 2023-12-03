import math
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
            thetaOne = round(int(levelOne) / 2)
            thetaTwo = 360 - (round(int(levelOne) / 2))
            bc = 84
        case "2":
            thetaOne = round(int(levelTwo) / 2)
            thetaTwo = 360 - (round(int(levelTwo) / 2))
            bc = 78
        case "3":
            thetaOne = round(int(levelThree) / 2)
            thetaTwo = 360 - (round(int(levelThree) / 2))
            bc = 67
        case _:
            "Try something else"

    c = scanRange / math.sin(math.degrees(int(bc)))
    

    print("What is your bearing?\n")
    bearing = input()

    def calcEndPoint(bearing, length):
        if int(bearing) %  90 != 0:
            newX, newY = math.cos(math.radians(int(bearing))) * length, math.sin(math.radians(int(bearing))) * length
        elif int(bearing) == 0 or int(bearing) == 360:
            newX, newY = length, 0
        elif int(bearing) == 90:
            newX, newY = 0, length
        elif int(bearing) == 180:
            newX, newY = length * (-1), 0
        elif int(bearing) == 270:
            newX, newY = 0, length * (-1)

        else:
            pass
        
        scanPoint = [xOne + round(newX), yOne + round(newY)]
        print(scanPoint)

    calcEndPoint(bearing, scanRange)
    calcEndPoint(thetaOne, c)
    calcEndPoint(thetaTwo, c)

    #Code below stolen from Geeks for Geeks

    # A utility function to calculate area
# of triangle formed by (x1, y1),
# (x2, y2) and (x3, y3)

    def area(x1, y1, x2, y2, x3, y3):

	    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


# A function to check whether point P(x, y)
# lies inside the triangle formed by
# A(x1, y1), B(x2, y2) and C(x3, y3)
    def isInside(x1, y1, x2, y2, x3, y3, x, y):

	# Calculate area of triangle ABC
	    A = area (x1, y1, x2, y2, x3, y3)

	# Calculate area of triangle PBC
	    A1 = area (x, y, x2, y2, x3, y3)

	# Calculate area of triangle PAC
	    A2 = area (x1, y1, x, y, x3, y3)

	# Calculate area of triangle PAB
	    A3 = area (x1, y1, x2, y2, x, y)

	# Check if sum of A1, A2 and A3
	# is same as A
	    if(A == A1 + A2 + A3):
		    return True
	    else:
		    return False

# Driver program to test above function
# Let us check whether the point P(10, 15)
# lies inside the triangle formed by
# A(0, 0), B(20, 0) and C(10, 30)
    if (isInside(0, 0, 20, 0, 10, 30, 10, 15)):
	    print('Inside')
    else:
	    print('Not Inside')

# This code is contributed by Danish Raza


activeScan(10, [30,35])
