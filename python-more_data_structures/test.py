#!/usr/bin/python3

roman_string = "DCCVII"

roman_no = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VII': 8, 'IX': 9, 'X': 10, 'XX': 20, 'XXX': 30, 'XL': 40, 'L': 50, 'LX': 60, 'LXX': 70, 'LXXX': 80, 'XC': 90, 'C': 100, 'CC': 200, 'CCC': 300, 'CD': 400, 'D': 500, 'DC': 600, 'DCC': 700, 'DCCC': 800, 'CM': 900, 'M': 1000, 'MM': 2000, 'MMM': 3000}
slice_string = roman_string
no = 0
x = 0
while x < len(roman_string):
    if slice_string[:2] in roman_no:
        x = x + 2
        j = slice_string[:2]
        slice_string = slice_string[2:]
        no = no + roman_no[j]
        print(slice_string) #helper
        print(j) #helper
        print(roman_no[j])
    else:
        x = x + 1
        print(slice_string)
        j = slice_string[0]
        slice_string = slice_string[1:]
        no = no + roman_no[j]
print(no)
