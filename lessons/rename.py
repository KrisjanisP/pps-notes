import os

# list files in directory
files = os.listdir('.')
for file in files:
    os.rename(file, file.replace(' ', '-'))