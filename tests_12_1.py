import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        begun1 = runner.Runner("tom")
        for i in range(10):
            begun1.walk()
        self.assertEqual(begun1.distance,50)
    def test_run(self):
        begun2 = runner.Runner("jerry")
        for i in range(10):
            begun2.run()
        self.assertEqual(begun2.distance,100)
    def test_challenge(self):
        begun3 = runner.Runner("biba")
        begun4 = runner.Runner("boba")
        for i in range(10):
            begun3.run()
            begun4.walk()
        self.assertNotEqual(begun3.distance,begun4.distance)

