import pandas as pd
from tqdm import tqdm


def convert_csv_to_dataframe(file_name):
    '''
    This method read the csv file and convert it to a dataframe.
    When it's done it change the date to a date time object and some of the columns to integers.
    '''
    # Returneres som en dataframe.
    # low_memory=False because column 5 and 9 has mixed datatypes.
    print('Convert csv file to a dataFrame.')
    for row in tqdm(file_name, total=len(file_name)): #opg 1 coln 8 (bydel) og parameter (Indre By)
        data = pd.read_csv(file_name, sep=',', low_memory=False, usecols=[2, 3, 6, 7])
    
    #return data

    parkingspot_centrum = data[data['bydel'] == 'Indre By']

    data['antal_pladser'] = pd.to_numeric(
        data['antal_pladser'], errors='coerce').fillna(0).astype(int)

    total = data['antal_pladser'].sum()
    
    print(total)

    highest_parking = data['antal_pladser'].idxmax()

    print(data['vejnavn'][highest_parking])
    print(data['antal_pladser'][highest_parking])