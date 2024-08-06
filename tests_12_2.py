import unittest
import runner_and_tournament

class TournamentTest(unittest.TestCase):

    def setUp(self):
        self.usain = runner_and_tournament.Runner('usain',10)
        self.andrew = runner_and_tournament.Runner('andrew',9)
        self.nick = runner_and_tournament.Runner('nick',3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def test_tournament_1(self):
        race1 = runner_and_tournament.Tournament(90,self.usain,self.nick)
        results = race1.start()
        self.all_results['race1'] = results
        self.assertTrue(self.nick==results[2],f'{results}')

    def test_tournament_2(self):
        race2 = runner_and_tournament.Tournament(90,self.andrew,self.nick)
        results = race2.start()
        self.all_results['race2'] = results
        self.assertTrue(self.nick==results[2],f'{results}')

    def test_tournament_3(self):
        race3 = runner_and_tournament.Tournament(90,self.usain,self.andrew,self.nick)
        results = race3.start()
        self.all_results['race3']=results
        self.assertTrue(self.nick==results[3])

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(f'{i}{cls.all_results[i]}')




