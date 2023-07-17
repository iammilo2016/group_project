# This module prints out the final results
from constants import *
 
def printRoomSummary(area, paintPriceGal,totalPaintcost,numRoom):
    '''
        Prints a summary for the room including:
            - room number 
            - area
            - # of gallons required
            - paint price 
        Arguments: 
            room - room number
            area - calculated area of the room
            paintPriceGal - paint price per Gal
        Returns:
            None

    '''
    print(
        f"""\nFor Room: {numRoom}
        Area to be painted: {area:.1f} sq ft.
        Paint required    : {paintPriceGal:.2f} gallons
        Paint cost(approx): ${totalPaintcost:.2f}
          """)

def computeGallons(area):

    ''' 
        Calculate gallons of paint for the area based on the paint coverage/sq ft

        Arguments:  area (float)
        Returns:    gallons of paint
    '''  

    gallon = area / 175
    return gallon

def computePaintPrice(paintprice,paintPricePerGal):
    '''
    Takes the area and paint price/gal as parameters, 
    calculates and returns the cost of paint
    Parameters:
        area - area to be painted
        pairtPricePerGall - price per gallon
    Returns: price - paint price for the room
    '''

    totalPaintCost = paintprice * paintPricePerGal
    return totalPaintCost

    
