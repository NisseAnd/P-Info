import pandas as pd

def number_of_parking_spots(data):
    # Boolean selection - Returns a boolean which is true or false for every element and
    # then put every true element in the data frame parkingspot_centrum.
    parkingspot_centrum = data[data['bydel'] == 'Indre By']
        

    total = parkingspot_centrum['antal_pladser'].sum()
    
    print(str(total) + ' parking spots in indre by.')

    highest_parking = parkingspot_centrum['antal_pladser'].idxmax()

    print(parkingspot_centrum['vejnavn'][highest_parking])
    print(parkingspot_centrum['antal_pladser'][highest_parking])