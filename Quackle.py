import os


def percent_dif(a, b):
    return abs(a - b) / ((a + b) / 2) * 100


class QuackleGame:
    def __init__(self, path):
        self.path = path
        self.filename = os.path.basename(path)
        self.parse_file()

    def parse_file(self):
        if not self.is_finished_game(self.path):
            raise AttributeError(
                self.path + " is unfinished! This class can't currently parse "
                "unfinished games."
            )

        with open(self.path) as f:
            self.player1 = Player(f.readline().split(" ")[1])
            self.player2 = Player(f.readline().split(" ")[1])
            for line in f.readlines():
                move = Move(line)
                if move.player == self.player1.name:
                    self.player1.add_move(move)
                else:
                    self.player2.add_move(move)

    @classmethod
    def is_finished_game(cls, path):
        with open(path) as f:
            return not any([line.startswith("#rack") for line in f.readlines()])

    def to_dict(self):
        return {
            "filename": self.filename,
            "score_1": self.player1.score,
            "score_2": self.player2.score,
            "bingo_1": self.player1.bingo_count,
            "bingo_2": self.player2.bingo_count,
            "percent_dif": percent_dif(self.player1.score, self.player2.score),
        }


class Player:
    def __init__(self, name):
        self.name = name
        self.moves = []

    def __str__(self):
        return self.name

    def add_move(self, move):
        self.moves.append(move)

    @property
    def score(self):
        if self.moves:
            return self.moves[-1].current_score
        else:
            return None

    @property
    def bingo_count(self):
        return len([move for move in self.moves if move.is_bingo])


class Move:
    def __init__(self, line):
        if not line.startswith(">"):
            raise AttributeError("Move must start with '>'")

        self.line = line

        self.player = line.split(": ")[0].strip(">")
        self.move_content = line.split(": ")[1].split(" ")
        self.rack = self.move_content[0]
        if self.no_location:
            self.location = ""
            self.word = self.move_content[1]
            self.points_earned = self._safe_int(self.move_content[2])
            self.current_score = int(self.move_content[3])
        else:
            self.location = self.move_content[1]
            self.word = self.move_content[2]
            self.points_earned = self._safe_int(self.move_content[3])
            self.current_score = int(self.move_content[4])

    @property
    def is_final_move(self):
        return "(" in self.line

    @property
    def is_bingo(self):
        return len([ch for ch in self.word if ch != "."]) == 7

    @property
    def no_location(self):
        return len(self.move_content) == 4

    @property
    def is_pass(self):
        return self.location == "-"

    def _safe_int(self, s):
        return int(s.replace("+-", "-"))
