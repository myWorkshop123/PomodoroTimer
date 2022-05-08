# TODO Display a popup to user with custom mesage and a button ok

class PopUpDisplayer:
    def __init__(self, msg):
        if isinstance(msg, str):
            if msg != '' or msg != '\n' or msg != '\t' or len(msg) > 0:
                self.msg = msg
            else:
                raise Exception('Message given as empty string, just the tab or \n are also not allowed')
        else:
            raise Exception

    def display_popup(self):
        print(self.msg)
