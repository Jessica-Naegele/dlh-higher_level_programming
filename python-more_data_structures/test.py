#!/usr/bin/python3
my_list=[(1, 2), (2, 1), (3, 10), (4, 2)]

new_list = [(x * y) for x, y in my_list]

j = []
for i in  range(0, len(my_list)):
    j.append(my_list[i][1])
    print(my_list[i][1])

print(new_list)
print(len(my_list))
print(sum(new_list))
print(sum(j))
#print(sum(my_list))
print(sum(new_list)/sum(j))