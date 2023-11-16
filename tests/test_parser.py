from index import parse_args
import unittest


class ParserTest(unittest.TestCase):

    def test_missing_argument(self):
        self.assertRaises(SystemExit, parse_args, [])

    def test_required_argument(self):
        parser = parse_args(['foo'])
        self.assertEqual(parser.matrix, 'foo')
