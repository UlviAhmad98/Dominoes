import random


class Dominoes:
    snake = list()
    count_dict = dict()
    snake_dict = dict()
    domino_order = list()
    indexes = set()
    # counter = 0
    # counter_player = 0

    def __init__(self):
        self.dominoes = list()
        self.status = None
        self.player = None
        self.computer = None
        self.stock = None
        self.computer_hand = None
        self.player_choice = None
        self.player_hand = None
        self.first_value = None
        self.end_value = None

    def domino_set(self):
        for x in range(0, 7):
            for y in range(0, 7):
                if x == y:
                    self.dominoes.append([x, y])
                if x > y:
                    self.dominoes.append([x, y])

    def pieces(self):
        self.domino_set()
        random.shuffle(self.dominoes)
        self.player = self.dominoes[:7]
        self.computer = self.dominoes[21:28]
        self.stock = self.dominoes[7:21]

    def first_move(self):

        if max(self.player) > max(self.computer):
            self.snake.append(max(self.player))
            self.player.remove(max(self.player))
            self.status = "computer"
        else:
            self.snake.append(max(self.computer))
            self.computer.remove(max(self.computer))
            self.status = "player"

    def player_turn(self):

        print("Status: It's your turn to make a move. Enter your command.")
        while True:
            player_move = input()
            if not player_move.lstrip("-").isdigit():
                print("Invalid input. Please try again.")
            else:
                absolute_value = int(player_move[-1])
                player_move = int(player_move)
                if (player_move > len(self.player)) or (player_move < -len(self.player)):
                    print("Invalid input. Please try again.")
                else:
                    if player_move == 0:
                        if len(self.stock) > 0:
                            self.player.append(self.stock[0])
                            self.stock.remove(self.stock[0])
                            break
                        else:
                            break
                    elif player_move > 0:
                        self.player_choice = self.player[player_move - 1]
                        if self.end_value in self.player_choice:
                            if self.end_value == self.player_choice[1]:
                                self.player_choice[0], self.player_choice[1] = self.player_choice[1], \
                                                                               self.player_choice[0]
                            self.snake.append(self.player_choice)
                            self.player.remove(self.player_choice)
                            break
                        else:
                            print("Illegal move. Please try again.")
                    elif player_move < 0:
                        self.player_hand = self.player[absolute_value - 1]
                        if self.first_value in self.player_hand:
                            if self.first_value == self.player_hand[0]:
                                self.player_hand[0], self.player_hand[1] = self.player_hand[1], self.player_hand[0]
                            self.snake.insert(0, self.player_hand)
                            self.player.remove(self.player_hand)
                            break
                        else:
                            print("Illegal move. Please try again.")
        self.status = "computer"

    def computer_turn(self):
        
        dom_list = list()
        computer_move = input("Status: Computer is about to make a move. Press Enter to continue...")
        if computer_move == "":
            self.count_dict = {x: [digit for lst in (self.computer + self.snake) for digit in lst].count(x) for x in
                               range(0, 7)}
            scores = {tuple(domino): (self.count_dict[domino[0]] + self.count_dict[domino[1]]) for domino in
                      self.computer}
            sorting = lambda x: sorted((x.keys(), x.values())[0])
            descending_list = sorting(scores)
            self.domino_order = [list(x) for x in descending_list]
            for dom in self.domino_order:
                dom_list.append(self.computer.index(dom))
            for wise_move in dom_list:
                if self.end_value in self.computer[wise_move]:
                    if self.end_value == self.computer[wise_move][1]:
                        self.computer[wise_move][0], self.computer[wise_move][1] = self.computer[wise_move][1], \
                                                                                self.computer[wise_move][0]
                    self.snake.append(self.computer[wise_move])
                    if self.end_value == self.computer[wise_move][1]:
                        self.computer[wise_move][0], self.computer[wise_move][1] = self.computer[wise_move][0], \
                                                                                self.computer[wise_move][1]
                    self.computer.remove(self.computer[wise_move])
                    break
                elif self.first_value in self.computer[wise_move]:
                    if self.first_value == self.computer[wise_move][0]:
                        self.computer[wise_move][0], self.computer[wise_move][1] = self.computer[wise_move][1], \
                                                                                self.computer[wise_move][0]
                    self.snake.insert(0, self.computer[wise_move])
                    if self.first_value == self.computer[wise_move][0]:
                        self.computer[wise_move][0], self.computer[wise_move][1] = self.computer[wise_move][0], \
                                                                                self.computer[wise_move][1]
                    self.computer.remove(self.computer[wise_move])
                    break
            else:
                if len(self.stock) > 0:
                    self.computer.append(self.stock[0])
                    self.stock.remove(self.stock[0])
        else:
            print("Invalid input. Please try again.")
        self.status = "player"

    def display(self):

        print("=" * 70)
        print(f"Stock size: {len(self.stock)}")
        print(f"Computer pieces: {len(self.computer)}\n")
        if len(self.snake) > 6:
            print(
                f"{self.snake[0]} {self.snake[1]} {self.snake[2]}...{self.snake[-3]} {self.snake[-2]} {self.snake[-1]}\n")
        else:
            print(f"{''.join(map(str, self.snake))}\n")
        print("Your pieces:")
        for n, piece in enumerate(self.player):
            print(f"{n + 1}: {piece}")
        print()
        self.first_value = self.snake[0][0]
        self.end_value = self.snake[-1][-1]

    def gameplay(self):

        if self.status == "player":
            return self.player_turn()
        elif self.status == "computer":
            return self.computer_turn()

    def draw_state(self):

        value_list = [x for xy in self.snake for x in xy]
        if value_list[0] == value_list[-1]:
            value = value_list.count(value_list[0])
            if value == 8:
                return "Status: The game is over. It's a draw!"

    def game_state(self):

        if (len(self.player) == 0) and len(self.stock) == 0 and (len(self.computer) != 0):
            return "Status: The game is over. You won!"
        elif (len(self.computer) == 0) and len(self.stock) == 0 and (len(self.player) != 0):
            return "Status: The game is over. The computer won!"
        elif self.draw_state():
            return self.draw_state()

    def play(self):

        self.pieces()
        self.first_move()
        self.display()
        while True:
            self.gameplay()
            self.display()
            if self.game_state():
                print(self.game_state())
                break


dominoes = Dominoes()
dominoes.play()
