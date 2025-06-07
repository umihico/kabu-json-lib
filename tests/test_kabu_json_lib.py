import unittest
from datetime import datetime
import pytz
from kabu_json_lib import bp, fetch_now


class TestKabuJsonLib(unittest.TestCase):
    def test_bp(self):
        self.assertEqual(bp(0.05), 500)
        self.assertEqual(bp(0.01), 100)
        self.assertEqual(bp(0), 0)
        self.assertIsNone(bp(None))

    def test_fetch_now(self):
        now = fetch_now()
        self.assertIsInstance(now, datetime)
        self.assertEqual(now.tzinfo, pytz.timezone("Asia/Tokyo"))


if __name__ == "__main__":
    unittest.main()
