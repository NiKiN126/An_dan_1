#!/usr/bin/python3
# -*- coding: utf-8 -*-

# opens the file file.txt in read mode
fileptr = open("file.txt", "r")

if fileptr:
    print("file is opened successfully")

# closes the opened file
fileptr.close()
