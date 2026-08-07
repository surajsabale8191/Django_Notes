
import os

def print_directory_contents(path="."):
    contents = os.listdir(path)
    for item in contents:
        print(item)

print_directory_contents()