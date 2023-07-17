from constants import *
from computations import *
from report import *
import math

def main():
    print('The Painter\'s Company Estimating Tool')
    getPaintPrice()
    getNumberOfCoats()
    getNumberRooms()
    
    '''
    Controls flow of the program. Gets the initial inputs, 
    iterates for the specified number of rooms, 
    calls appropriate functions, calculates, 
    and displays total paint required and cost.
    Arguments: None
    Returns: None
    '''
    pass

def getPaintPrice():
    enterpriceofPaint = float(input("Enter price of paint: "))
    
    return enterpriceofPaint
    '''
        Asks the user to enter the paint price and returns the value entered

        Returns:  paint price / gallon
    '''


def getNumberOfCoats():

    enterCoats = int(input("Enter number of coats of paint to apply (1-4): "))
    while enterCoats < 1 or enterCoats > 4:
        print("Error: Number of coats must be between 1 and 4")
        enterCoats = int(input("Enter number of coats of paint to apply (1-4): "))
    return enterCoats
    ''' 
        Asks the user to enter the number of coats of paint 
        to apply (1-4) and returns value entered. Error checks the
        input, must be in the range 1-4.

        Returns:  number of coats of paint
    '''

def getNumberRooms():
    enterRooms = int(input("How many rooms do you want to paint? "))
    return enterRooms
    '''  
       Asks the user to enter the number of rooms 
       to paint and returns value entered
          
        Returns: number of rooms
    '''
    pass

def roomsMenu(nbrOfRooms):
    roomMenuDict = {'1':'Rectangular','2':'Square','3':'Custom'}
    print(roomMenuDict(1))
    enterType = int(input("Enter type of room (1-3): "))
    while enterType < 1 or enterType > 3:
        print("Error: Type of room must be between 1 and 3")
        enterType = int(input("Enter type of room (1-3): "))
    return enterType
    '''
       Reads the shape of the room based on a list of valid shapes.
       Based on a roomMenuDict of 1:Rec, 2:Square and 3:Custom.
       Error checks the input must be one of the valid keys (1-3)

       Arguments: nbrOfRooms (int)

       Returns:  menu option selected (1,2,3)
    '''
    roomMenuDict = {'1':'Rectangular','2':'Square','3':'Custom'}
    

def getNumberWindowsDoors():
    '''
        Inputs the number of windows and doors in a room
    
        Returns:  number of doors and windows in a room
    '''
    pass

if __name__ == '__main__':
    main()