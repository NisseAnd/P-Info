""" 
The url to run this program use this url:
https://raw.githubusercontent.com/rmlassesen/dataset/master/p_pladser.csv
"""

import utility.downloader as download
import utility.convert_csv as convert_csv
import library.centrum_parking as ex1
import library.marked_parking_spots as ex2
import library.public_and_privat_parking as ex3
import library.family_type as ex4
import library.privat_parking as ex5


if __name__ == '__main__':
    global file_name
    file_name = download.download_file()

data = convert_csv.convert_csv_to_dataframe(file_name)

# Get the income file
data_income_file = download.get_income_data()

# Convert income file to data frame.
income_data = convert_csv.convert_income_to_dataframe(data_income_file)

ex1.number_of_spots(data)
ex2.marked_spots(data)
ex3.public_and_private_parking_spots(data)
print(ex4.family_type_best_p_spots(income_data))
ex5.privat_parking_electric_cars(data, income_data)
