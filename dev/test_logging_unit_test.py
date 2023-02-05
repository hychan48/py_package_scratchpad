import unittest

# Also works in unittest. works in both pytest and unittest
class MyTestCase(unittest.TestCase):
    def test_something(self):
        import logging
        logging.info('info from unittest')
        logging.debug('debug from unittest')
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
