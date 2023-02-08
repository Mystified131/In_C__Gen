from pydub import AudioSegment
import random
import shutil
import os
from subprocess import call
from RandFunct import random_number
from RandFunct2 import random_number2

def noteshift(insound, pitch, len):

    if isinstance(pitch, str):
        silaud = AudioSegment.silent(duration = len)
        return(silaud)

    if not isinstance(pitch, str):

        asound = AudioSegment.from_wav(insound)

        new_sample_rate = int(asound.frame_rate * (2.0 ** pitch))
        nupitch_sound = asound._spawn(asound.raw_data, overrides={'frame_rate': new_sample_rate})
        nupitch_sound = nupitch_sound.set_frame_rate(44100)

        inlen = (asound.duration_seconds * 1000)

        if inlen >= len:
            outsound = nupitch_sound[0:len]

        if inlen < len:
            sillen = len - inlen
            silaud = AudioSegment.silent(duration = sillen)
            outsound = nupitch_sound + silaud

        return(outsound)

pattdict = {}

pattdict = {}

pattdict[1] = [(-.333, 80),(-.249, 920),(-.333, 80),(-.249, 920),(-.333, 80),(-.249, 920)]
pattdict[2] = [(-.333, 80),(-.249, 420),(-.167, 500),(-.249, 1000)]
pattdict[3] = [('sil', 500),(-.249, 500),(-.167, 500),(-.249, 500)]
pattdict[4] = [('sil', 500),(-.249, 500),(-.167, 500),(-.083, 500)]
pattdict[5] = [(-.249, 500),(-.167, 500),(-.083, 500),('sil', 500)]
pattdict[6] = [(.167, 8000)]
pattdict[7] = [('sil', 3500),(-.416, 250),(-.416, 250),(-.416, 500),('sil', 2500)]
pattdict[8] = [(-.083, 4000),(-.167, 8000)]
pattdict[9] = [(.083, 250),(-.083, 250),('sil', 3500)]
pattdict[10] = [(.083, 250),(-.083, 250)]
pattdict[11] = [(-.167, 250),(-.083, 250),(.083, 250),(-.083, 250),(.083, 250),(-.083, 250)]
pattdict[12] = [(-.167, 500),(-.083, 500),(.083, 4000),(.167, 1000)]
pattdict[13] = [(.083, 250),(-.083, 750),(-.083, 250),(-.167, 250),(-.083, 500),('sil', 750),(-.083, 2250)]
pattdict[14] = [(.167, 4000),(.083, 4000),(-.083, 4000),(-.125, 4000)]
pattdict[15] = [(-.083, 250),('sil', 3750)]
pattdict[16] = [(-.083, 250),(.083, 250),(.167, 250),(.083, 250)]
pattdict[17] = [(.083, 250),(.167, 250),(.083, 250),(.167, 250),(.083, 250),('sil', 250)]
pattdict[18] = [(-.249, 250),(-.125, 250),(-.249, 250),(-.125, 250),(-.249, 750),(-.249, 250)]
pattdict[19] = [('sil', 1500),(6, 1500)]
pattdict[20] = [(-.249,250),(-.125, 250),(-.249, 250),(-.125, 250),(-.666, 750),(-.249, 250),(-.125, 250),(-.249, 250),(-.125, 250),(-.249, 250)]
pattdict[21] = [(-.125, 3000)]
pattdict[22] = [(-.249, 750),(-.249, 750),(-.249, 750),(-.249, 750),(-.249, 750),(-.125, 750),(-.083, 750),(0, 750),(.083, 500)]
pattdict[23] = [(-.249, 500),(-.125, 750),(-.125, 750),(-.125, 750),(-.125, 750),(-.125, 750),(-.083, 750),(0, 750),(.083, 750)]
pattdict[24] = [(-.249, 500),(-.125, 500),(-.083, 750),(-.083, 750), (-.083, 750), (-.083, 750), (-.083, 750),(0, 750),(.083, 500)]
pattdict[25] = [(-.249, 500),(-.125, 500),(-.083, 500),(0, 750),(0, 750),(0, 750),(0, 750),(0, 750),(0, 750),(.083, 750)]
pattdict[26] = [(-.249, 500),(-.125, 500),(-.083, 500),(0, 500),(.167, 750),(.167, 750),(.167, 750),(.167, 750),(.167, 750),(.167, 750)]
pattdict[27] = [(-.167, 500),(-.125, 500),(-.167, 500),(-.125, 500),(-.083, 500),(-.167, 250),(-.083, 250),(-.167, 500),(-.249, 500),(-.167, 500),(-.249, 500)]
pattdict[28] = [(-.249, 500),(-.125, 500),(-.249, 500),(-.125, 500),(-.249, 750),(-.249, 250)]
pattdict[29] = [(-.167, 3000),(-.083, 3000),(.167, 3000)]
pattdict[30] = [(.167, 6000)]
pattdict[31] = [(-.083, 500),(-.167, 500),(-.083, 500),(0, 500),(-.083, 500),(0, 500)]
pattdict[32] = [(-.167, 500),(-.083, 500),(-.167, 500),(-.083, 500),(0, 500),(-.167, 3500),(-.083, 750)]
pattdict[33] = [(-.083, 250),(-.167, 250),('sil', 500)]
pattdict[34] = [(-.083, 250),(-.167, 250)]
pattdict[35] = [(-.167, 500),(-.083, 500),(.083, 500),(-.083, 500),(.083, 500),(-.083, 500),(.083, 500),(-.083, 500),(.083, 500),(.083, 500),('sil', 3500),(.5, 1000),(.583, 3000)]
pattdict[36] = [(-.083, 500),(-.083, 500),(.083, 500),(-.083, 500),(.083, 500),(-.083,500)]
pattdict[37] = [(-.167, 250),(-.083, 250)]
pattdict[38] = [(-.083, 250),(-.083, 250),(.167, 250)]
pattdict[39] = [(.083, 250),(-.083, 250),(-.167, 250),(-.083, 250),(.083, 250),(.167, 250)]
pattdict[40] = [(.083, 250),(-.167, 250)]
pattdict[41] = [(.083, 250),(-.083, 250)]
pattdict[42] = [(.167, 4000),(.083, 4000),(0, 4000),(.167, 4000)]
pattdict[43] = [(.042, 250),(.333, 250),(.042, 250),(.333, 250),(.333, 500),(.333, 500),(.042, 500),(.042, 250),(.333, 250)]
pattdict[44] = [(.042, 500),(.333, 1000),(.333, 500),(.167, 1000)]
pattdict[45] = [(.167, 4000),(.083, 4000),(0, 4000),(.167, 4000)]
pattdict[46] = [(-.083, 250),(.249, 250),(.333, 250),(.249, 250),('sil', 500),(-.083, 500),('sil', 500),(-.083, 500),('sil', 500),(-.083, 500),(-.083, 250),(.249, 250),(.333, 250),(.249, 250)]
pattdict[47] = [(.249, 250),(.333, 250),(.249, 500)]
pattdict[48] = [(-.167, 3000),(-.083, 2000),(-.167, 3000)]
pattdict[49] = [(-.167, 250),(-.083, 250),(.5, 250),(-.083, 250),(.5, 250),(-.167, 250)]
pattdict[50] = [(-.167, 250),(-.083, 250)]
pattdict[51] = [(-.167, 250),(-.083, 250),(.5, 250)]
pattdict[52] = [(-.083, 250),(.5, 250)]
pattdict[53] = [(.5, 250),(-.083, 250)]

