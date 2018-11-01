import pandas as pd
import utility.convert_csv as cc
from tqdm import tqdm

def mulig(dframe):
    
    # hvis man bruger 'p_pladser.py':
    #data = cc.convert_csv_to_dataframe('p_pladser.csv')
    #parkingspot_centrum = data[data['bydel'] == 'Indre By']
    #total = parkingspot_centrum['antal_pladser'].sum()
    #print(total)

    #data['antal_pladser'] = pd.to_numeric(
    #    data['antal_pladser'], errors='coerce').fillna(0).astype(int)

    # d1 = pd.DataFrame(columns=[ 'float_column' ], dtype=float)
    # df.iloc[:, n] 

    file_name = 'indkomstbruttohustype.csv'
    for row in tqdm(file_name, total=len(file_name)): #opg 1 coln 8 (bydel) og parameter (Indre By)
        data = pd.read_csv(file_name, sep=',', low_memory=False, usecols=[2, 5, 8])
    
    #print(data.iloc[0, 1]) #ser ud til at give en fin string
    #print(data.dtypes) #ser ud til at ville virke: 
        # DISTRIKTSNAVN    object FAMILIETYPE      object  HUSTANDE          int64
    #print(data.iloc[0])

    #print(data.iloc[:, 2].sum()) #HUS
    
    
    #2018-11-01 -- lav liste med alle familie typer
    # derefter: find det samlede antal husstande med hver familietype

    print(data.iloc[:, 1])

    return "hello"






#end
