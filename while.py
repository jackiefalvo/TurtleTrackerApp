# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:12:25 2020

@author: cif3

# notes on for vs while
    # for loop - goes through entire contents of the file (reads through each line)
    # while loop - is in there until condition is proven false
        # ** more memory efficient - good for big data
"""

# read in data
raw_file = './Data/Raw/RawArgosData_SaraTurtleTrack.txt'
raw_data = open(raw_file, 'r')

# first read a single line (will continue reading single lines every time it's run)
lineString = raw_data.readline()


while lineString: # this says 'while (as long as) linestring has a value'

    # evaluate if first character of line is # or u
    if lineString[0] in ('#', 'u'): 
        # read next line **this is what updates our variable lineString
        lineString = raw_data.readline()
        continue # don't continue in script, rather, continue to read/evaluate the next line
        
# split string into data items
    lineData = lineString.split()

# extract items in list into variables
    record_ID = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7] 
    
# read next line..(have to do it here too since loop has moved on)
    lineString = raw_data.readline()
    
# tell us sara's location
    print(f"Record {record_ID} indicates Sara was seen at {obs_lat}N,{obs_lon}W on {obs_date}")

    
# close out file
raw_data.close()