#This code imports the necessary modules.

from pydub import AudioSegment
import random
import shutil
import os
from subprocess import call
from RandFunct import random_number
from RandFunct2 import random_number2

#srchstr = "C:\\Users\\mysti\\Desktop\\archback"

srchstr = 'F:\\Acid_Loops\\'

genlst = ['Rock', 'Jazz', 'Chill', 'Reg', 'Dub', 'Rhodes', 'Machine', 'Beach', 'Jungle', 'Ghost', 'Analog', 'Dark', 'Choir', 'Funk', 'Horns', 'Organ', 'Brass', 'Ocean', 'Space', 'Strings', 'Bells', 'Groove', 'Hip', 'Amb', 'Ele', 'Tech', 'Pop', 'Afr', 'Eth', 'Arab', 'Classic', 'Mode']

genlen = len(genlst)

gench = random_number(genlen)

genstr = genlst[gench]

print("")

print(genstr)

print("")

letstr = ['B', 'C', 'D', 'E', 'F', 'G', 'H']

content = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        filestr = str(filepath)

        filest = str(file)

        filechr = filest[-5:-4]

        filechr2 = filest[-6:-5]

        if  (filestr.endswith(".wav") and (genstr in filestr)) and  ('Vo' not in filestr): 
            isn = 0
            for stri in letstr:
                if filechr2.startswith(stri): 
                    isn += 1
            if isn == 0:
                content.append(filepath)

print("")

print("Gathering Samples.")

x = len(content)

x1 = 2000

if x1 >= x:
    x1 = x

for ctr in range(x1):
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
