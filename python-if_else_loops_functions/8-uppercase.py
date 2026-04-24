#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter)<97:
            print(letter, end="")
        else:
            print(chr(65+(ord(letter)-97)), end="")
