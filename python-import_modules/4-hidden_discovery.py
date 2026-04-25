#!/usr/bin/python3
import hidden_4
features = dir(hidden_4)
features_sort = sorted(features)
count = len(features_sort)
if __name__ == "__main__":
    for i in range (0, count):
        if features_sort[i].startswith("__") == False:
            print(features_sort[i])
