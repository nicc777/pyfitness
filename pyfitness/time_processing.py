class TimeOverDistance:
    def __init__(self, hours=0, min=0, sec=0):
        self.hours = hours
        self.min = min
        self.sec = sec
        self.total_sec = sec + (min * 60) + (hours * 60 * 60)

    def calc_min_per_distance(self, distance=0, distance_unit='Km'):
        secs = self.total_sec / distance
        hours = 0
        mins = 0
        if secs > (60*60):
            hours = int(secs/(60*60))
            secs -= (hours*(60*60))
        if secs > 60:
            mins = int(secs / 60)
            secs -= (mins * 60)
        print('{:03d}:{:02d}:{:04.2f} per {:s}'.format(hours, mins, secs, distance_unit))

# EOF
