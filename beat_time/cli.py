"""CLI for Internet Time."""

import argparse
from importlib.metadata import version

from beat_time.beat import internettime, now


def main():
    """The main function."""
    parser = argparse.ArgumentParser(description="Swatch Internet Time")
    parser.add_argument(
        "-c",
        "--centibeats",
        action="store_true",
        help="Display centibeats",
        default=False,
    )
    parser.add_argument("-t", "--time", help="Time to convert (HH:MM:SS)")
    parser.add_argument(
        "-z",
        "--timezone",
        metavar="TZ",
        type=float,
        help="Timezone in hours, default: UTC+01",
        default=1,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {version('beat-time')}",
    )
    args = parser.parse_args()

    if args.time:
        hours, minutes, seconds = args.time.split(":")
        print(
            internettime(
                int(hours), int(minutes), int(seconds), args.timezone, args.centibeats
            )
        )
    else:
        print(now(args.centibeats))


if __name__ == "__main__":
    main()
