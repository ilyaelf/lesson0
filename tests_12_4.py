import logging
import unittest
import rt_with_exceptions

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,'тест не выполнялся')
    def test_walk(self):
        try:
            begun1 = rt_with_exceptions.Runner("tom",speed=-2)
            for i in range(10):
                begun1.walk()
            self.assertEqual(begun1.distance,50,'test walk')
            logging.info("test_walk ran sucessfully")
        except ValueError:
            logging.warning("wrong speed for runner")

    @unittest.skipIf(is_frozen,'тест не выполнялся')
    def test_run(self):
        try:
            begun2 = rt_with_exceptions.Runner(10,5)
            for i in range(10):
                begun2.run()
            self.assertEqual(begun2.distance,100,'test run')
            logging.info("test_run ran sucsesfully")
        except TypeError:
            logging.warning("wrong 'name' type")
    @unittest.skipIf(is_frozen,'тест не выполнялся')
    def test_challenge(self):
        begun3 = rt_with_exceptions.Runner("biba")
        begun4 = rt_with_exceptions.Runner("boba")
        for i in range(10):
            begun3.run()
            begun4.walk()
        self.assertNotEqual(begun3.distance,begun4.distance,'test chalenge')



logging.basicConfig(level=logging.INFO,filemode="w",filename="runner_tests.log",
                        format="%(asctime)s|%(funcName)s|%(levelname)s|%(message)s|%(pathname)s")

