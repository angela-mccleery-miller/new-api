import os, glob

os.chdir("/C/Angela Miller/Desktop/coding/python/pythonalgorithms")
for file in glob.glob("*.jpg"):
    print(file)