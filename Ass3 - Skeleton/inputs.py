from constants import *
from computations import *
from report import *
import math

def main():
    
    '''
    Controls flow of the program. Gets the initial inputs, 
    iterates for the specified number of rooms, 
    calls appropriate functions, calculates, 
    and displays total paint required and cost.
    Arguments: None
    Returns: None
    '''
    i = 0
    quoteSurface = 0
    quoteGallons = 0
    quoteWindows = 0
    paintPrice = getPaintPrice() #get paint price 
    numCoats = getNumberOfCoats() #num of coats
    numRooms = getNumberRooms() #num of rooms
    print()
    while i < numRooms:
        i += 1 
        menuOption = roomsMenu(i) #the menu option
        RoomArea = computeRoomArea(menuOption) #calls functions from computations
        numWindowDoors = getNumberWindowsDoors() #gets number of windows 
        print()
        WindowDoorsArea = computeWindowsDoorsArea(numWindowDoors)
        areaPainted = (RoomArea - WindowDoorsArea) #func for this
        totalSurface = areaPainted * numCoats   #func for this 
        gallons = computeGallons(totalSurface) #finds the amt of gallons 
        totalPaintPrice = computePaintPrice(paintPrice,gallons) #paint cost
        sumRoom = printRoomSummary(totalSurface,gallons,totalPaintPrice,i) #prints out the summary per each room
        quoteWindows += numWindowDoors #adds the number of windows to calc the quote amount for the customer quote
        quoteSurface += totalSurface #adds the total surface to calc the quote amount for the customer quote
        quoteGallons += gallons #adds the number of gallons to calc the quote amount for the customer quote
    totalCustomerQuote = ((paintPrice * (math.ceil(quoteGallons))) + (quoteSurface * LABOUR_PER_SQ_FOOT) + (quoteWindows * 10)) * (1+PROFIT_MARGIN)
    print(f"""Customer Quote for All {numRooms} rooms:
        Coats of paint to be applied: {numCoats} 
        Total area ot be painted    : {quoteSurface}
        Paint Required              : {(math.ceil(quoteGallons))} gallons 
        Total Customer estimate     : {totalCustomerQuote:.2f}
        (Includes paint, labor and overhead)
          """)

    


def getPaintPrice():    
    '''
        Asks the user to enter the paint price and returns the value entered

        Returns:  paint price / gallon
    '''
    paintPrice = float(input("Enter Price of paint: "))
    return paintPrice


def getNumberOfCoats():
    
    ''' 
        Asks the user to enter the number of coats of paint 
        to apply (1-4) and returns value entered. Error checks the
        input, must be in the range 1-4.

        Returns:  number of coats of paint
    '''
    numCoats = int(input("Enter number of coats of paint to apply (1-4): "))
    return numCoats


def getNumberRooms():
    '''  
       Asks the user to enter the number of rooms 
       to paint and returns value entered
          
        Returns: number of rooms
    '''

    numRooms = int(input("How many rooms do you want to paint?: "))
    return numRooms



def roomsMenu(nbrOfRooms):
    '''
       Reads the shape of the room based on a list of valid shapes.
       Based on a roomMenuDict of 1:Rec, 2:Square and 3:Custom.
       Error checks the input must be one of the valid keys (1-3)

       Arguments: nbrOfRooms (int)

       Returns:  menu option selected (1,2,3)
    '''
    roomMenuDict = {'1':'Rectangular','2':'Square','3':'Custom'}
    

    print(f"Rooms {nbrOfRooms}")
    print("Select the shape of the room: ")
    for option in roomMenuDict:
            print(option,'-', roomMenuDict[option])
    menuOption = int(input("Option: "))
    if menuOption in range(0,4):
        return menuOption
    else:
        print("Invalid option")
        menuOption = int(input("Option: "))

def getNumberWindowsDoors():
    '''
        Inputs the number of windows and doors in a room
    
        Returns:  number of doors and windows in a room
    '''
    numWindowsDoors = int(input("How many windows and doors are in the room? "))
    return numWindowsDoors

    
    




if __name__ == '__main__':
    main()