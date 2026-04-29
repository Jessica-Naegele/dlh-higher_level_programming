#!/usr/bin/python3
a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
key = 'LANG'
new_dict = dict()
k = ''
t = False
l = len(a_dictionary)
for i in a_dictionary:
    #print(a_dictionary[i])
    if a_dictionary[i] == key:
        t = True
print(t)
if t:
    for j in a_dictionary:
        if a_dictionary[j] != key:
            new_dict[j] = a_dictionary[j]
else: 
    new_dict = a_dictionary

print(new_dict)    


