
import os
'''
This is comment where we can add comment to the perticule task that we are going to done or for reference purpose
'''
def print_directory_contents(path="."):
    contents = os.listdir(path)
    for item in contents:
        print(item)

print_directory_contents()