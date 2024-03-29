import pytest

from Quackle import QuackleGame, Player, Move


class TestQuackleGame:
    def test_init(self):
        game = QuackleGame("fixtures/test1.gcg")
        assert type(game) == QuackleGame
        assert game.player1.name == "New_Player_1"
        assert game.player2.name == "Quackle"

        with pytest.raises(Exception) as e:
            game = QuackleGame("fixtures/bad_files/unfinished_game.gcg")

    def test_is_finished_game(self):
        finished_game = "fixtures/test1.gcg"
        unfinished_game = "fixtures/bad_files/unfinished_game.gcg"

        assert QuackleGame.is_finished_game(finished_game)
        assert not QuackleGame.is_finished_game(unfinished_game)

    def test_to_dict(self):
        game = QuackleGame("fixtures/test1.gcg")
        game_dict = game.to_dict()
        assert game_dict["filename"] == "test1.gcg"
        assert game_dict["score_1"] == 520
        assert game_dict["score_2"] == 386
        assert game_dict["bingo_1"] == 4
        assert game_dict["bingo_2"] == 2
        assert game_dict["percent_dif"] == 29.58057395143488


class TestPlayer:
    def test_init(self):
        name = "Player_1"
        player1 = Player(name)
        assert player1.name == name

    def test_score(self):
        game = QuackleGame("fixtures/test2.gcg")
        assert game.player1.score == 409
        assert game.player2.score == 391

    def test_bingo_count(self):
        game = QuackleGame("fixtures/test2.gcg")
        assert game.player1.bingo_count == 3
        assert game.player2.bingo_count == 2


class TestMove:
    def test_init(self):
        line = ">New_Player_1: AEFINUW 9C WIFE +25 25"
        move = Move(line)
        assert move.player == "New_Player_1"
        assert move.rack == "AEFINUW"
        assert move.location == "9C"
        assert move.word == "WIFE"
        assert move.points_earned == 25
        assert move.current_score == 25

        # Test line at the end of game
        line = ">Quackle:  (ACI) +8 543"
        move = Move(line)
        assert move.player == "Quackle"
        assert move.rack == ""
        assert move.location == ""
        assert move.word == "(ACI)"
        assert move.points_earned == 8
        assert move.current_score == 543

        # Test exchanged tiles
        line = ">New_Player_1: EIOOSUU -IOOUU +0 65"
        move = Move(line)
        assert move.player == "New_Player_1"
        assert move.rack == "EIOOSUU"
        assert move.location == ""
        assert move.word == "-IOOUU"
        assert move.points_earned == 0
        assert move.current_score == 65
        assert not move.is_pass

        # Test passes
        line = ">Quackle: V -  +0 254"
        move = Move(line)
        assert move.player == "Quackle"
        assert move.rack == "V"
        assert move.location == "-"
        assert move.word == ""
        assert move.points_earned == 0
        assert move.current_score == 254
        assert move.is_pass

    def test_is_bingo(self):
        game = QuackleGame("fixtures/test1.gcg")
        line = ">Quackle: ?EINRTT H8 .NTeRTIE +74 115"
        move = Move(line)
        assert move.is_bingo

        line = ">New_Player_1: DEGIINS 12C .I +22 348"
        move = Move(line)
        assert not move.is_bingo

    def test_is_final_move(self):
        line = ">New_Player_1:  (G) +4 520"
        move = Move(line)
        assert move.is_final_move

        line = ">New_Player_1: DEGIINS 12C .I +22 348"
        move = Move(line)
        assert not move.is_final_move

    def test_no_location(self):
        line = ">New_Player_1: DEGIINS 12C .I +22 348"
        move = Move(line)
        assert not move.no_location

        line = ">New_Player_1: EIOOSUU -IOOUU +0 65"
        move = Move(line)
        assert move.no_location

    def test_safe_int(self):
        pass


class TestCli:
    def test_clean(self):
        pass

    def test_generate_csvs(self):
        pass
