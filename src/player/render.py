from utils import parse_show_time


def render_show_time(show_descr):
    fromTs = parse_show_time(show_descr['start'])
    toTs = parse_show_time(show_descr['stop'])
    return f"{fromTs.strftime('%d.%m.%y')} {fromTs.strftime('%H:%M')} - {toTs.strftime('%H:%M')}"
