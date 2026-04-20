# Python Hangman Logic

## Overview
This project is a CLI-based implementation of the classic Hangman game. It focuses on managing complex game states, including life-tracking, difficulty-based parameter adjustment, and real-time string manipulation to update user progress.

## Technical Stack
- Language: Python 3.x
- Core Concepts:
    - State-based game loops (While/Not logic)
    - List manipulation for string reconstruction
    - Conditional difficulty scaling (Easy, Medium, Hard)
    - Input normalization and validation

## Key Features
- Difficulty Modes: The system adjusts the 'lives' variable based on user selection (Easy: 6, Medium: 4, Hard: 1), directly impacting the game's win-condition threshold.
- Dynamic Feedback: Utilizes placeholder lists to visualize the word length and correctly guessed characters, providing immediate visual feedback after each iteration.
- Game-State Management: Tracks the completion of the word and the depletion of lives to determine the final output (Win/Loss) and terminate the execution loop safely.

## How To Run
1. Clone the repository.
2. Ensure Python 3 is installed.
3. Run the script:
   python hangman.py
4. Select your difficulty and enter letters when prompted.
