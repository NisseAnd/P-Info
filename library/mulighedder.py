import numpy as np
import pandas as pd
import utility.convert_csv as cc
from tqdm import tqdm

def mulig(dframe):
    
    data = household_dataframe_2014()    
    distrikt = data.DISTRIKTSNAVN.unique()      #skal bruges til naeste del
    families = data.FAMILIETYPE.unique()     #skal bruges til naeste del
    
    #dataPark = park_dataframe()
    #distPark = dataPark.bydel.unique()  
    #clean_living = normalize_district_name(distrikt)
    '''district_freq = create_district_freq(data, dataPark)''' #samme raekkefoelge som clean_living

    #['Enlige uden børn', 'Enlige med børn', 'Par uden børn', 'Par 1 barn', 'Par 2 børn', 'Par 3 eller flere børn']
    #families = [x for x in families if isinstance(x,str)]
    #print(families)

    # testresultat: result = sum_from_category_2014('Enlige uden børn', '1. Indre By', data)
    #print(result)

    ######################## så er foerste del klar ## Nu til pandas pivot_tabel #############################
    #http://pbpython.com/pandas-pivot-table-explained.html
    #pd.pivot_table(df,index=["Manager","Rep"])

    chrpivot = pd.pivot_table(data, index=['DISTRIKTSNAVN', 'FAMILIETYPE'], values=["HUSTANDE"], aggfunc=np.sum)
    print(chrpivot.head())

    



    return "hello"

def sum_from_category_2014(familietype, distriktnavn, indkomstframe):
    table_of_people = indkomstframe.loc[
        (indkomstframe['AAR'] == 2014)&
        (indkomstframe['FAMILIETYPE'] == familietype)&
        (indkomstframe['DISTRIKTSNAVN'] == distriktnavn)]
    return table_of_people['HUSTANDE'].sum()
    

def create_district_freq(household_frame, parking_frame):
    data = household_frame
    dataPark = parking_frame  
    distrikt = data.DISTRIKTSNAVN.unique()
    distPark = dataPark.bydel.unique()
    
    clean_living = normalize_district_name(distrikt)
    clean_park = normalize_district_name(distPark)
    households = households_in_indcomedist(distrikt, data)
    parkingspaces = parkspace_in_parkdist(distPark, dataPark)

    district_freq = park_freq_by_district(clean_living, households, clean_park, parkingspaces)
    return district_freq

# organized by the districts in data.DISTRIKTSNAVN.unique()
def park_freq_by_district(area_list1, num_list1, area_list2, num_list2):
    output = []
    for item in area_list1:
        firstlist_index = area_list1.index(item)
        secondlist_index = area_list2.index(item)
        firstvalue = num_list1[firstlist_index] #households
        secondvalue = num_list2[secondlist_index] #parking space
        output.append(secondvalue/firstvalue) #parking spaces pr. household
        #print(item)
        #print(secondvalue/firstvalue)
    return output


def normalize_district_name(list_of_names):
    proper_names = ['Vesterbro-Kongens Enghave', 'Indre By', 'Brønshøj-Husum', 'Vanløse', 
            'Amager Øst', 'Amager Vest', 'Østerbro', 'Valby', 'Nørrebro', 'Bispebjerg']
    accept_names = ['Vesterbro', 'Indre By', 'Brønshøj', 'Vanløse', 'Amager Øst', 'Amager Vest', 'Østerbro', 'Valby', 'Nørrebro', 'Bispebjerg']
    output_list = []
    for item in list_of_names:
        #print(item)
        if isinstance(item, str):#if not pd.isnull(item):
            #print(item)
            myindex = _get_idx_of_substring(item, accept_names)
            #print(myindex)
            if isinstance(myindex, int):
                output_list.append(proper_names[myindex])
    return output_list

def _get_idx_of_substring(district, substring_list):
    for idx, val in enumerate(substring_list):
        try:
            if val in district:
                return idx
        except:
            pass
            #print('If there is ExceptionI, then execute this block.')
            #return -1


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


def parkspace_in_parkdist(parkdistricts, parkframe):
    list_of_parkspace = []
    for item in parkdistricts:
        #print(item)
        parking_in_district = parkframe[parkframe['bydel'] == item].antal_pladser.sum()
        #print(parking_in_district)
        if parking_in_district != 0:
            list_of_parkspace.append(parking_in_district)
    return list_of_parkspace

#print(households_in_indcomedist(distrikt, data))
def households_in_indcomedist(indcomedistricts, indcomeframe):
    list_of_households = []
    for item in indcomedistricts:
        list_of_households.append(indcomeframe[(indcomeframe['DISTRIKTSNAVN'] == item)&(indcomeframe['AAR'] == 2014)].HUSTANDE.sum())
    return list_of_households





#end


# 2018-11-02 -- trash
'''

    # hvis man bruger 'p_pladser.py':
    #data = cc.convert_csv_to_dataframe('p_pladser.csv')
    #parkingspot_centrum = data[data['bydel'] == 'Indre By']
    #total = parkingspot_centrum['antal_pladser'].sum()
    #print(total)

    #data['antal_pladser'] = pd.to_numeric(
    #    data['antal_pladser'], errors='coerce').fillna(0).astype(int)

    # d1 = pd.DataFrame(columns=[ 'float_column' ], dtype=float)
    # df.iloc[:, n] 

    data = household_dataframe()

    #print(data.iloc[0, 1]) #ser ud til at give en fin string
    #print(data.dtypes) #ser ud til at ville virke: 
        # DISTRIKTSNAVN    object FAMILIETYPE      object  HUSTANDE          int64
    #print(data.iloc[0])

    #print(data.iloc[:, 2].sum()) #HUS
    
    
    #2018-11-01 -- lav liste med alle familie typer (len == antal familietyper)
    # derefter: find det samlede antal husstande med hver familietype

    #df.name.unique()
    #print(data.iloc[:, 1]) #colonenn med FAMILIETYPE, hver inje er strings
   
   
    famlist = data.FAMILIETYPE.unique() #<class 'numpy.ndarray'> inkl nan
    distrikt = data.DISTRIKTSNAVN.unique()
    
    
    #print(distrikt)
    #print("len distrikt er:")
    #print(len(distrikt))

    # find distrikterne i parkering:
'''