import pandas as pd

def number_of_spots(data):
    parkingspot_centrum = data[data['bydel'] == 'Indre By'] #returnere en boolean parkingspots_centrum som er true