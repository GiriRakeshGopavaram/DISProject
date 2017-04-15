
1. Team Number: P19
2. Team Members: Vikram Simha Reddy Ganta and Giri Rakesh Gopavaram
3. Summary: We will be using Natural Gas Residential Consumption data as our data set. We are working on total and average amount of consumption for a state.
4. Describe your Data Source: Our data source is NaturalGas.txt, which is structured data. It contains 4 fields named State, Month, Year, Consumption_Amount (in Million Cubic Feet). It is of size 2.1 MB.
5. Link to Data Source: https://www.eia.gov/opendata/qb.php?category=458094&sdid=NG.N3010MO2.M (Links to an external site.)
6. What makes it a big data problem?
    Volume: Volume of the data set is 2.1 MB. There are 3850 records.
    Variety: It is a structured data. Data is stored in text file.
    Velocity: This is historical training data that covers to Jan-1989 to Dec-2016.
    Veracity: Data is formatted/cleaned and it is trustworthy.
    Value: The monthly consumption levels of California state is much higher than Missouri.
7. Describe your two Map Reduce problems in the format "for each _(key)_ , we will find the _(value)__".
i. For each store, calculate the Total consumption for a state.
ii. For each store, calculate the Average consumption for a state.
8. Mapper input:  show few lines of data that your mapper will read.
Missouri          Dec         2016         21067
Missouri          Nov         2016         7285
Missouri          Oct         2016         2607
Missouri          Sep         2016         1663
Missouri         Aug         2016        1739
California       Dec         2016         66085
California        Nov         2016        37269
California        Oct         2016        22105
California        Sep         2016        19803
California        Aug         2016        18507
9. Mapper output/ Reducer input:
Missouri          21067
Missouri           7285
Missouri           2607
Missouri           1663
Missouri          1739
California         66085
California         37269
California          22105
California          19803
California         18507
10. Reducer Output:
For Total Consumption :
Missouri    34361
California    163769
For Average Consumption :
Missouri    6872.2
California    32753.8
11. Language: Python
12. Process: We are processing numeric data. No data cleaning is required for the data set.

Steps to be followed: Mapper
Clone a copy of repository to your c:\44564 folder.
Open a command window as Administrator in this project folder (e.g. C:\44564\P19).
Follow the below commands:
> python mapper.py
![mapper](https://cloud.githubusercontent.com/assets/22079671/25057729/036d14f2-2138-11e7-8325-dffb7dcbdde5.PNG)


Steps to be followed: Reducer Output for Total Consumption by state
Clone a copy of repository to your c:\44564 folder.
Open a command window as Administrator in this project folder (e.g. C:\44564\P19).
Follow the below commands:
> python reducer.py
![reducertotal](https://cloud.githubusercontent.com/assets/22079671/25059937/3ba83f18-2156-11e7-94b7-d036b6e646e3.PNG)

Steps to be followed: Reducer Output for Average Consumption by state
Clone a copy of repository to your c:\44564 folder.
Open a command window as Administrator in this project folder (e.g. C:\44564\P19).
Follow the below commands:
> python reducer.py
![reducer](https://cloud.githubusercontent.com/assets/22079671/25057733/055e3b9c-2138-11e7-81e1-19407f88ca12.PNG)

Graphical Representation: 
![graph](https://cloud.githubusercontent.com/assets/22079671/25060040/afc38900-2158-11e7-8f4c-2f5fc7b7526f.PNG)


