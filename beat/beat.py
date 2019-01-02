'''Module to calculate beats(Swatch Internet Time).
'''

import argparse
import pkg_resources
from datetime import datetime

def internettime(hours, minutes, seconds, tzone):
    '''Returns time(Swatch Internet Time) in beats.
    '''
    itime = (((seconds + (minutes * 60) + ((hours + tzone + 1) * 3600)) / 86.4)
            % 1000)
    beats = int(itime)
    centibeats = str(itime).split(".")[1][0:3]
    return '@{0}.{1}'.format(beats, centibeats)

def now():
    '''Gets the current time in beats.
    '''
    utc_now = datetime.utcnow()
    beats = internettime(utc_now.hour, utc_now.minute, utc_now.second, tzone=0)
    return beats

def main():
    '''The main function.
    '''
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-t', '--time', help='Time to convert (HH:MM:SS)')
    parser.add_argument('-z', '--timezone', metavar='TZ', type=float,
                        help='Timezone in hours, default: UTC+01',
                        default=1)
    parser.add_argument('-v', '--version', action='store_true')
    args = parser.parse_args()

    if args.version:
        print('.beat v{0}'.format(pkg_resources.get_distribution("beat").version))
        return
    if args.time:
        hours, minutes, seconds = args.time.split(":")
        print(internettime(int(hours), int(minutes), int(seconds),
                           args.timezone))
    else:
        beats = now()
        print(beats)


if __name__ == "__main__":
    main()
