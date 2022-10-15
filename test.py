import unittest
from main import stroka

class Testmain(unittest.TestCase):
    def test_stroka(self):
        self.assertEqual(stroka('привет мир'), 'Привет мир!')

if __name__ == "__main__":
    unittest.main()