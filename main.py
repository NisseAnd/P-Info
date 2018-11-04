""" 
The url to run this program use this url:
https://raw.githubusercontent.com/rmlassesen/dataset/master/p_pladser.csv
"""


import utility.downloader as dl
import utility.convert_csv as cc
import library.road_with_most_spots as rwms
import library.centrum_parking as cp
import library.privat_parking as privat_parking
import library.public_and_privat_parking as ex3

import library.even_or_odd_parking_spots as eoops
import library.marked_parking_spots as mps


if __name__ == '__main__':
    global file_name
    file_name = dl.download_file()

data = cc.convert_csv_to_dataframe(file_name)
#cp.number_of_parking_spots(data)

# Get the income data
#data_income = dl.get_income_data()

data_income = cc.convert_income_to_dataframe([1, 5, 6, 7, 8])

data_park = cc.convert_p_space_to_dataframe([2, 3, 6, 7, 9])


# Get the income file
data_income_file = dl.get_income_data()
# Convert income file to data frame.
income_data = cc.convert_income_to_dataframe(data_income_file)

# Opg. 3
ex3.public_and_private_parking_spots(data)

# opg 5
#privat_parking.prinat_parking_electric_cars(data, income_data)

rwms.p_spots()
cp.number_of_spots()
eoops.even_or_odd(data)
mps.marked_spots(data)

