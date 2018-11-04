# P-Info

## Documentation
Analyzine the dataset about parking spots in Copenhagen and the dataset about income for people living in Copenhagen. This is the link to the assignment https://github.com/rmlassesen/dataset  

## Group
Anders Nissen, Christian Lykke and Bo Henriksen.  

## Dependencies
The project does only use dependencies which is part of Pythons Anaconda installation. 

## How to run the project
1. Clone the project  
2. Cd into the directory of the project  
3. To run the project you need to paste this url to the dataset as a parameter 
https://raw.githubusercontent.com/rmlassesen/dataset/master/p_pladser.csv  

4. Example of how to run the project  
5. python main.py [<url_to_dataset>]  

## Results
1. Hvor mange p-pladser er der i Indre By? Hvilken vej har flest?  
There are 12183 parking spots in centrum.  

2. Er der i København flest p-pladser i den side af vejen med lige eller ulige husnumre?  
The even side has most parkingspots with 13382 and the uneven side has 12151.  

  Hvilken side har flest afmærkede parkeringsbåse?  
  The uneven side has most marked parkingspots with 2883 and the even side has 2835.
  
3. Vis med et splittet bar-plot den procentvise fordeling(y-aksen) af private og offentlige p-pladser i hver by-del(x-aksen) 
Sry we did not make a map but this is the percentage between public and privat parkingspots:

                                                    antal_pladser  percentage
bydel                     vejstatus
Amager Vest               Internt færdselsareal                11    0.008853  
                          Kommunevej                         5442    4.379950  
                          Privat fællesvej                   6653    5.354613  
Amager Øst                Internt færdselsareal               418    0.336424  
                          Kommunevej                         5843    4.702691  
                          Privat fællesvej                   8282    6.665701  
Bispebjerg                Internt færdselsareal               187    0.150505  
                          Kommunevej                         4547    3.659616  
                          Privat fællessti                      2    0.001610  
                          Privat fællesvej                   6211    4.998873  
Brønshøj-Husum            Internt færdselsareal               486    0.391153  
                          Kommunevej                         3029    2.437866  
                          Privat fællesvej                   8639    6.953029  
                          Privat fællesvej §2 stk1            313    0.251916  
Indre By                  Internt færdselsareal                38    0.030584  
                          Kommunevej                        11845    9.533353  
                          Privat fællesvej                    281    0.226161  
Nørrebro                  Internt færdselsareal                88    0.070826  
                          Kommunevej                        11253    9.056886  
                          Privat fællesvej                      1    0.000805  
Valby                     Internt færdselsareal               484    0.389543  
                          Kommunevej                         5881    4.733275  
                          Privat fællesvej                   6506    5.236302  
                          Privat fællesvej §2 stk1             71    0.057144  
Vanløse                   Internt færdselsareal               223    0.179480  
                          Kommunevej                         2930    2.358187  
                          Privat fællesvej                   7454    5.999292  
                          Privat fællesvej §2 stk1             18    0.014487  
Vesterbro-Kongens Enghave Internt færdselsareal               524    0.421737  
                          Kommunevej                         7137    5.744157  
                          Privat fællesvej                   3041    2.447524  
Østerbro                  Internt færdselsareal               173    0.139238  
                          Kommunevej                        15443   12.429174  
                          Privat fællesvej                    794    0.639044  

4. Hvilken familietype har de bedste parkeringsmuligheder?  

5. Vis fordelingen af private parkeringspladser og parkeringsmuligheder for el-biler ift hver bydels gennemsnitlige bruttoindkomst.  
Because of the small amount of parkingspots for electric cars. We decieded not to make a map. This is how it lokks.
                                                          
bydel                       vejstatus           p_ordning             antal_pladser 
Amager Øst                  Privat fællesvej    El-Bil plads              6  
Vesterbro-Kongens Enghave   Privat fællesvej    El-Bil plads              4  

6. Farvekod på et kort bydelene i København, ud fra den gennemsnitlige bruttoindkomst. Plot markers med private (P) og el-bil-parkeringspladser (EL)  

![alt text](https://github.com/BoMarconiHenriksen/movie_dataset/blob/developer/movies_per_year.png)  
