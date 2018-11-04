import pandas as pd
import utility.convert_csv as cc

def number_of_spots():
    spots_in_centrum = cc.convert_p_space_to_dataframe([3, 7]) # 3, 7 

    p_spots = spots_in_centrum[spots_in_centrum['bydel'] == 'Indre By'].antal_pladser.sum() 

    print('There are', p_spots, "parking spots in centrum") 