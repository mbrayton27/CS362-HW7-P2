import unittest
import main1

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(main1.print_count(400), 'That year is a leap year')

if __name__ == '__main__':
    unittest.main()
