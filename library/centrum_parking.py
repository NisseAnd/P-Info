import pandas as pd
import utility.convert_csv as cc

def number_of_spots():
    spots_in_centrum = cc.convert_p_space_to_dataframe([3, 7]) # 3, 7 

    p_spots = spots_in_centrum[spots_in_centrum['bydel'] == 'Indre By'].antal_pladser.sum() 

    print('There are',p_spots, "parking spots in centrum") 


    #parkingspot_centrum = data[data['bydel'] == 'Indre By'] #returnere en boolean parkingspots_centrum som er true

    

    #num_of_spots = data_park.antal_pladser.sum() SKAL IKKE BRUGES TIL OPG 1!!!!!

    #print('There are ',num_of_spots,' parking spots in centrum') SKAL IKKE BRUGES TIL OPG 1!!!!!