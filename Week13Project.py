#!/usr/bin/env python3.7

import os

#Current Working Directory
directory = os.getcwd()

#EmptyList
files = []

#Looping
for filename in os.listdir(directory):
    
    #Size, Modified Time, Creation Time, Path
    file_size = os.path.getsize(filename)
    modified_time = os.path.getmtime(filename)
    creation_time = os.path.getctime(filename)
    file_path = os.path.realpath(filename)
   
    #Add Dictionary 
    files.append({'name': filename, 'size': file_size, 'time': modified_time, 'path': file_path})

#Print Dictionary    
print (*files,sep="\n")
    
    