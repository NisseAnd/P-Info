import pandas as pd
import utility.convert_csv as cc

def p_spots():
    most_p_spots = cc.convert_p_space_to_dataframe([2, 3]) #2, 3
    
    newlist = []

    for vejnavn in most_p_spots.vejnavn.unique():
        newlist.append(most_p_spots[most_p_spots['vejnavn'] == vejnavn].antal_pladser.sum())

    road_name = most_p_spots.vejnavn.unique()[newlist.index(max(newlist))]

    print(road_name,'has',max(newlist),'parking spots')