import os

srchstr = 'C:\\Users\\mysti\\Coding\\In_C_Gen\\Sources_Bucket'

content = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file
               
        if  filepath.endswith(".wav") and not (filepath.endswith('1')):
            os.remove(filepath)

print("")

print("Finished with operation.")

