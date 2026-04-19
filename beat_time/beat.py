"""Internet Time conversion (beats)."""

from datetime import datetime, timezone


def internettime(hours, minutes, seconds, tzone, centibeats=False):
    """Returns Internet Time in beats."""
    itime = ((seconds + (minutes * 60) + ((hours + tzone + 1) * 3600)) / 86.4) % 1000
    beats = int(itime)
    if centibeats:
        cbeats = str(itime).split(".")[1][:3]
        return f"@{beats}.{cbeats}"
    return f"@{beats}"


def now(centibeats=False):
    """Gets the current time in beats."""
    utc_now = datetime.now(timezone.utc)
    return internettime(utc_now.hour, utc_now.minute, utc_now.second, 0, centibeats)
