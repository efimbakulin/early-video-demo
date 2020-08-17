import json
import os
from urllib.parse import parse_qs

from jinja2 import Template

import template
from render import render_show_time
from utils import generate_query_string, parse_show_time

PAGE_TEMPLATE = Template(template.TEMPLATE)

with open(os.environ.get(
        'PROGRAMME_PATH', "/etc/flussonic/programme.json")) as f:
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
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    yield page.encode("utf-8")
