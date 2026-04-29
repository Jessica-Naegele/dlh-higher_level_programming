#!/usr/bin/python3
a_dictionary = { 'c': "a", 'd': "a"  }
value = 'a'

print(value)
new_dict = dict()
t = False
for i in a_dictionary:
    if a_dictionary[i] == value:
        t = True
    print(t)
if t:
    for j in a_dictionary:
        print(j)
        if a_dictionary[j] != value:
            print(a_dictionary[j])
            new_dict[j] = a_dictionary[j]
    a_dictionary = new_dict
print(a_dictionary)
