#This code imports the necessary modules.

from pydub import AudioSegment
import random
import shutil
import os
from subprocess import call
from RandFunct import random_number
from RandFunct2 import random_number2

#srchstr = "C:\\Users\\mysti\\Desktop\\archback"

srchstr = 'E:\\Acid_Loops\\'

content = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        filestr = str(filepath)

        filest = str(file)

        filechr = filest[-5:-4]

        filechr2 = filest[-6:-5]

        letstr = ['B', 'C', 'D', 'E', 'F', 'G', 'H']

        #print(filechr)
               
        if  (filestr.endswith(".wav") and ('Orch' in filestr)): 
            isn = 0
            for stri in letstr:
                if filechr2.startswith(stri): 
                    isn += 1
            if isn == 0:
                content.append(filepath)

print("")

print("Gathering Samples.")

x = len(content)

for ctr in range(x):
    atrack = content[ctr]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m

    outstr = 'C:\\Users\\mysti\\Coding\\In_C_Gen\\Sources_Bucket\\In_C_Inst_Vapr_' + str(ctr) + tracknam + ".wav"

    #try:
    shutil.copy(content[ctr], outstr)
    print("")
    print("Successful copy of Sample: ", str(ctr))
    
    #except:
        #print("")
        #print("Copy/IO issue for Sample: ", str(ctr))

call(["python", "In_C_Gen_Mallet.py"])

## THE GHOST OF THE SHADOW ##
