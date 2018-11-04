import pandas as pd 
import utility.convert_csv as cc

def marked_spots():
    even_odd_marked_p_spots = cc.convert_p_space_to_dataframe([3, 9]) #[3, 9]

    newlist = []

    for p_type in even_odd_marked_p_spots.p_type.unique():
        newlist.append(even_odd_marked_p_spots[even_odd_marked_p_spots['p_type'] == p_type].antal_pladser.sum())

    marked_p_spots = even_odd_marked_p_spots.p_type.unique()[newlist.index(max(newlist))]

    print(marked_p_spots,'has',max(newlist),'parking spots')