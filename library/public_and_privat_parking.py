import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" 
Vis med et splittet bar-plot den procentvise fordeling(y-aksen) 
af private og offentlige p-pladser i hver by-del(x-aksen)
 """

def public_and_private_parking_spots(data):
    # Sorts the df by bydel and vejstatus and then sum the amout of parking spots.
    sort_data = data.groupby(['bydel', 'vejstatus']).sum()
       
    # Calculate percentages.
    # total_parking_spots = sort_data['antal_pladser'].sum()
    # sort_data['percentage'] = sort_data['antal_pladser'] / total_parking_spots * 100
    sort_data['percentage'] = sort_data.div(sort_data['antal_pladser'].sum()).values * 100

    # Make a data frame with only privat fællesvej and one with public Kommunevej.
    #private = sort_data.query('vejstatus == ["Privat fællesvej"]')
    #public = sort_data.query('vejstatus == ["Kommunevej"]')
    #print(public)

    sort_data.plot(y=["vejstatus", "Kommunevej"], kind="bar")
    #x="X", 

    plt.show()
