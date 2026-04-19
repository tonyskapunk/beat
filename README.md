# beat

A CLI tool and Python library for [Swatch® Internet Time](https://en.wikipedia.org/wiki/Swatch_Internet_Time) (.beats).

Swatch® Internet Time divides the day into 1000 beats (@000 to @999), with each beat equal to 1 minute and 26.4 seconds. It uses BMT (Biel Mean Time, UTC+1) as its reference timezone, eliminating the need for time zones or daylight saving conversions.

## Installation

```Shell
pip install beat-time
```

## CLI Options

| Flag                 | Description
|-----                 |------------
| `-c`, `--centibeats` | Display centibeats (fractional beats)
| `-t`, `--time`       | Time to convert in `HH:MM:SS` format
| `-z`, `--timezone`   | Timezone offset in hours (default: 1)
| `-v`, `--version`    | Show version

### CLI Usage

Get the current time in beats:

```Shell
$ beat
@123
```

With centibeats for more precision:

```Shell
$ beat -c
@123.456
```

Convert a specific time (HH:MM:SS) to beats:

```Shell
$ beat -t
@123
```

Specify a timezone offset (default is UTC+1/BMT):

```Shell
$ beat -t 1:57:46 -z 0
@123
```

Show version:

```Shell
$ beat -v
```

## Library Usage

```Python
import beat_time

# Current time in beats
beat_time.now()                 # '@123'
beat_time.now(centibeats=True)  # '@123.449'

# Convert a specific time (hours, minutes, seconds, timezone offset)
beat_time.internettime(1, 57, 46, tzone=0)                    # '@123'
beat_time.internettime(1, 57, 46, tzone=0, centibeats=True)   # '@123.449'
```

## Web Version

A standalone HTML version is available in [`docs/index.html`](docs/index.html) that displays the current beat time in the browser, updating every centibeat (864ms).

## License

[GPLv3](LICENSE)
