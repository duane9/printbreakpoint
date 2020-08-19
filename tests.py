import unittest
from io import StringIO

from printbreakpoint import pb


class TestPrintBreakpoint(unittest.TestCase):

    def test_pb(self):
        out_file = StringIO()
        pb('test', out_file=out_file)
        expected = '\x1b[92mpb\x1b[0m | tests.py:11 in test_pb | test\n'
        self.assertEqual(out_file.getvalue(), expected)


if __name__ == '__main__':
    unittest.main()
