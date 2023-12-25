import random
import time
import pygame

pygame.init()

def play_shaking_single_DFPlayer(frequency, nr_of_files):

    folder="sounds/"
    sleeptime = 1/frequency

    sound = None
    while True:

        time.sleep(sleeptime)
        if sound:
            sound.stop()
        soundfile = random.randint(1,nr_of_files)
        sound = pygame.mixer.Sound("{}{}.wav".format(folder,str(soundfile).zfill(3)))
        sound.play()



def play_shaking_double_DFPlayer(frequency, nr_of_files, split_ch = None):
    folder = "sounds/"
    sleeptime = 1 / frequency

    sound1 = None
    sound2 = None
    counter = 0
    while True:
        time.sleep(sleeptime)
        soundfile = random.randint(1, nr_of_files)
        sound_path = "{}{}.wav".format(folder, str(soundfile).zfill(3))

        # If a sound is already playing, fade it out
        if counter % 2:
            if sound1:
                sound1.fadeout(int(sleeptime*1000))
            sound1 = pygame.mixer.Sound(sound_path)
            ch = sound1.play()
            if split_ch:
                ch.set_volume(0.0, 1.0)

        else:
            if sound2:
                sound2.fadeout(int(sleeptime*1000))
            sound2 = pygame.mixer.Sound(sound_path)
            ch = sound2.play()
            if split_ch:
                ch.set_volume(1.0, 0.0)
        
        counter+=1

            
#playshaking(2, 2)
play_shaking_double_DFPlayer(frequency= 4, nr_of_files= 2, split_ch=1)
