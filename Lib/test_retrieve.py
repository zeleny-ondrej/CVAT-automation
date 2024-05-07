import unittest
from retrieve import Retrieve


class TestRetrieve(unittest.TestCase):
    def test_invalid_url(self):
        api = Retrieve()
        with self.assertRaises(Exception) as context:
            api.get_jobs()
            self.assertTrue(
                "Invalid host URL" in context.exception, "Test invalid "
            )

    # placeholders
    def test_invalid_password(self):
        pass

    def test_invalid_username(self):
        pass
