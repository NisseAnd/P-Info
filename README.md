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
Sry we did not make a map but the percentage can be seen as a console print when you run the program.  
 
4. Hvilken familietype har de bedste parkeringsmuligheder?  

5. Vis fordelingen af private parkeringspladser og parkeringsmuligheder for el-biler ift hver bydels gennemsnitlige bruttoindkomst.  
Because of the small amount of parkingspots for electric cars. We decieded not to make a map. This is how it lokks.
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                                                   
bydel&nbsp;&nbsp;&nbsp;&nbsp;vejstatus&nbsp;&nbsp;&nbsp;&nbsp;p_ordning&nbsp;&nbsp;&nbsp;&nbsp;antal_pladser  
Amager Øst&nbsp;&nbsp;&nbsp;&nbsp;Privat fællesvej&nbsp;&nbsp;&nbsp;&nbsp;El-Bil plads&nbsp;&nbsp;&nbsp;&nbsp;6  
Vesterbro-Kongens Enghave&nbsp;&nbsp;&nbsp;&nbsp;Privat fællesvej&nbsp;&nbsp;&nbsp;&nbsp;El-Bil plads&nbsp;&nbsp;&nbsp;&nbsp;4  

6. Farvekod på et kort bydelene i København, ud fra den gennemsnitlige bruttoindkomst. Plot markers med private (P) og el-bil-parkeringspladser (EL)  
