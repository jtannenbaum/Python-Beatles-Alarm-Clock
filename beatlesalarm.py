import time, os, sys, random

ABSPATH = "/media/[re]drive_/Deluge Downloads/The Beatles Stereo 2009 Remasters/"

slist = """
The Beatles - 2009 - Abbey Road (2009 Stereo Remaster) [FLAC]/04 - Oh! Darling.flac
The Beatles - 2009 - The Beatles Disc 1 (2009 Stereo Remaster) [FLAC]/01 - Back in the U.S.S.R..flac
The Beatles - 2009 - The Beatles Disc 1 (2009 Stereo Remaster) [FLAC]/02 - Dear Prudence.flac
The Beatles - 2009 - The Beatles Disc 1 (2009 Stereo Remaster) [FLAC]/11 - Blackbird.flac
The Beatles - 2009 - Yellow Submarine (2009 Stereo Remaster) [FLAC]/06 - All You Need Is Love.flac
The Beatles - 2009 - Yellow Submarine (2009 Stereo Remaster) [FLAC]/04 - Hey Bulldog.flac
The Beatles - 2009 - Abbey Road (2009 Stereo Remaster) [FLAC]/05 - Octopus's Garden.flac
The Beatles - 2009 - Abbey Road (2009 Stereo Remaster) [FLAC]/07 - Here Comes The Sun.flac
The Beatles - 2009 - Abbey Road (2009 Stereo Remaster) [FLAC]/02 - Something.flac
The Beatles - 2009 - Abbey Road (2009 Stereo Remaster) [FLAC]/08 - Because.flac
The Beatles - 2009 - Help! (2009 Stereo Remaster) [FLAC]/01 - Help!.flac
The Beatles - 2009 - A Hard Day's Night (2009 Stereo Remaster) [FLAC]/02 - I Should Have Known Better.flac
The Beatles - 2009 - Please Please Me (2009 Stereo Remaster) [FLAC]/05 - Boys.flac
The Beatles - 2009 - Past Masters Disc 2 (2009 Stereo Remaster) [FLAC]/07 - Hey Jude.flac
The Beatles - 2009 - Past Masters Disc 2 (2009 Stereo Remaster) [FLAC]/03 - Paperback Writer.flac
The Beatles - 2009 - Magical Mystery Tour (2009 Stereo Remaster) [FLAC]/09 - Penny Lane.flac
The Beatles - 2009 - Magical Mystery Tour (2009 Stereo Remaster) [FLAC]/07 - Hello Goodbye.flac
"""


flist = [a for a in slist.split('\n') if a] # 'if a' eliminates any blank strings 

flist = [ABSPATH + a for a in flist] # update flist to have full paths

playing = False
while True:
    if not playing: print 'current hour: ' + time.strftime('%H')
    if time.strftime('%H') == '08' and not playing : # == 'xx' if it's the xxth hour of the day
        playing = True # avoids starting multiple mplayers
        path = flist[random.randint(0, len(flist)-1)] # random element of flist
        os.system('mplayer "' + path + '"')
    time.sleep(5.0)
