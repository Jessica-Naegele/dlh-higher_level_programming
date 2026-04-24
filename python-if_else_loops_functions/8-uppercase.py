#!/usr/bin/python3
def uppercase(str):
    new_str =""
    for i in range (0,len(str)):
        if ord(str[i])<97:
            new_str = new_str + str[i]
        else:
            new_str = new_str + chr(65+(ord(str[i])-97))
    print("{}".format(new_str))
