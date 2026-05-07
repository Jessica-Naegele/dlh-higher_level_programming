#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

r = "OK\n\" if d is not None and len(d.strip()) > 0 else \"\" ; print(r, end=\"\")"

nb_characters = write_file("my_second_file.txt", r)
print(nb_characters)