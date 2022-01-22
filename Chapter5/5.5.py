import os
try:
    with open('Mac.rtf', 'x') as f:
        print(f.read())
except FileExistsError as e:
    print("This file is exists")