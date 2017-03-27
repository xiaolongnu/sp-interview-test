import unittest
import main

class Test(unittest.TestCase):
    def test_q1(self):
        self.assertEqual(main.q1("hello"), 13)

    def test_q2(self):
        self.assertEqual(main.q2("hello"), '43556')

    def test_q3(self):
        self.assertListEqual(main.q3("23"), ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
    
    def test_q4(self):
        self.assertItemsEqual(main.q4("2355"), ['cell', 'bell'])
        self.assertItemsEqual(main.q4("4663"), ['hone', 'gone', 'good', 'goof', 'home', 'hoof', 'hood'])


if __name__ == "__main__":
    unittest.main()