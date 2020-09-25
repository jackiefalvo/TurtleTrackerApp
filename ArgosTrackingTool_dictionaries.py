#-------------------------------------------------------------
# ARGOSTrackingTool.py -- dictionaries
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Cristiana Falvo (cristiana.falvo@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

# read in data
raw_file = './Data/Raw/RawArgosData_SaraTurtleTrack.txt'
raw_data = open(raw_file, 'r')

# read all lines of file, add to list
data = raw_data.readlines()

# close file
raw_data.close()

# create two empty dictionary objects
date_dict = {}
coord_dict = {}
     
# iterating through lines -- using tuples   
for line in data:
    if line[0] in ('#', 'u'): # if the line's first character is in this tuple
        continue # then skip it
        
    # split string into data items
    lineData = line.split()

    # extract items in list into variables
    record_ID = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    #if obs_lc not in ('1','2','3'):
        #continue
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    # only keep data where lc value = 3, 2, or 1
    if obs_lc in ('1','2','3'):
    
        # populate date dict
        # establish key as record_ID, establish value as obs_date
        date_dict[record_ID] = obs_date
        
        # populate coord_dict
        # establish record_ID as key, tuple(long,lat) as value
        coord_dict[record_ID] = (obs_lon, obs_lat)
    
   
        
        

# it works at this point but each variable item above (recordID, etc) is overwritten
    # so each variable has the value of the last line right now
    # want to create dictionaries now
        # date dictionary
            # keys = uids, values = dates
                # key = record_ID
                # value = obs_date
        # location dictionary
            # keys = uids, values = tuple(long,lat)



