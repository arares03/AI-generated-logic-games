# Prover9 Logical Puzzle Game
![AI-story-generator](https://github.com/user-attachments/assets/fdc100ca-9413-4674-b37c-45fe362e6c6a)
## Overview
The **Prover9 Logical Puzzle Game** is an interactive project that combines **logical reasoning, storytelling, and problem-solving**. Players are presented with a narrative containing logical statements and must determine whether a given goal is achievable based on the logic provided.

## Features
- **Logical Reasoning Game:** Uses **Prover9** for automated theorem proving.
- **AI Story Generation:** Generates dynamic stories based on logical statements.
- **Graphical User Interface (GUI):** Built with **Tkinter** for an interactive experience.
- **Customizable Challenges:** Players can test their logical skills by verifying if a goal can be achieved.
- **Python-Based Logic Processing:** Uses **SymPy** for logic handling and validation.

## Technologies Used
- **Python** - Main programming language
- **Tkinter** - GUI framework
- **Prover9** - Automated theorem prover
- **SymPy** - Logic generation and verification
- **Google Generative AI** - Story generation from logical premises

## System Architecture
### Components
- **Prover9:** Validates whether a logical goal follows from a given set of statements.
- **entry.py:** Main script that initializes the GUI and handles game logic.
- **gen.py:** Generates logical propositions and determines their validity.
- **Tkinter Interface:** Provides user interaction with the game.
- **Google Generative AI:** Enhances storytelling by creating logical narratives.

## How It Works
1. **User Input:** Players select a story genre.
2. **Logic Generation:** The system generates a set of logical statements and a goal.
3. **Story Creation:** The AI generates a story incorporating the logical constraints.
4. **Validation with Prover9:** The player decides if the goal is achievable.
5. **Game Outcome:** The system verifies the answer using Prover9.

## Installation

### Prerequisites
- **Python 3.x**
- **Prover9 Theorem Prover** (Ensure it is installed and accessible)
- **Tkinter** (Built into Python but may require installation on some systems)
- **Google Generative AI API Key**

### Setup
```sh
git clone https://github.com/your-repo/prover9-logical-puzzle-game.git
cd prover9-logical-puzzle-game
pip install -r requirements.txt
```

### Running the Game
```sh
python entry.py
```

## User Interface
- **Genre Input:** Select a genre for the story.
- **Generate Story:** AI generates a narrative based on logical statements.
- **Possible / Not Possible:** Players determine if the goal is achievable.
- **Results:** The system verifies the player's decision using Prover9.

