import unittest
from geom_analysis import say_hi

import unittest

class MyTestClass(unittest.TestCase):

    def test_say_hi(self):
        """Tests teh say_hi function."""
        name = None
        self.assertIsNotNone(say_hi(name))
        self.assertEqual(say_hi(name), "Please introduce yourself...")
        name = 3
        self.assertEqual(say_hi(name), f"Hey {name}! It's so nice meeting you!")
        name = "George"
        self.assertEqual(say_hi(name), f"Hey {name}! It's so nice meeting you!")
    
    def test_say_hi_none(self):
        """Tests teh say_hi function."""
        name = None
        self.assertIsNotNone(say_hi(name))

    def test_say_hi_int(self):
        """Tests teh say_hi function."""
        name = 3
        self.assertEqual(say_hi(name), f"Hey {name}! It's so nice meeting you!")

    def test_say_hi_name(self):
        """Tests teh say_hi function."""
        name = "George"
        self.assertEqual(say_hi(name), f"Hey {name}! It's so nice meeting you!")

if __name__ == "__main__":
    unittest.test_geom_analysis()
