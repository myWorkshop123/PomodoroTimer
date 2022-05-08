# python program to play a sound
import playsound
import os

class TunePlayer:
    def __init__(self, sound_file_path):
        # validations
        # the path should be string
        if isinstance(sound_file_path,str):
            if os.path.exists(sound_file_path):
                self.sound_file_path = sound_file_path
            else:
                raise Exception('File Not found')
        else:
            raise Exception('File path format expected str, given {}'.format(type(sound_file_path)))

    def play(self):
        playsound.playsound(self.sound_file_path,block=False)
