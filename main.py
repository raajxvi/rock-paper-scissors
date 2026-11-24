
import random
import tkinter as tk
from tkinter import messagebox

# ---------------- GAME SETTINGS ----------------

CHOICES = ["Rock", "Paper", "Scissors"]

EMOJIS = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌️"
}

# Pastel colors
COLORS = {
    "Rock": "#BFDDF5",
    "Paper": "#FFE0B5",
    "Scissors": "#F7C6DE"
}

BG_COLOR = "#F7F3FC"
HEADER_COLOR = "#DCD2F0"
TEXT_COLOR = "#514766"
SCORE_COLOR = "#E5F3EC"
RESULT_COLOR = "#FFF8E8"
BUTTON_COLOR = "#D8C9F0"

player_score = 0
computer_score = 0
draws = 0
match_finished = False


# ---------------- GAME LOGIC ----------------

def play(choice):
    global player_score, computer_score, draws
    global match_finished

    if match_finished:
        return

    # Computer chooses randomly
    computer = random.choice(CHOICES)

    # Determine winner
    if choice == computer:
        result = "It's a draw!"
        draws += 1

    elif (
        (choice == "Rock" and computer == "Scissors")
        or (choice == "Paper" and computer == "Rock")
        or (choice == "Scissors" and computer == "Paper")
    ):
        result = "You win this round!"
        player_score += 1

    else:
        result = "Computer wins this round!"
        computer_score += 1

    # Reveal both choices immediately
    player_move.config(
        text=f"You chose\n{EMOJIS[choice]} {choice}"
    )

    computer_move.config(
        text=f"Computer chose\n{EMOJIS[computer]} {computer}"
    )

    result_label.config(
        text=result,
        bg=BG_COLOR,
        fg=TEXT_COLOR
    )

    # Update scoreboard
    score_label.config(
        text=(
            f"YOU: {player_score}     "
            f"COMPUTER: {computer_score}     "
            f"DRAWS: {draws}"
        )
    )

    # First to 5 points wins
    if player_score >= 5 or computer_score >= 5:
        match_finished = True

        winner = (
            "Congratulations! You won the match!"
            if player_score >= 5
            else "Computer won the match!"
        )

        result_label.config(text="MATCH OVER!")

        disable_choices()
        messagebox.showinfo("Match Over", winner)


def disable_choices():
    for button in choice_buttons:
        button.config(state="disabled")


def restart():
    global player_score, computer_score, draws
    global match_finished

    player_score = 0
    computer_score = 0
    draws = 0
    match_finished = False

    score_label.config(
        text="YOU: 0     COMPUTER: 0     DRAWS: 0"
    )

    player_move.config(text="Your choice")
    computer_move.config(text="Computer's choice")

    result_label.config(
        text="Make your choice!",
        bg=BG_COLOR,
        fg=TEXT_COLOR
    )

    for button in choice_buttons:
        button.config(state="normal")


# ---------------- CREATE WINDOW ----------------

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("750x650")
root.configure(bg=BG_COLOR)
root.resizable(False, False)


# ---------------- HEADING ----------------

title = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 25, "bold"),
    bg=HEADER_COLOR,
    fg=TEXT_COLOR,
    pady=18
)
title.pack(fill="x")

subtitle = tk.Label(
    root,
    text="Choose your move! First to 5 points wins.",
    font=("Arial", 13),
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    pady=15
)
subtitle.pack()


# ---------------- SCOREBOARD ----------------

score_label = tk.Label(
    root,
    text="YOU: 0     COMPUTER: 0     DRAWS: 0",
    font=("Arial", 16, "bold"),
    bg=SCORE_COLOR,
    fg=TEXT_COLOR,
    padx=15,
    pady=15
)
score_label.pack(fill="x", padx=35)


# ---------------- CHOICE BUTTONS ----------------

choice_frame = tk.Frame(root, bg=BG_COLOR)
choice_frame.pack(pady=30)

choice_buttons = []

for choice in CHOICES:
    button = tk.Button(
        choice_frame,
        text=f"{EMOJIS[choice]}\n\n{choice}",
        font=("Arial", 22, "bold"),
        bg=COLORS[choice],
        fg=TEXT_COLOR,
        activebackground=HEADER_COLOR,
        activeforeground=TEXT_COLOR,
        width=10,
        height=4,
        relief="raised",
        bd=3,
        cursor="hand2",
        command=lambda c=choice: play(c)
    )

    button.pack(side="left", padx=10)
    choice_buttons.append(button)


# ---------------- ROUND RESULT ----------------

result_label = tk.Label(
    root,
    text="Make your choice!",
    font=("Arial", 24, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    pady=12
)
result_label.pack()


# ---------------- DISPLAY BOTH MOVES ----------------

moves_frame = tk.Frame(root, bg=BG_COLOR)
moves_frame.pack(pady=10)

player_move = tk.Label(
    moves_frame,
    text="Your choice",
    font=("Arial", 14, "bold"),
    bg=RESULT_COLOR,
    fg=TEXT_COLOR,
    width=22,
    height=3
)
player_move.pack(side="left", padx=10)

computer_move = tk.Label(
    moves_frame,
    text="Computer's choice",
    font=("Arial", 14, "bold"),
    bg=RESULT_COLOR,
    fg=TEXT_COLOR,
    width=22,
    height=3
)
computer_move.pack(side="left", padx=10)


# ---------------- RESTART BUTTON ----------------

restart_button = tk.Button(
    root,
    text="↻  Restart Game",
    font=("Arial", 14, "bold"),
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    activebackground="#C8B6E8",
    activeforeground=TEXT_COLOR,
    cursor="hand2",
    command=restart,
    padx=20,
    pady=10,
    relief="flat"
)
restart_button.pack(pady=20)


# ---------------- START GAME ----------------

root.mainloop()
