import pandas as pd
import numpy as np

""" 
Vis fordelingen af private parkeringspladser og parkeringsmuligheder for el-biler 
ift hver bydels gennemsnitlige bruttoindkomst.
 """


def prinat_parking_electric_cars(data, data_income):
    # pivot table is a table of statistics that summarize the data of a more extensive table.
    # They enable a person to arrange and rearrange (or "pivot") statistics in order to draw attention to useful information.
    # We choose with columns we will use as our index and it the pivot table will arrange our data based on the indexs.
    # We the columns "antal_pladser" as our value. and sum it.
    # aggfunc can take a list of functions.
    sort_data = pd.pivot_table(data, index=["bydel", "vejstatus", "p_ordning"], aggfunc=np.sum) # Muligt at tilføje values=["antal_pladser"], 
    # print(sort_data)

    privat_parking_el_cars = sort_data.query(
        'vejstatus == ["Privat fællesvej"]') #  & p_ordning ==["El-Bil plads"] 
    
    #print(privat_parking_el_cars)

    # print(data_income.columns)

    sort_income_data = pd.pivot_table(data_income, index=["BYDEL", "INDKOMSTKATEGORI"]) # , values=["HUSTANDE"]

    print(sort_income_data)




