import runner
import runner_and_tournament
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,'тест не выполнялся')
    def test_walk(self):
        begun1 = runner.Runner("tom")
        for i in range(10):
            begun1.walk()
        self.assertEqual(begun1.distance,50,'test walk')

    @unittest.skipIf(is_frozen,'тест не выполнялся')
    def test_run(self):
        begun2 = runner.Runner("jerry")
        for i in range(10):
            begun2.run()
        self.assertEqual(begun2.distance,100,'test run')
    @unittest.skipIf(is_frozen,'тест не выполнялся')
    def test_challenge(self):
        begun3 = runner.Runner("biba")
        begun4 = runner.Runner("boba")
        for i in range(10):
            begun3.run()
            begun4.walk()
        self.assertNotEqual(begun3.distance,begun4.distance,'test chalenge')

class TournamentTest(unittest.TestCase):
    is_frozen = True
    def setUp(self):
        self.usain = runner_and_tournament.Runner('usain',10)
        self.andrew = runner_and_tournament.Runner('andrew',9)
        self.nick = runner_and_tournament.Runner('nick',3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen,'тест не выполнялся')
    def test_tournament_1(self):
        race1 = runner_and_tournament.Tournament(90,self.nick,self.usain)
        results = race1.start()
        self.all_results['race1'] = results
        self.assertTrue(self.nick==results[2],f'{results}')

    @unittest.skipIf(is_frozen,'тест не выполнялся')
    def test_tournament_2(self):
        race2 = runner_and_tournament.Tournament(90,self.andrew,self.nick)
        results = race2.start()
        self.all_results['race2'] = results
        self.assertTrue(self.nick==results[2],f'{results}')

    @unittest.skipIf(is_frozen,'тест не выполнялся')
    def test_tournament_3(self):
        race3 = runner_and_tournament.Tournament(90,self.usain,self.andrew,self.nick)
        results = race3.start()
        self.all_results['race3']=results
        self.assertTrue(self.nick==results[3])

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(f'{i}{cls.all_results[i]}')