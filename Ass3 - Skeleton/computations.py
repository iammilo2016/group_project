from constants import *


def computeRoomArea(menuOption):
    '''
        Computes the area based on the type of room.
        if menuOption = 1  Calls computeRectangleWallsArea()
        if menuOption = 2 calls computeSquareWallsArea()
        if menuOption = 3 calls computeCustomWallsArea()
        Arguments: none
        Returns: area of room in square feet
    '''
    if menuOption == 1:
        RectangleArea = computeRectangleWallsArea()
        print('')
        return RectangleArea
    elif menuOption == 2:
        SquareWallsArea = computeSquareWallsArea()
        print('')
        return SquareWallsArea
    else:
        CustomWallsArea = computeCustomWallsArea()
        print('')
        return CustomWallsArea
    
def computeRectangleWallsArea():
    '''
    Asks the user to enter the length, width and height 
    and calculates the surface area to be painted in the room.
    
    Arguments: None
    Returns: area of the walls
    '''
    l = float(input("Enter the length of the room in feet:"))
    w = float(input("Enter the width of the room in feet:"))
    h = float(input("Enter the height of the room in feet:"))

    area = (2*w*h ) + (2*l*h)
    return area



def computeRectangleArea(length, width):
    '''
    Computes and returns the area of a rectangle with the specified
    length and width.
    Parameters:
        length - length of rectangle
        width - width of rectangle
    Returns: area - area of rectangle
    '''
    pass
 
def computeSquareWallsArea():
    '''
    Asks the user to enter the length and height 
    and calculates the surface area to be painted in the room 
    and returns area.
    Arguments: None
    Returns: area of the walls
    '''
    l = float(input("Enter the length of the room in feet:"))
    w = float(input("Enter the width of the room in feet:"))
    area = 4*l*w
    return area

def computeWindowsDoorsArea(numberOfWindows):
    '''
    Takes the number of windows/doors in a room as a parameter 
    and calculates the area for every door or window.  
    Returns the total area of all windows/doors in a room
    Parameters: numberOfWindows - # of windows in the room
    Returns: area of the all the windows
    '''
    i = 0
    totalArea = 0
    while i < (numberOfWindows):
        i += 1
        l = float(input(f"Enter length for window/door {i} in feet: "))
        w = float(input(f"Enter width for window/door {i} in feet: "))
        totalArea += (l*w)
    return totalArea


def computeCustomWallsArea():
    '''
    Asks the user to specify the number of walls in that 
    room and calculates the room area. 
    Parameters: None
    Returns: area - wall area of the custom room
    '''
    wallNum = int(input("How many walls are there in the room? "))
    totalArea = 0
    i = 0
    while i < wallNum:
        i += 1
        l = float(input(f"Enter length for window/door {i} in feet: "))
        w = float(input(f"Enter width for window/door {i} in feet: "))
        totalArea += (l*w)
    return totalArea

        #add enter length n width {i}
        #total area += (l*h)
        #return totalarea




    