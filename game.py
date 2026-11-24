
class RockPaperScissors:
    CHOICES = ("rock", "paper", "scissors")

    WINNING_MOVES = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.draws = 0

    def play_round(self, player, computer):
        if player == computer:
            self.draws += 1
            return "It's a draw!"

        if self.WINNING_MOVES[player] == computer:
            self.player_score += 1
            return "You win this round!"

        self.computer_score += 1
        return "Computer wins this round!"

    def match_over(self):
        return (
            self.player_score >= 5
            or self.computer_score >= 5
        )

    def scoreboard(self):
        return (
            f"You: {self.player_score} | "
            f"Computer: {self.computer_score} | "
            f"Draws: {self.draws}"
        )
