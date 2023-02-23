from pydub import AudioSegment
#from pydub.playback import play

sound = AudioSegment.from_file("C:\\Users\\mysti\\Coding\\In_C_Gen\\In_C_Inst_354dsPianoOSA06.wav", format="wav")
#play(sound)

octaves = 1.5
new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
hipitch_sound = hipitch_sound.set_frame_rate(44100)

oufil = "C:\\Users\\mysti\\Coding\\In_C_Gen\\higherpitch.wav"
hipitch_sound.export(oufil, format="wav")

#play(hipitch_sound)