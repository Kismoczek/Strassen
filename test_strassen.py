import unittest

import numpy as np

from main import strassen


class MyTestCase(unittest.TestCase):
    def test_something(self):


        x1 = np.random.random((4, 4))
        x2 = np.random.random((4, 4))
        # sprawdza czy błąd jest w akceptowalnej granicy
        self.assertTrue(np.allclose(strassen(x1, x2), x1.dot(x2), rtol=1e-05, atol=1e-08, equal_nan=False))





if __name__ == '__main__':
    unittest.main()
