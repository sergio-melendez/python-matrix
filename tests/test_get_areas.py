from index import get_areas
import unittest


class GetAreasTest(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(get_areas([[1, 0, 1], [0, 1, 0]]), 3)
        self.assertEqual(get_areas([[1, 0, 1], [1, 1, 0]]), 2)
        self.assertEqual(get_areas([[1, 1, 1, 0], [0, 1, 0, 0]]), 1)
