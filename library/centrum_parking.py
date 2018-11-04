import pandas as pd
import utility.convert_csv as cc

def number_of_spots(data):
    p_spots = data[data['bydel'] == 'Indre By'].antal_pladser.sum() 

    print('There are', p_spots, "parking spots in centrum") 