srchstr = "C:\\Users\\mysti\\Coding\\In_C_Gen\\One_Shot_Bucket"

content = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file
               
        if  filepath.endswith(".wav"):
            content.append(filepath)

voices = 35
conlen = len(content)

print("")

print("Gathering One Shots.")

contvox = []

for ctr in range(voices):
    rannum = random_number(conlen)
    movstr = content[rannum]

    outstr = 'C:\\Users\\mysti\\Coding\\In_C_Gen\\In_C_Voice_' + str(ctr) + ".wav"

    try:
        shutil.copy(movstr, outstr)
        contvox.append(outstr)
        print("")
        print("Successful copy of Sample: ", str(ctr))

    except:
        print("")
        print("Copy/IO issue for Sample: ", str(ctr))

#print(contvox)

totvoxlen = len(contvox)

for voc in range(totvoxlen):

    trkval = contvox[voc]

    #insnd = AudioSegment.from_wav(trkval)

    pattlen = len(pattdict)

    for pgen in range(pattlen):

        patvals = pattdict[pgen + 1]

        print("")

        print(patvals)

        notnum = len(patvals)

        phraud =  AudioSegment.silent(0)

        for notspec in range(notnum):

            phrvals = patvals[notspec]

            pitval = phrvals[0]
            durval = phrvals[1]

            newnot = AudioSegment.silent(0)

            print("")

            print("Building: " + str(pitval) + ": " + str(durval))

            newnot = noteshift(trkval, pitval, durval)

            phraud += newnot

            outstr = 'C:\\Users\\mysti\\Coding\\In_C_Gen\\In_C_VoxPatt_' + str(voc) + "_" + str(pgen) + ".wav"

            try:

                phraud.export(outstr, format="wav")

                print("")
                print("Successful copy of Pattern.")

            except:

                print("")
                print("Copy/IO issue for Pattern.")

        


    

