from index import main
import unittest


class MainTest(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(main('1,0,1;0,1,0'), 3)
