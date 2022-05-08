# Create a program where the user specifies a hrs, b minutes, c seconds and after that duration he should
# see hello world on the display

#TODO Take the input from user
# hrs,minutes,seconds = 0,0,3

# print hello world after the mentioned time
import time
# time.sleep(seconds)
# print('hello world')
#
# def convert_hours_and_minutes_into_seconds(hours,minutes,seconds):
#     seconds = hours * 60 * 60 + minutes * 60 + seconds
#     return seconds
#
# def call_sleep():
#     seconds = convert_hours_and_minutes_into_seconds(hrs,minutes,seconds=3)
#     time.sleep(seconds)
#     print('hello')

class MyCustomTimer:
    def __init__(self,hrs,mins,secs):
        if isinstance(hrs,int) and isinstance(mins,int) and isinstance(secs,int):
            if hrs >= 0 and mins >= 0 and secs >= 0:
                if secs <= 60 and mins <= 60:
                    self.hrs = hrs
                    self.mins = mins
                    self.secs = secs
                else:
                    raise Exception('Seconds and Minutes should be less than or equal to 60')
            else:
                raise Exception('Negative values not allowed')
        else:
            raise Exception('hours,minutes and seconds have to be integer only')

    def transform_everything_into_seconds(self):
        result = self.hrs * 60 * 60 + self.mins * 60 + self.secs
        return result

    def call_sleep(self):
        total_second = self.transform_everything_into_seconds()
        time.sleep(total_second)
    def do_something(self, *args):
        #TODO perform typechecking here
        self.call_sleep()
        print(f'Time up do your thing after {self.hrs} hrs, {self.mins} minutes and {self.secs} seconds')
        for funcs in args:
            funcs()


