# this is the main Program
import TunePlayer,PopUpDisplayer,MyCustomTimer

class MainProgram:
    def __init__(self):
        # initialize tune player
        sound_file_path = 'assets/alert_tune.wav'
        tune_player = TunePlayer.TunePlayer(sound_file_path)
        popup_display = PopUpDisplayer.PopUpDisplayer('Times Up Buddy Take some rest now')
        # Specify the hrs,minutes and seconds
        hrs = 0
        minutes = 0
        seconds = 10

        timer = MyCustomTimer.MyCustomTimer(hrs,minutes,seconds)
        timer.do_something(tune_player.play , popup_display.display_popup)






if __name__ == '__main__':
    MainProgram()