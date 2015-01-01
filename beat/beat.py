'''Module to calculate beats(Swatch Internet Time).
'''

from time import localtime, timezone
import argparse
import pkg_resources

def internettime(hours, minutes, seconds, tzone):
    '''Returns time(Swatch Internet Time) in beats.
    '''
    itime = (((seconds + (minutes * 60) + ((hours + tzone + 1) * 3600)) / 86.4)
            % 1000)
    beats = int(itime)
    centibeats = str(itime).split(".")[1][0:3]
    return "@%s.%s" % (beats, centibeats)

def now(tzone):
    '''Gets the current time in beats.
    '''
    hours, minutes, seconds = localtime()[3:6]
    beats = internettime(hours, minutes, seconds, tzone)
    return beats

def main():
    '''The main function.
    '''
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-t', '--time', help='Time to convert (HH:MM:SS)')
    parser.add_argument('-z', '--timezone', metavar='TZ', type=float,
                        help='Timezone in hours, default: local timezone',
                        default=float(timezone/3600))
    parser.add_argument('-v', '--version', action='store_true')
    args = parser.parse_args()

    if args.version:
        print('.beat v{0}'.format(pkg_resources.get_distribution("beat").version))
        return
    if args.time:
        hours, minutes, seconds = args.time.split(":")
        print internettime(int(hours), int(minutes), int(seconds),
                           args.timezone)
    else:
        beats = now(tzone=args.timezone)
        print beats


if __name__ == "__main__":
    main()
