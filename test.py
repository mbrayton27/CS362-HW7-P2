import unittest
import main1

class TestCase1(unittest.TestCase):
    def test1(self):
        self.assertEqual(main1.print_count(400), 'That year is a leap year')

    def test2(self):
        self.assertEqual(main1.print_count(200), 'That year is NOT a leap year')

if __name__ == '__main__':
    unittest.main()
