from pathlib import Path
import os

srcFolder = input(Path(r"Enter the location of the folder you would like to change: "))
os.chdir(srcFolder)
srcFiles = os.listdir(srcFolder)
origExt = input("Enter the original extension: ").lower()
newExt = input("Enter the new extension: ").lower()
num = 1
for filename in srcFiles:
    if filename.endswith(origExt):
        name, ext = os.path.splitext(filename)
        os.rename(filename, name + "." + newExt)
        num += 1
print("Done")
