'''Module to calculate beats(Swatch Internet Time).
'''

from time import localtime
import argparse

def internettime(hours, minutes, seconds, tzone=0):
    '''Returns time(Swatch Internet Time) in beats.
    '''
    itime = (((seconds + (minutes * 60) + ((hours - tzone + 1) * 3600)) / 86.4)
            % 1000)
    beats = int(itime)
    centibeats = str(itime).split(".")[1][0:3]
    return "@%s.%s" % (beats, centibeats)

def now():
    '''Gets the current time in beats.
    '''
    hours, minutes, seconds = localtime()[3:6]
    beats = internettime(hours, minutes, seconds)
    return beats

def main():
    '''The main function.
    '''
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-t', '--time', help='Time to convert (HH:MM:SS)')
    parser.add_argument('-z', '--timezone', default=0, type=int,
                        help='Timezone in hours, default 0(UTC), sorry no '
                        'support(yet) to zones with less than an hour TZ.')
    args = parser.parse_args()
    if args.time:
        hours, minutes, seconds = args.time.split(":")
        print internettime(int(hours), int(minutes), int(seconds),
                           args.timezone)
    else:
        beats = now()
        print beats


if __name__ == "__main__":
    main()
