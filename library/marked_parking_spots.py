import pandas as pd 
# import utility.convert_csv as cc

def marked_spots(data):
    even_df = data[data['vejside'] == 'Lige husnr.']
    uneven_df = data[data['vejside'] == 'Ulige husnr.']
    
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
    

    """ even_odd_marked_p_spots = cc.convert_p_space_to_dataframe([3, 9]) #[3, 9]

    newlist = []

    for p_type in even_odd_marked_p_spots.p_type.unique():
        newlist.append(even_odd_marked_p_spots[even_odd_marked_p_spots['p_type'] == p_type].antal_pladser.sum())

    marked_p_spots = even_odd_marked_p_spots.p_type.unique()[newlist.index(max(newlist))]

    print(marked_p_spots,'has',max(newlist),'parking spots') """