from unittest import TestCase

import utils


class UriGeneratorTests(TestCase):
    def test_uri_generator(self):
        res = utils.generate_uri("localhost", 12345, "channel-id")
        self.assertEqual(res, "http://localhost:12345/channel-id/embed.html")
