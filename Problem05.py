import os

# Select the whose content you want to list
path = '/'
contents = os.listdir(path)
# use the os module to list the directory content 

for item in contents:
    print(item)