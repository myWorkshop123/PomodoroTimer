# this is the main Program
import TunePlayer, PopUpDisplayer, MyCustomTimer


class MainProgram:
    def __init__(self):
        # initialize tune player
        print('Program Started')
        sound_file_path = 'assets/alert_tune.wav'
        # Specify the hrs,minutes and seconds for study
        study_hrs, study_minutes, study_seconds = 0, 0, 20
        # Specify the hrs,minutes and seconds for rest
        rest_hrs, rest_minutes, rest_seconds = 0, 0, 5
        # Specify the total number of laps
        iterations = 3
        tune_player = TunePlayer.TunePlayer(sound_file_path)
        rest_message_displayer = PopUpDisplayer.PopUpDisplayer('Take Rest')
        study_meesage_displayer = PopUpDisplayer.PopUpDisplayer('Start Working')
        study_timer = MyCustomTimer.MyCustomTimer(study_hrs, study_minutes, study_seconds)
        rest_timer = MyCustomTimer.MyCustomTimer(rest_hrs, rest_minutes, rest_seconds)
        for i in range(iterations):
            print('Study Started')
            study_timer.do_something(tune_player.play, rest_message_displayer.display_popup)
            print('Rest Started')
            rest_timer.do_something(tune_player.play, study_meesage_displayer.display_popup)
            print(f'{i + 1} lap finished')


if __name__ == '__main__':
    MainProgram()
