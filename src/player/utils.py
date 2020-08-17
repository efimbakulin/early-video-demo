from datetime import datetime, timezone
from urllib.parse import urlencode

from dateutil.parser import parse


def parse_show_time(ts):
    return parse(ts)


def generate_query_string(tsfrom=None, tsto=None):
    now = datetime.now(timezone.utc)
    if tsfrom is None or tsto is None or tsfrom > now:  # live show
        qs = {'ago': 3600}
    else:
        qs = {}
        if (now > tsfrom):
            qs['from'] = int(tsfrom.timestamp())
        if (now > tsto):
            qs['to'] = int(tsto.timestamp())
    return urlencode(qs)


def generate_uri(host, port, channel):
    return f"http://{host}:{port}/{channel}/embed.html"
