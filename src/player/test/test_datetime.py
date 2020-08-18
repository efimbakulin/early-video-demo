from datetime import datetime
from unittest import TestCase

from dateutil import tz
from parameterized import parameterized

import utils


class DateTimeTests(TestCase):
    @parameterized.expand([
        ('20200810111213 +03', datetime(2020, 8, 10,
                                        11, 12, 13, 0, tz.gettz('Europe/Moscow'))),
        ('20200810111213', datetime(2020, 8, 10, 11, 12, 13))
    ])
    def test_parse_xmltv_datetime(self, ts, expected):
        self.assertEqual(utils.parse_show_time(ts), expected)
