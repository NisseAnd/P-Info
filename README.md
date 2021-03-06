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
### 1. Hvor mange p-pladser er der i Indre By? Hvilken vej har flest?  
There are 12183 parking spots in centrum.  

Elsdyrsgade is the road with most parkingspots and it has 60.  

### 2. Er der i København flest p-pladser i den side af vejen med lige eller ulige husnumre?  
The even side has most parkingspots with 60741 and the uneven side has 56669.    

##### Hvilken side har flest afmærkede parkeringsbåse?  
The even side has most marked parkingspots with 9422 and the uneven side has 9284.  

### 3. Vis med et splittet bar-plot den procentvise fordeling(y-aksen) af private og offentlige p-pladser i hver by-del(x-aksen) 
Sry we did not make a map but the percentage can be seen as a console print when you run the program.  
 
### 4. Hvilken familietype har de bedste parkeringsmuligheder?  
Flest pladser pr. hustand: 0, antal pladser: 0.43613138686131386  
FAMILIETYPE &nbsp;&nbsp;&nbsp;&nbsp; HUSTANDE &nbsp;&nbsp;&nbsp;&nbsp; FAMILIERATIO &nbsp;&nbsp;&nbsp;&nbsp; GENNEMSNITSRATIO  

0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 286604 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 124997.0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0.436131  

### 5. Vis fordelingen af private parkeringspladser og parkeringsmuligheder for el-biler ift hver bydels gennemsnitlige bruttoindkomst.  
Because of the small amount of private parkingspots for electric cars. We decieded not to make a map. This is the private parkingspots.  

Amager Øst&nbsp;&nbsp;&nbsp;&nbsp;Privat fællesvej&nbsp;&nbsp;&nbsp;&nbsp;El-Bil plads&nbsp;&nbsp;&nbsp;&nbsp;6  
Vesterbro-Kongens Enghave&nbsp;&nbsp;&nbsp;&nbsp;Privat fællesvej&nbsp;&nbsp;&nbsp;&nbsp;El-Bil plads&nbsp;&nbsp;&nbsp;&nbsp;4  

### 6. Farvekod på et kort bydelene i København, ud fra den gennemsnitlige bruttoindkomst. Plot markers med private (P) og el-bil-parkeringspladser (EL)  
