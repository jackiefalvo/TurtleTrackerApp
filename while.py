# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:12:25 2020

@author: cif3
"""

# read in data
raw_file = './Data/Raw/RawArgosData_SaraTurtleTrack.txt'
raw_data = open(raw_file, 'r')

# read all lines of file, add to list
data = raw_data.readlines()
print(data[17])

# iterating through lines -- using while loop
# first read a single line (will continue reading single lines every time it's run)
lineString = raw_data.readline()    

while lineString: # this says 'while linestring has a value'

    if lineString[0] in ('#', 'u'):
        # read the next line
        lineString = raw_data.readline()
        continue
        

# split string into data items
    lineData = data.split()

# extract items in list into variables
    record_ID = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7] 
    
# tell us sara's location
    print(f"Record {record_ID} indicates Sara was seen at {obs_lat}N,{obs_lon}W on {obs_date}")

# read the next liine
    lineString = raw_data.readline()
    
# close out file
raw_data.close()