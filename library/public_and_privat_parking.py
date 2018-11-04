import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" 
Vis med et splittet bar-plot den procentvise fordeling(y-aksen) 
af private og offentlige p-pladser i hver by-del(x-aksen)
 """

def public_and_private_parking_spots(data):
    sort_data = pd.pivot_table(data, index=["bydel", "vejstatus"], aggfunc = np.sum, margins=True) # Muligt at tilføje values=["antal_pladser"], 
    #print(sort_data)


    privat_parking = sort_data.query(
       'vejstatus == ["Privat fællesvej"]') #  & p_ordning ==["El-Bil plads"] 
    #print(privat_parking)

    public_parking = sort_data.query(
       'vejstatus == ["Kommunevej"]')
    
    #privat_parking.loc['percent'] = (privat_parking.antal_pladser / privat_parking.antal_pladser.sum() * 100)

    print(public_parking)