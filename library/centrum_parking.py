import pandas as pd
import utility.convert_csv as cc

def number_of_spots(data):
    # Dataframe with all the parking spots for centrum.
    p_spots_centrum = data[data['bydel'] == 'Indre By']

    # We sum because there can be more than one parking spot in each place.
    p_spots_total = p_spots_centrum.antal_pladser.sum() 

    # Which road has most parkingspots.
    index_most_parkingspots = p_spots_centrum['antal_pladser'].idxmax() #.vejnavn.unique()[newlist.index(max(newlist))]
    road_name = p_spots_centrum['vejnavn'][index_most_parkingspots]
    amount_p_spots = p_spots_centrum['antal_pladser'][index_most_parkingspots]
    
    print('There are', p_spots_total, "parking spots in centrum") 
    print(road_name, 'is the road with most parkingspots and it has', amount_p_spots)