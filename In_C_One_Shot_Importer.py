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
               
        if  filepath.endswith(".wav") and (('One' in str(filepath))  and ('Shot' in str(filepath)) and ((' A' in str(filepath)) or  ('_A' in str(filepath))) and ('Am' not in str(filepath))) and (('Hat' not in str(filepath))  and ('Kick' not in str(filepath)) and ('Roll' not in str(filepath))   and ('Cymbal' not in str(filepath)) and ('Crash' not in str(filepath)) and ('Snare' not in str(filepath)) and ('Clap' not in str(filepath)) and ('Vocal' not in str(filepath)) and ('Rim' not in str(filepath)) and ('Click' not in str(filepath)) and ('Glitch' not in str(filepath)) and ('Noise' not in str(filepath)) and ('Beep' not in str(filepath)) and ('Pop' not in str(filepath))  and ('Ride' not in str(filepath))  and ('Tamb' not in str(filepath))  and ('HH' not in str(filepath)) and ('Pad' not in str(filepath))  and ('hat' not in str(filepath)))  :

            content.append(filepath)

print("")

print("Gathering One Shots.")

x = len(content)

for ctr in range(x):
    atrack = content[ctr]
    trackname = atrack[-20:-4]
    tracknam = ""
    for m in trackname:
        if m.isalnum():
            tracknam += m

    outstr = 'C:\\Users\\mysti\\Coding\\In_C_Gen\\One_Shot_Bucket\\In_C_Inst_' + str(ctr) + tracknam + ".wav"

    try:
        shutil.copy(content[ctr], outstr)
        print("")
        print("Successful copy of Sample: ", str(ctr))

    except:
        print("")
        print("Copy/IO issue for Sample: ", str(ctr))

#call(["python", "DJProcessorNuAmb.py"])

## THE GHOST OF THE SHADOW ##
