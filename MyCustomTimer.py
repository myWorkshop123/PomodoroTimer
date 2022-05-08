import time


class MyCustomTimer:
    def __init__(self, hrs, mins, secs):
        if isinstance(hrs, int) and isinstance(mins, int) and isinstance(secs, int):
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
        # TODO perform typechecking here
        self.call_sleep()
        for funcs in args:
            if funcs.__name__ == 'display_popup':
                funcs()
            else:
                funcs()
