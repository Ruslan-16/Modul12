import unittest
from runner12 import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", 10)
        self.runner_andrei = Runner("Андрей", 9)
        self.runner_nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            readable_result = {place: str(runner) for place, runner in result.items()}
            print(readable_result)

    def test_race_usain_and_nick(self):
        # Турнир с Усэйном и Ником
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertTrue(results[max(results.keys())] == self.runner_nick)

    def test_race_andrei_and_nick(self):
        # Турнир с Андреем и Ником
        tournament = Tournament(90, self.runner_andrei, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertTrue(results[max(results.keys())] == self.runner_nick)

    def test_race_usain_andrei_and_nick(self):
        # Турнир с Усэйном, Андреем и Ником
        tournament = Tournament(90, self.runner_usain, self.runner_andrei, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results[3] = results
        self.assertTrue(results[max(results.keys())] == self.runner_nick)


# Запуск тестов
if __name__ == "__main__":
    unittest.main()
