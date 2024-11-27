# Devesh Sukhdeo
# Period 1-2 
# 11/20/24
# Description: Creating a ringtone using Earsketch, 30 seconds, ABA format
from earsketch import *

setTempo(120)
init()

# Creating sound variables
intro = Y36_ELECTRO_1
background1 = COMMON_LOVE_DRUMBEAT_1
riser1 = BOYKINZ_NIGHT_BEAT_SWELL
riser2 = TECHNO_WHITENOISESFX_001
cym = YG_FUNK_CYMBALS_3
beat_sound = RD_POP_ARPBASS_2
chorus1 = RD_POP_ARPBASS_1
chorus2 = RD_ROCK_POPRHYTHM_MAINDRUMS_3 
beat1 ="0+0-00+0+0" 

#Create function for section A (Start & End)
def sectionA(startMeasure, endMeasure):
    fitMedia(intro, 1, startMeasure, endMeasure)
    fitMedia(background1, 2, startMeasure, endMeasure)

#Create function for section B (Middle)
def sectionB(startMeasure, endMeasure):
    fitMedia(chorus1, 3, startMeasure, endMeasure)
    fitMedia(chorus2, 4, startMeasure, endMeasure)
    for measure in range (startMeasure, endMeasure):
        makeBeat(beat_sound, 6, measure, beat1)

#Transitions    
fitMedia(riser1, 5, 6, 7)
fitMedia(riser2, 5, 11, 12)
fitMedia(cym, 5, 12, 12.5)

# Effects (Fades & Volume changes)
setEffect(6, VOLUME, GAIN, 5)
setEffect(1, VOLUME, GAIN, 10, 17, -60, 18)
setEffect(2, VOLUME, GAIN, 0, 15, -60, 16)

#Calling functions, for ABA arrangement
sectionA(1, 7)
sectionB(7,12)
sectionA(12, 18)

finish()
