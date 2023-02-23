from pydub import AudioSegment

def pitchshift(sound, pitch):

    new_sample_rate = int(sound.frame_rate * (2.0 ** pitch))
    nupitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    nupitch_sound = nupitch_sound.set_frame_rate(44100)

    return(nupitch_sound)

def notelen(newsound, len):

    inlen = len(newsound)

    if inlen >= len:
        outsound = newsound[0:len]

    if inlen < len:
        sillen = len - inlen
        silaud = AudioSegment.silent(duration = sillen)
        outsound = newsound + silaud

    return(outsound)
