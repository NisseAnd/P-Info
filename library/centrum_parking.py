import pandas as pd

def number_of_spots(data):
    parkingspot_centrum = data[data['bydel'] == 'Indre By'] #returnere en boolean parkingspots_centrum som er true


    #p_spots = data_park[data_park['bydel'] == 'Indre By'].antal_pladser.sum() SKAL BRUGES TIL OPG 1

    #print('There are',p_spots, "parking spots in centrum") SKAL BRUGES TIL OPG 1

    #num_of_spots = data_park.antal_pladser.sum() SKAL IKKE BRUGES TIL OPG 1

    #print('There are ',num_of_spots,' parking spots in centrum') SKAL IKKE BRUGES TIL OPG 1