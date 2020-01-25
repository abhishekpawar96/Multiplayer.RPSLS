class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

    def get_player_move(self, p):
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def both_went(self):
        return self.p1Went and self.p2Went

    def winner(self):

        p1 = self.moves[0].upper()
        p2 = self.moves[1].upper()

        c1 = in_number(p1)
        c2 = in_number(p2)

        # "Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors,
        # scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock,
        # and as it always has, rock crushes scissors."
        win = [[-1, 1, 0, 0, 1], [0, -1, 1, 1, 0], [1, 0, -1, 0, 1], [1, 0, 1, -1, 0], [0, 1, 0, 1, -1]]

        winner = win[c1][c2]
        # if p1 == "ROCK" and p2 == "SCISSOR":
        #     winner = 0
        # elif p1 == "SCISSOR" and p2 == "ROCK":
        #     winner = 1
        # elif p1 == "PAPER" and p2 == "ROCK":
        #     winner = 0
        # elif p1 == "ROCK" and p2 == "PAPER":
        #     winner = 1
        # elif p1 == "SCISSOR" and p2 == "PAPER":
        #     winner = 0
        # elif p1 == "PAPER" and p2 == "SCISSOR":
        #     winner = 1

        return winner

    def reset_went(self):
        self.p1Went = False
        self.p2Went = False


def in_number(c):
    if c == "ROCK":
        return 0
    elif c == "PAPER":
        return 1
    elif c == "SCISSOR":
        return 2
    elif c == "LIZARD":
        return 3
    else:
        return 4
