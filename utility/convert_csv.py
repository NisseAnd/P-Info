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
    for row in tqdm(file_name, total=len(file_name)):
        data = pd.read_csv(file_name, sep=',', low_memory=False, usecols=[2, 3, 5, 6, 7, 8, 9])
    
    # Convert antal_pladser to int
    data['antal_pladser'] = pd.to_numeric(
        data['antal_pladser'], errors='coerce').fillna(0).astype(int)
    
    # Print object types of columns in dataframe
    # print(data.dtypes)

    return data

# Make a new convert csv method to the income data and convert string to int for relevant columns.

def convert_income_to_dataframe(column_list):
    file_name = 'indkomstbruttohustype.csv'
    for row in tqdm(file_name, total=len(file_name)): #[1, 5, 6, 7, 8]
        data_income = pd.read_csv(file_name, sep=',', low_memory=False, usecols=column_list)

    data_income['FAMILIETYPE'] = pd.to_numeric(
        data_income['FAMILIETYPE'], errors='coerce').fillna(0).astype(int)

    return data_income

def convert_p_space_to_dataframe(column_list):
    file_name = 'p_pladser.csv'
    for row in tqdm(file_name, total=len(file_name)): #[2, 3, 6, 7, 9]
        data_park = pd.read_csv(file_name, sep=',', low_memory=False, usecols=column_list)

    data_park['antal_pladser'] = pd.to_numeric(
        data_park['antal_pladser'], errors='coerce').fillna(0).astype(int)

    return data_park