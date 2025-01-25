import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import random

# Initialize scores and game history
player1_score = 0
player2_score = 0
history = []
max_score = 5  # End the game when a player reaches this score
dark_mode = False
difficulty = "Easy"  # Default difficulty level
sound_enabled = True  # Sound is enabled by default
animations_enabled = True  # Animations are enabled by default

# Function to decide the winner
def decide_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a tie!"
    if (choice1 == "rock" and choice2 == "scissor") or \
       (choice1 == "paper" and choice2 == "rock") or \
       (choice1 == "scissor" and choice2 == "paper") or \
       (choice1 == "rock" and choice2 == "lizard") or \
       (choice1 == "lizard" and choice2 == "paper") or \
       (choice1 == "paper" and choice2 == "spock") or \
       (choice1 == "spock" and choice2 == "scissor") or \
       (choice1 == "scissor" and choice2 == "lizard") or \
       (choice1 == "lizard" and choice2 == "spock") or \
       (choice1 == "spock" and choice2 == "rock"):
        return "Player 1 wins!"
    return "Player 2 wins!"

# Function to update scores
def update_score(winner):
    global player1_score, player2_score

    if winner == "Player 1 wins!":
        player1_score += 1
    elif winner == "Player 2 wins!":
        player2_score += 1

    # Update the score label and the count label
    score_label.config(text=f"Score - Player 1: {player1_score}, Player 2: {player2_score}")
    count_label.config(text=f"Round Count - Player 1: {player1_score} | Player 2: {player2_score}")

    # Check if the game is over
    if player1_score == max_score:
        messagebox.showinfo("Game Over", "Player 1 is the overall winner!")
        reset_game()
    elif player2_score == max_score:
        messagebox.showinfo("Game Over", "Player 2 is the overall winner!")
        reset_game()

# Function to play against another player
def play_with_player():
    global history
    choice1 = player1_choice.get().lower()
    choice2 = player2_choice.get().lower()

    # Validate input
    if choice1 not in ["rock", "paper", "scissor", "lizard", "spock"] or choice2 not in ["rock", "paper", "scissor", "lizard", "spock"]:
        messagebox.showerror("Invalid Input", "Please enter rock, paper, scissor, lizard, or spock.")
        return

    result = decide_winner(choice1, choice2)
    update_score(result)

    # Add round to history
    history.append(f"Player 1: {choice1}, Player 2: {choice2}, Result: {result}")
    history_label.config(text="\n".join(history[-5:]))  # Show the last 5 rounds

    # Show result
    messagebox.showinfo("Result", f"Player 1: {choice1}\nPlayer 2: {choice2}\n\n{result}")

# Function to play against AI with difficulty level
def play_with_ai():
    global history, difficulty, sound_enabled, animations_enabled
    choice1 = player1_choice.get().lower()

    # Generate AI's choice based on difficulty
    if difficulty == "Easy":
        choice2 = random.choice(["rock", "paper", "scissor", "lizard", "spock"])
    elif difficulty == "Medium":
        choice2 = random.choice(["rock", "paper", "scissor"])
    else:
        choice2 = "rock"  # AI plays strategically in hard mode (example)

    # Validate input
    if choice1 not in ["rock", "paper", "scissor", "lizard", "spock"]:
        messagebox.showerror("Invalid Input", "Please enter rock, paper, scissor, lizard, or spock.")
        return

    result = decide_winner(choice1, choice2)
    update_score(result)

    # Add round to history
    history.append(f"Player 1: {choice1}, AI: {choice2}, Result: {result}")
    history_label.config(text="\n".join(history[-5:]))  # Show the last 5 rounds

    # Show result
    messagebox.showinfo("Result", f"Player 1: {choice1}\nAI: {choice2}\n\n{result}")

# Function to reset the game
def reset_game():
    global player1_score, player2_score, history
    player1_score = 0
    player2_score = 0
    history = []
    player1_choice.delete(0, tk.END)
    player2_choice.delete(0, tk.END)
    score_label.config(text=f"Score - Player 1: {player1_score}, Player 2: {player2_score}")
    history_label.config(text="")
    count_label.config(text="Round Count - Player 1: 0 | Player 2: 0")

