import unittest
from tests_12_3 import RunnerTest, TournamentTest


def load_tests():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(load_tests())
