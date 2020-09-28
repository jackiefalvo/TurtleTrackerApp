#-------------------------------------------------------------
# ARGOSTrackingTool.py -- user input
#
# Notes about user input function:
        # x = input("guess a number")
            # whatever the user inputs will be assigned to x
            # the value of x will be stored as a string
#
# Author: Cristiana Falvo (cristiana.falvo@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------
#%% create dictionaries with for loop

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
        continue # then skip it (continue reading through lines)
        
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
    
#%% examining date_dict
  
# how many keys are in date_dict      
print(len(date_dict.keys()))
    # there are 332 keys (UIDs) in date dict

# print values for first UID
print(date_dict['20616'])
    # so, each UID is associated with only one date
    # but note, there will be multiple UIDs that have the same date value
    
# hm, how many points were recorded on 7/3/2003 ?

# # true/false statement - does input match the key of this value
# d == date_dict['20616']

# script
d = input("enter date of interest")
count = 0

for item in date_dict:
    print(item)
    count += 1
    
print("count =", count)
    # what IS an item in date_dict? # ey/value pair?
    # this prints the UIDs


#%% back to video flow..using user input to search dict

# Ask user to enter search date
search_date = input("enter date to search for sara [M/D/YYYY] : ")

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
        continue # then skip it (continue reading through lines)
        
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
        
# loop through items in date_dict, collect keys that match user input

keys_of_interest = []

for date_item in date_dict.items():
    the_uid, the_date = date_item # separates two parts, names them
    if the_date == search_date:
        keys_of_interest.append(the_uid) # list of keys associated w/ user date
    
# inform the user if no records were found
if len(keys_of_interest) == 0:
    print(f"No observations on {search_date}")
        
# spits out the key(s) that are associated w/ the user inputted date
#print(keys_of_interest, len(keys_of_interest), "keys found") 

# reveal locations for the keys of interest 
for key in keys_of_interest:
    coords_of_interest = coord_dict[key] # indexing coord_dict by keys of interst
    #print(coords_of_interest)
     
    print(f"For UID {the_uid} Sara was pinged at {coords_of_interest}")

print(f"On {search_date}, Sara was pinged a total of", len(keys_of_interest), f"times.")
        
