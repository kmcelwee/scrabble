from QuackleGame import QuackleGame

class TestQuackleGame:
    def test_init(self):
        game = QuackleGame('fixtures/test1.gcg')
        assert type(game) == QuackleGame