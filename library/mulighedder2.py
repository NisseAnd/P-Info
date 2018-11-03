import numpy as np
import pandas as pd
from tqdm import tqdm

def mulig(dframe):
    
    data = household_dataframe_2014()    
    indkomstpivot = pd.pivot_table(data, index=['DISTRIKTSNAVN', 'FAMILIETYPE'], values=["HUSTANDE"], aggfunc=np.sum)
    #print(chrpivot.head())
    
    dataPark = park_dataframe()
    parkpivot = pd.pivot_table(dataPark, index=['bydel'], values=["antal_pladser"], aggfunc=np.sum) #, 'antal_pladser'
    #print(parkpivot.head())

    total_pop = pd.pivot_table(data, index=['DISTRIKTSNAVN'], values=["HUSTANDE"], aggfunc=np.sum)
    #print(total_pop.head())
    #print(total_pop.index.values)

    


    return "Opg 4: hvilken familiegruppe har de bedste parkeringsmulihedder (ikke faerdig)"

'''
    Amager Vest               
Amager Øst                  
Bispebjerg                 
Brønshøj-Husum            
Indre By                   
Nørrebro                    
Valby                     
Vanløse                   
Vesterbro-Kongens Enghave  
Østerbro
'''

def household_dataframe_2014():
    file_name = 'indkomstbruttohustype.csv'
    for row in tqdm(file_name, total=len(file_name)): #opg 1 coln 8 (bydel) og parameter (Indre By)
        data = pd.read_csv(file_name, sep=',', low_memory=False, usecols=[0, 2, 5, 8])
    data = data[data['AAR'] == 2014]
    return data

def park_dataframe():
    file_name = 'p_pladser.csv'
    for row in tqdm(file_name, total=len(file_name)): #opg 1 coln 8 (bydel) og parameter (Indre By)
        dataPark = pd.read_csv(file_name, sep=',', low_memory=False, usecols=[3,7])
    return dataPark

'''
import library.mulighedder2 as mu
data = cc.convert_csv_to_dataframe('p_pladser.csv')
print(mu.mulig(data))
'''


#end
