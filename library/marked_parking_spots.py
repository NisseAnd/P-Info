import pandas as pd 
# import utility.convert_csv as cc

def marked_spots(data):
    even_df = data[data['vejside'] == 'Lige husnr.']
    uneven_df = data[data['vejside'] == 'Ulige husnr.']
    
    # We sum because there can be more than one parking spot in a place.
    even_total = even_df.antal_pladser.sum()
    uneven_total = uneven_df.antal_pladser.sum()
    
    if even_total > uneven_total:
        print('The even side has most parkingspots with', even_total, 'and the uneven side has', uneven_total)
    else:
        print('The uneven side has most parkingspots with', uneven_total, 'and the even side has', even_total)
    
    # Marked parking.
    even_marked_df = even_df[even_df['p_type'] == 'Afmærket parkering']
    uneven_marked_df = uneven_df[uneven_df['p_type'] == 'Afmærket parkering']

    even_marked_total = even_marked_df.antal_pladser.sum()
    uneven_marked_total = uneven_marked_df.antal_pladser.sum()

    if even_marked_total > uneven_marked_total:
        print('The even side has most marked parkingspots with', even_marked_total, 'and the uneven side has', uneven_marked_total)
    else:
        print('The uneven side has most marked parkingspots with', uneven_marked_total, 'and the even side has', even_marked_total)
    

    """ Kode der blev refaktoret.
    newlist = []

    for vejside in data.vejside.unique():
        newlist.append(data[data['vejside'] == vejside].antal_pladser.sum()) 

    even_spots = data.vejside.unique()[newlist.index(max(newlist))]

    print(even_spots, 'has', max(newlist), 'parking spots') """
    