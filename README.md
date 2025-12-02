# Water Gun Snake Game
Welcome to Water Gun Snake Game, an exciting turn-based strategy game built entirely in Python using a simple and interactive command-line interface (CLI). This project demonstrates core Python fundamentals like random selection, loops, conditional logic, dictionaries, and competitive game mechanics inspired by the classic "Rock Paper Scissors" gameplay.

## Project Overview
Water Gun Snake Game is a thrilling multiplayer-style game where players compete against the computer in an endless series of rounds. Each round, the player chooses one of three options—water, gun, or snake—while the computer makes its own random selection. The game determines a winner based on predefined rules, creating dynamic competition with unlimited gameplay. This is a modern twist on traditional hand games, bringing strategic depth and entertainment value.

## Features
* Computer AI with random choice selection
* Three distinct game options (Water, Gun, Snake)
* Real-time player vs. computer comparison
* Win/Loss/Draw outcome determination
* Unlimited gameplay rounds (1110 rounds maximum)
* Dictionary-based choice mapping for clean code structure
* Dynamic output displaying both player and computer choices
* Clear win/loss/draw feedback after each round
* Input validation with error handling
* Beginner-friendly, clean, and readable Python code
* Interactive CLI for seamless user experience

## How It Works
* The program initiates an infinite game loop allowing up to 1110 rounds.
* In each round, the computer randomly selects from "water," "gun," or "snake."
* The player enters their choice through the command-line interface.
* Both choices are displayed in a user-friendly format.
* The game engine compares the choices using predefined game rules.
* The outcome (Win, Loss, or Draw) is determined and displayed.
* The round counter increments, and the game continues to the next round.
* Players can choose to exit the game at any time.

## Game Rules
The game follows these strategic rules:

* **Water beats Gun** - Water drowns the gun mechanism
* **Gun beats Snake** - Gun shoots the snake
* **Snake beats Water** - Snake poisons the water
* **Same Choices** - Result in a draw with no winner

## Example Gameplay
```
Enter your choice: w
You choose water
Computer choose gun
You win!

Enter your choice: g
You choose gun
Computer choose s
You loss!

Enter your choice: w
You choose water
Computer choose w
It's draw!
```

## Game Options
* **w** - Water (liquid, defensive)
* **g** - Gun (weapon, offensive)
* **s** - Snake (creature, strategic)

## Concepts Used
* random.choice() for computer AI decision making
* Dictionaries for mapping user input to full names
* Nested conditional logic (if-elif-else) for game rules
* Loops (for) for creating multiple game rounds
* String formatting with f-strings for dynamic output
* User input handling through input() function
* Comparison operators for determining winners
* Game logic implementation and strategy rules
* User interaction through CLI (Command-Line Interface)
* Error handling for invalid inputs
