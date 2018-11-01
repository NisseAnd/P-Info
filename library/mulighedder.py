import pandas as pd


def mulig(dframe):

    parkingspot_centrum = dframe[dframe['bydel'] == 'Indre By']
    total = parkingspot_centrum['antal_pladser'].sum()
    print(total)

    

    return "hello"



#end
