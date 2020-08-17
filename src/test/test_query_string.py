from datetime import datetime, timedelta, timezone
from unittest import TestCase

from freezegun import freeze_time

from player import utils


@freeze_time("2020-08-10 10:00:00 +03")
class QueryStringGeneratorTests(TestCase):
    def test_finished(self):
        fromts = datetime.now(timezone.utc) - timedelta(minutes=50)
        tots = datetime.now(timezone.utc) - timedelta(minutes=5)
        qs = utils.generate_query_string(fromts, tots)
        self.assertEqual(qs, 'from=1597039800&to=1597042500')

    def test_in_progress(self):
        fromts = datetime.now(timezone.utc) - timedelta(minutes=50)
        tots = datetime.now(timezone.utc) + timedelta(minutes=5)
        qs = utils.generate_query_string(fromts, tots)
        self.assertEqual(qs, 'from=1597039800')

    def test_live(self):
        expected = 'ago=3600'
        self.assertEqual(utils.generate_query_string(None, datetime.now(timezone.utc)),
                         expected)
        self.assertEqual(utils.generate_query_string(datetime.now(timezone.utc), None),
                         expected)
        self.assertEqual(utils.generate_query_string(datetime.now(timezone.utc) + timedelta(minutes=1), None),
                         expected)
