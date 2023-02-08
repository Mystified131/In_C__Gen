from pydub import AudioSegment
import random
import shutil
import os
import numpy as np
import math
import datetime
from subprocess import call
from RandFunct import random_number
from RandFunct2 import random_number2
from pydub.playback import play
import time

def noteshift(insound, pitch, leng):

    leng2 = int(leng / 3)

    if isinstance(pitch, str):
        silaud = AudioSegment.silent(duration = leng2)
        return(silaud)

    if not isinstance(pitch, str):

        try:

            asound = AudioSegment.from_wav(insound)

        except:

            print("")
            print("New sound error.")
            silaud = AudioSegment.silent(duration = leng2)
            return(silaud)

        new_sample_rate = int(asound.frame_rate * (2.0 ** pitch))
        nupitch_sound = asound._spawn(asound.raw_data, overrides={'frame_rate': new_sample_rate})
        nupitch_sound = nupitch_sound.set_frame_rate(44100)

        inlen = len(nupitch_sound)

        if inlen >= leng2:
            outsound2 = nupitch_sound.fade_in(10)
            outsound4 = outsound2.fade_out(10)

        if inlen < leng2:
            sillen = leng2 - inlen
            silaud = AudioSegment.silent(duration = sillen)
            outsound2 = nupitch_sound.fade_in(10)
            outsound3 = outsound2.fade_out(10)
            outsound4 = outsound3 + silaud

        return outsound4

def trakdubber(gamsnd, otrack):

    betasnd = AudioSegment.from_wav(otrack)

    gamsnd2 = betasnd.overlay(gamsnd)

    return gamsnd2

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

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
               
        if  filepath.endswith(".wav") and ("In_C_Inst" in str(filepath)):
            content.append(filepath)

voices = 35

conlen = len(content)

print("")

print("Gathering One Shots.")

for ctr in range(voices):
    rannum = random_number(conlen)
    movstr = content[rannum]

    outstr = 'C:\\Users\\mysti\\Coding\\In_C_Gen\\In_C_Voice_' + str(ctr) + ".wav"

    try:
        shutil.copy(movstr, outstr)
        #contvox.append(outstr)
        print("")
        print("Successful copy of Sample: ", str(ctr))

    except:
        print("")
        print("Copy/IO issue for Sample: ", str(ctr))

contvox = []

voic = len(contvox)

srchstr2 = "C:\\Users\\mysti\\Coding\\In_C_Gen"

for subdir, dirs, files in os.walk(srchstr2):
    for file in files:
        filepath = subdir + os.sep + file
               
        if  filepath.endswith(".wav") and 'In_C_Voice' in str(filepath):
            contvox.append(filepath)

seg = 0

totvoxlen = 38

trklen = 340000

contlen = len(contvox)

sonlist = []

for cr in range(totvoxlen):

    conran = random_number(contlen)

    trakval = contvox[conran]

    sonlist.append(trakval)

totvoxlen = 8

seglen = 8

for segmen in range(seglen):

    segn = segmen + 1

    print("")

    print("Starting composing for segment: ", segn)

    print("")

    print("Of a total number of segments: ", seglen)

    for voc in range(totvoxlen):

        #trkval = contvox[voc]

        pattlen = len(pattdict)

        phrcomp =  AudioSegment.silent(0)

        phrchoc = 1

        trkval = sonlist[voc]

        for pgen in range(pattlen):

            ppush = int((53 / seglen) * seg)

            phrchoc += ppush

            if phrchoc > 53:
                phrchoc = 1

            patvals = pattdict[phrchoc]

            print("")

            print(patvals)

            notnum = len(patvals)

            phraud =  AudioSegment.silent(0)

            for notspec in range(notnum):

                phrvals = patvals[notspec]

                pitval = phrvals[0]
                durval = phrvals[1]

                #newnot = AudioSegment.silent(0)

                #print("")

                #print("Building note: " + str(pitval))

                newnot = noteshift(trkval, pitval, durval)

                phraud += newnot

            phrcomp += phraud

            print("")

            print("Adding pattern number: ", str(phrchoc))

            print("")

            print("For phrase number: ", str(pgen))

            print("")

            vocchk = voc + 1

            print("Using voice number: ", str(vocchk))

            #phrlen = int(phrcomp.duration_seconds)

            phrlen = len(phrcomp)

            print("")

            print("Current phrase build, out of 340000 milliseconds, is ", phrlen)

            if phrlen > trklen:

                phrcomp2 = phrcomp[0:trklen]

                phrcomp3 = phrcomp2 - 12
                
                phrcomp4 = phrcomp3.set_frame_rate(44100)

                ostr = 'C:\\Users\\mysti\\Coding\\In_C_Gen\\In_C_VoxSegment_' + str(vocchk) +  ".wav"

                phrcomp4.export(ostr, format="wav")

                break
            
            if phrlen <= trklen:
                
                ranrep = random_number(10)

                if ranrep > 5:

                    phrchoc += 1

    #seg += 1

    #if seg >= 8:

    #outstr = 'C:\\Users\\mysti\\Coding\\In_C_Gen\\In_C_VoxSegment_' + str(seg) +  ".wav"

    #try:

        #segcomp.export(outstr, format="wav")

        #print("")
        #print("Successful render of segment.")

    #except:

        #print("")
        #print("Gen/IO issue for segment.")

    #if seg > 8:

    contenttrk = []

    for subdir, dirs, files in os.walk(srchstr2):
        for file in files:
            filepath = subdir + os.sep + file
                
            if  filepath.endswith(".wav") and ("VoxSegment" in str(filepath)):
                contenttrk.append(filepath)

    gamsnd = AudioSegment.silent(duration = trklen)

    conalen = len(contenttrk)

    print("")

    print("Assembling tracks into a segment.")

    for otrak in range(conalen):

        print("")

        print("Dubbing track: ", otrak)

        ttrak = contenttrk[otrak]

        gamsnd = trakdubber(gamsnd, ttrak)

    otstr = 'C:\\Users\\mysti\\Coding\\In_C_Gen\\In_C_MixSegment_' + str(tim) + "_" + str(segn) + ".wav"

    gamsnd.export(otstr, format="wav")

    print("")

    print("Generation complete for segment: ", segn)

print("")

print("Generation complete, segments in same folder as code.")

exit

## THE GHOST OF THE SHADOW ##

        


    

