#!/usr/bin/python3
import os
os.write(1, bytes(list(range(65, 91)) + [10]))
