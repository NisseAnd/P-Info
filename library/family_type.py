import numpy as np
import pandas as pd
from tqdm import tqdm

def family_type_best_p_spots(income_data):
 
    #create dataframes from csv files:
    data = income_data     
    indkomstpivot = pd.pivot_table(data, index=['DISTRIKTSNAVN', 'FAMILIETYPE'], values=["HUSTANDE"], aggfunc=np.sum)
    dataPark = park_dataframe()
    parkpivot = pd.pivot_table(dataPark, index=['bydel'], values=["antal_pladser"], aggfunc=np.sum)

    #calculate total population and merge datasets:
    total_pop = pd.pivot_table(data, index=['DISTRIKTSNAVN'], values=["HUSTANDE"], aggfunc=np.sum)
    total_pop = clean_up_indkomstframe(total_pop)
    merge_datasetes = pd.concat([total_pop, parkpivot], axis = 1, sort=False)
    merge_datasetes['parkratio'] = merge_datasetes['antal_pladser']/merge_datasetes['HUSTANDE']

    #add the merged datasets back into the income dataset
    clean_indkomst = clean_up_indkomstframe(indkomstpivot)
    clean_indkomst = add_ratio_to_indkomst(clean_indkomst, merge_datasetes)

    #calculate the total parkingspaces for each FAMILIETYPE
    clean_indkomst['FAMILIERATIO'] = clean_indkomst['HUSTANDE']*clean_indkomst['DISTRIKTRATIO']
    
    #extract usefull columns
    clean_indkomst = clean_indkomst.reset_index()
    clean_indkomst = clean_indkomst[['FAMILIETYPE','HUSTANDE', 'FAMILIERATIO']]
    
    #calculate average for each FAMILIETYPE:
    clean_indkomst = clean_indkomst.groupby('FAMILIETYPE').sum(axis=1)
    clean_indkomst['GENNEMSNITSRATIO'] = clean_indkomst['FAMILIERATIO']/clean_indkomst['HUSTANDE']
    clean_indkomst = clean_indkomst.sort_values('GENNEMSNITSRATIO', ascending=False)

    #Return result:
    mest_priviligeret = clean_indkomst.index.values[0]
    gennemsnit_antal_pladser = clean_indkomst.iloc[0]['GENNEMSNITSRATIO']
    out0 = "opg4: hvilken familietype har de bedste parkeringsmulighedder?\n"
    out1 = f"Flest pladser pr. hustand: {mest_priviligeret}, antal pladser: {gennemsnit_antal_pladser}\n"
    out2 = clean_indkomst.to_string()

    return out0+out1+out2



def add_ratio_to_indkomst(clean_indkomst, mymerge):
    clean_indkomst['DISTRIKTRATIO'] = 'newratio' 
    
    clean_indkomst.at['Indre By','DISTRIKTRATIO'] = mymerge.loc['Indre By','parkratio']
    clean_indkomst.at['Amager Vest','DISTRIKTRATIO'] = mymerge.loc['Amager Vest','parkratio']
    clean_indkomst.at['Østerbro','DISTRIKTRATIO'] = mymerge.loc['Østerbro','parkratio']
    clean_indkomst.at['Nørrebro','DISTRIKTRATIO'] = mymerge.loc['Nørrebro','parkratio']
    clean_indkomst.at['Vesterbro-Kongens Enghave','DISTRIKTRATIO'] = mymerge.loc['Vesterbro-Kongens Enghave','parkratio']
    clean_indkomst.at['Valby','DISTRIKTRATIO'] = mymerge.loc['Valby','parkratio']
    clean_indkomst.at['Vanløse','DISTRIKTRATIO'] = mymerge.loc['Vanløse','parkratio']
    clean_indkomst.at['Brønshøj-Husum','DISTRIKTRATIO'] = mymerge.loc['Brønshøj-Husum','parkratio']
    clean_indkomst.at['Bispebjerg','DISTRIKTRATIO'] = mymerge.loc['Bispebjerg','parkratio']
    clean_indkomst.at['Amager Øst','DISTRIKTRATIO'] = mymerge.loc['Amager Øst','parkratio']

    return clean_indkomst


def clean_up_indkomstframe(total_pop):
    total_pop.drop(index='Uden for inddeling', inplace=True)

    total_pop.rename(index={'1. Indre By': 'Indre By'}, inplace=True)
    total_pop.rename(index={'10. Amager Vest': 'Amager Vest'}, inplace=True)
    total_pop.rename(index={'2. Østerbro': 'Østerbro'}, inplace=True)
    total_pop.rename(index={'3. Nørrebro': 'Nørrebro'}, inplace=True)
    total_pop.rename(index={'4. Vesterbro/Kongens Enghave': 'Vesterbro-Kongens Enghave'}, inplace=True)
    total_pop.rename(index={'5. Valby': 'Valby'}, inplace=True)
    total_pop.rename(index={'6. Vanløse': 'Vanløse'}, inplace=True)
    total_pop.rename(index={'7. Brønshøj-Husum': 'Brønshøj-Husum'}, inplace=True)
    total_pop.rename(index={'8. Bispebjerg': 'Bispebjerg'}, inplace=True)
    total_pop.rename(index={'9. Amager Øst': 'Amager Øst'}, inplace=True)
    return total_pop

def park_dataframe():
    file_name = 'p_pladser.csv'
    for row in tqdm(file_name, total=len(file_name)): #opg 1 coln 8 (bydel) og parameter (Indre By)
        dataPark = pd.read_csv(file_name, sep=',', low_memory=False, usecols=[3,7])
    return dataPark 
