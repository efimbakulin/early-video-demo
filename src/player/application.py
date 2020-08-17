import json
import os
from urllib.parse import parse_qs

from dateutil.parser import parse
from jinja2 import Template

from render import render_show_time
from utils import generate_query_string, parse_show_time

CONFIG = None
PAGE_TEMPLATE = None
PROGRAMMES = None


def init():
    global CONFIG, PAGE_TEMPLATE, PROGRAMMES

    config_path = os.environ.get(
        'PLAYER_CONFIG', "/etc/flussonic/application.conf")

    with open(config_path) as f:
        CONFIG = json.load(f)

    with open(CONFIG['page_template']) as f:
        PAGE_TEMPLATE = Template(f.read())

    with open(CONFIG['programme']) as f:
        PROGRAMMES = json.load(f)


def application(env, start_response):
    qs = parse_qs(env.get('QUERY_STRING', ''))
    channel_id = qs.get('c', ['1']).pop()
    programme_id = qs.get('p', None)
    channel = PROGRAMMES['channels'][channel_id]
    fromts = tots = None
    if programme_id:
        programme_id = int(programme_id.pop())
        show = channel['programme'][programme_id]
        fromts = parse_show_time(show['start'])
        tots = parse_show_time(show['stop'])

    qs = generate_query_string(fromts, tots)

    ctx = {
        'render_show_time': render_show_time,
        'channels': PROGRAMMES['channels'],
        'channel_id': channel_id,
        'streaming_qs': qs
    }
    page = PAGE_TEMPLATE.render(**ctx)
    print(page)


init()


if __name__ == '__main__':
    application({'QUERY_STRING': 'c=1&p=3'}, None)
