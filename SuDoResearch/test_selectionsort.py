import unittest
import selectionsort

class TestGaleShapley(unittest.TestCase):

    def test_coupling(self):

        pref_matrix =  [[1,2,3],
                        [1,2,3],
                        [2,1,3],
                        [3,2,1],
                        [3,1,2],
                        [2,1,3]]
        self.assertEqual(selectionsort.coupling(3, pref_matrix), [3,1,2])

        pref_matrix = [[1,2],
                       [2,1],
                       [2,1],
                       [1,2]]
        self.assertEqual(selectionsort.coupling(2, pref_matrix), [1,2])

        pref_matrix = [[5,1,2,3,4],
                       [1,2,5,3,4],
                       [1,5,2,3,4],
                       [2,5,3,1,4],
                       [3,2,5,1,4],
                       [5,2,3,4,1],
                       [5,1,3,4,2],
                       [2,1,5,3,4],
                       [2,1,5,3,4],
                       [5,1,2,4,3]]
        self.assertEqual(selectionsort.coupling(5, pref_matrix), [5, 1, 2, 4, 3])