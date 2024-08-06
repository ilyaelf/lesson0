import unittest
import tests_12_3

runnersST = unittest.TestSuite()
runnersST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runnersST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

test_runners = unittest.TextTestRunner(verbosity=2)
test_runners.run(runnersST)

