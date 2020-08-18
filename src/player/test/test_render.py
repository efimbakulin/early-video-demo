from unittest import TestCase

from freezegun import freeze_time
from parameterized import parameterized

from render import show_started


@freeze_time("2020-08-10 11:12:20 +03")
class RenderTests(TestCase):

    @parameterized.expand([
        ('20200810111213 +03', True),
        ('20200810111223 +03', False)
    ])
    def test_show_started(self, ts, expected):
        self.assertEqual(show_started({'start': ts}), expected)
