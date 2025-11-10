from life_game_matrix import getNextMatrix
from unittest import TestCase, main
import numpy
class TestLifeGameMatrix(TestCase):
    def setUp(self):
        self.matrix1 = numpy.array([[0,0,0,0,0],
                                   [0,0,1,0,0],
                                   [0,0,1,0,0],
                                   [0,0,1,0,0],
                                   [0,0,0,0,0]])
        self.matrix2 = numpy.array([[0,0,0,0,0],
                                   [0,0,0,0,0],
                                   [0,1,1,1,0],
                                   [0,0,0,0,0],
                                   [0,0,0,0,0]])
    def test_matrix1_to_matrix2(self):
        self.assertEqual(self.matrix2.all(), getNextMatrix(self.matrix1).all())
    def test_matrix2_to_matrix1(self):
        self.assertEqual(self.matrix1.all(), getNextMatrix(self.matrix2).all())    
if __name__ == '__main__':
    main()        