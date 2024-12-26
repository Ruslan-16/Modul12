import unittest

def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.__class__.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        return method(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_run(self):
        self.assertEqual(1 + 1, 2)

    @skip_if_frozen
    def test_walk(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_challenge(self):
        self.assertFalse(False)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertEqual(2 * 2, 4)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertNotEqual(2 + 2, 5)

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertIn(3, [1, 2, 3])
