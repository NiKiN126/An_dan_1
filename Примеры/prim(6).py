#!/usr/bin/python3
# -*- coding: utf-8 -*-

# open the file.txt in read mode. causes an error if no such file exists.
fileptr = open("file2.txt", "r")
# running a for loop
for i in fileptr:
    print(i)  # i contains each line of the file

# closes the opened file
fileptr.close()