# Function to open settings window
def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")

    # Sound Control
    sound_label = tk.Label(settings_window, text="Enable Sound:", font=("Arial", 12))
    sound_label.pack()
    sound_check = tk.Checkbutton(settings_window, text="Enabled", variable=sound_enabled)
    sound_check.pack()

    # Animations Control
    animations_label = tk.Label(settings_window, text="Enable Animations:", font=("Arial", 12))
    animations_label.pack()
    animations_check = tk.Checkbutton(settings_window, text="Enabled", variable=animations_enabled)
    animations_check.pack()

    # Difficulty Dropdown
    difficulty_label = tk.Label(settings_window, text="Select Difficulty:", font=("Arial", 12))
    difficulty_label.pack()
    difficulty_dropdown = ttk.Combobox(settings_window, values=["Easy", "Medium", "Hard"], font=("Arial", 12))
    difficulty_dropdown.set(difficulty)
    difficulty_dropdown.pack()

    # Close Settings Button
    close_button = tk.Button(settings_window, text="Close", command=settings_window.destroy)
    close_button.pack()

# Function to show the game mode selection popup
def game_mode_selection():
    mode = simpledialog.askstring("Game Mode", "Select game mode: 'Player' or 'AI'").lower()
    if mode == "player":
        play_button.pack(pady=10)
        player2_choice.pack(pady=5)
        ai_button.pack_forget()  # Remove AI button
    elif mode == "ai":
        ai_button.pack(pady=10)
        play_button.pack_forget()  # Remove Player vs Player button
    else:
        messagebox.showerror("Invalid Selection", "Please choose either 'Player' or 'AI'.")
        game_mode_selection()  # Retry selection

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors, Lizard, Spock Game")

# Set a dark background for a modern feel
root.config(bg="#2E3B4E")

# Add the game title with a modern font and color
title_label = tk.Label(root, text="Rock, Paper, Scissors, Lizard, Spock Game", font=("Arial", 20, "bold"), fg="#FFFFFF", bg="#2E3B4E")
title_label.pack(pady=10)

# Player 1 label and input with a sleek modern design
player1_label = tk.Label(root, text="Player 1 (Enter Choice):", font=("Arial", 12), fg="#FFFFFF", bg="#2E3B4E")
player1_label.pack()
player1_choice = tk.Entry(root, font=("Arial", 12), width=20)
player1_choice.pack(pady=5)

# Player 2 label and input (moved below Player 1 input)
player2_label = tk.Label(root, text="Player 2 (Enter Choice):", font=("Arial", 12), fg="#FFFFFF", bg="#2E3B4E")
player2_label.pack()
player2_choice = tk.Entry(root, font=("Arial", 12), width=20)
player2_choice.pack(pady=5)

# Score label with bold and modern design
score_label = tk.Label(root, text=f"Score - Player 1: {player1_score}, Player 2: {player2_score}", font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#2E3B4E")
score_label.pack(pady=5)

# Round count label for showing the score as a counter
count_label = tk.Label(root, text="Round Count - Player 1: 0 | Player 2: 0", font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#2E3B4E")
count_label.pack(pady=5)

# Game History label
history_label = tk.Label(root, text="", font=("Arial", 10), fg="#FFFFFF", bg="#2E3B4E")
history_label.pack(pady=5)

# Play against player button with modern design and hover effect
play_button = tk.Button(root, text="Play Against Another Player", command=play_with_player, font=("Arial", 12), bg="#4CAF50", fg="white", relief="flat")
play_button.pack(pady=10)

# Play against AI button with modern design
ai_button = tk.Button(root, text="Play Against AI", command=play_with_ai, font=("Arial", 12), bg="#FF9800", fg="white", relief="flat")

# Settings button with modern design
settings_button = tk.Button(root, text="Settings", command=open_settings, font=("Arial", 12), bg="#2196F3", fg="white", relief="flat")
settings_button.pack(pady=10)

# Show game mode selection on startup
game_mode_selection()

# Start the Tkinter event loop
root.mainloop()
