from index import create_matrix
import unittest


class CreateMatrixTest(unittest.TestCase):

    def test_invalid_input(self):
        self.assertRaises(Exception, create_matrix, 'foo')
        self.assertRaises(Exception, create_matrix, ',')
        self.assertRaises(Exception, create_matrix, '')

    def test_single_matrix(self):
        matrix = create_matrix('1')
        self.assertEqual(matrix, [[1]])

    def test_correct_matrix(self):
        matrix = create_matrix('1,1;0,1')
        self.assertEqual(matrix, [[1, 1], [0, 1]])
