# Tug of War - Pygame Edition

A two-player local multiplayer Tug of War game built with **Python** and **Pygame**.

This project was debugged, modularized, and enhanced using **Vibe Coding** techniques as part of **Lab 4: Vibe Coding**.

---

## Project Overview

The game simulates a real-time Tug of War match between two players. Each player repeatedly presses their assigned key to pull the center knot toward their side.

The match ends when:

- A player pulls the knot past their winning boundary.
- The 30-second countdown timer reaches zero.
- The player closest to their side wins when time expires.
- The knot remains exactly in the center when time expires, resulting in a tie.

---

## Features

- Two-player local multiplayer gameplay.
- Real-time keyboard-based controls.
- 30-second countdown timer.
- Visual rope and center knot.
- Red and blue winning boundary markers.
- Automatic winner detection.
- Tie-breaker logic when the timer expires.
- Boundary clamping to keep the knot inside the game area.
- Instant match reset without closing the application.
- Modular project structure.
- Informative HUD displaying the timer and match status.

---

## Controls

| Player / Action | Key | Description |
|---|:---:|---|
| Player 1 Pull | `A` | Pulls the knot toward the left |
| Player 2 Pull | `L` | Pulls the knot toward the right |
| Restart Match | `R` | Resets the rope, timer, and match state |
| Quit Game | Close Window | Closes the Pygame window |

> Players should press their assigned keys repeatedly to pull the knot toward their side.

---

## Match Rules

### Boundary Victory

The first player to pull the center knot beyond their colored boundary wins immediately.

- Player 1 wins when the knot crosses the red boundary on the left.
- Player 2 wins when the knot crosses the blue boundary on the right.

### Time Limit

Each match lasts for **30 seconds**.

### Timeout Rule

If the timer reaches zero before either player crosses a boundary:

- The player whose side is closest to the knot wins.
- If the knot is exactly at the center, the result is declared a **Tie**.

### Restarting a Match

Press `R` at any time to reset:

- The knot position.
- The countdown timer.
- The winner state.
- The match status.

---

## Project Structure

```text
56_tug_of_war/
├── game/
│   ├── game_engine.py
│   ├── player.py
│   └── rope.py
├── main.py
└── README.md
```

### File Descriptions

| File | Description |
|---|---|
| `main.py` | Application entry point that starts the game |
| `game/game_engine.py` | Contains the main game loop, rendering logic, timer, HUD, and event handling |
| `game/player.py` | Defines player behavior and keyboard input handling |
| `game/rope.py` | Manages rope movement, knot position, boundary clamping, and win validation |
| `README.md` | Project documentation |

---

## Lab 4 Submission Structure

The completed Lab 4 submission should use the following structure:

```text
Lab-4/
├── 56_tug_of_war/
│   ├── game/
│   │   ├── game_engine.py
│   │   ├── player.py
│   │   └── rope.py
│   ├── main.py
│   └── README.md
├── video_before.mp4
├── video_after.mp4
└── chat_history.pdf
```

### Required Submission Files

| File | Description |
|---|---|
| `56_tug_of_war/` | Updated and modularized project source code |
| `video_before.mp4` | Approximately 10-second recording showing the original or broken game |
| `video_after.mp4` | Approximately 10-second recording showing the corrected and working game |
| `chat_history.pdf` | Exported prompt history from the Vibe Coding AI sessions |

---

## Technical Requirements

- Python 3.8 or newer
- Pygame 2.0 or newer
- Keyboard and display capable of running a Pygame application

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ChigilarNishanth/56_tug_of_war.git
cd 56_tug_of_war
```

### 2. Create a Virtual Environment

Creating a virtual environment is recommended:

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS and Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install Pygame using `pip`:

```bash
pip install pygame
```

If your system uses `python3`, use:

```bash
pip3 install pygame
```

---

## Running the Game

From the project root directory, run:

```bash
python main.py
```

On systems where Python 3 is accessed using `python3`, run:

```bash
python3 main.py
```

A Pygame window should open and display the Tug of War game.

---

## How to Play

1. Start the game using the command shown above.
2. Player 1 presses `A` repeatedly to pull the knot left.
3. Player 2 presses `L` repeatedly to pull the knot right.
4. Watch the countdown timer in the HUD.
5. Pull the knot across your colored boundary to win.
6. Press `R` to restart the match at any time.

---

## Bug Fixes and Improvements

The project was improved through several debugging and enhancement steps:

### Event Handling

Corrected keyboard event handling so that player inputs are detected reliably through Pygame events.

### Rope Physics

Improved the rope movement logic so that each player's key press moves the center knot in the correct direction.

### Boundary Clamping

The knot position is clamped to the playable area so that it cannot move outside the visible game window.

### Countdown Timer

Added a 30-second countdown timer that is displayed in the main HUD.

### Winner Detection

Added immediate winner detection when the knot crosses either player's boundary line.

### Timeout Tie-Breaker

Added logic to determine the winner based on the knot's final position when the timer reaches zero.

### Tie Detection

If the knot is exactly centered when time expires, the game declares the result as a tie.

### Match Reset

Added the `R` key to reset the game without restarting the application.

### HUD and Visual Feedback

Added clear boundary lines, player indicators, timer information, and match status text.

---

## Troubleshooting

### Pygame Is Not Installed

If you receive an error such as:

```text
ModuleNotFoundError: No module named 'pygame'
```

Install Pygame with:

```bash
pip install pygame
```

### Python Command Is Not Found

Try using:

```bash
python3 main.py
```

You may also need to install Python from the official Python website.

### The Game Window Closes Immediately

Run the game from a terminal so that any error messages remain visible:

```bash
python main.py
```

Check that:

- You are in the project root directory.
- The `game` folder exists.
- All required Python files are present.
- Pygame is installed correctly.

### Keyboard Input Does Not Work

Make sure the Pygame window is active and focused before pressing `A`, `L`, or `R`.

---

## Educational Purpose

This project demonstrates:

- Python application structure.
- Object-oriented programming concepts.
- Game loops and frame updates.
- Event handling with Pygame.
- Keyboard input processing.
- Basic game physics.
- Collision and boundary detection.
- Timers and game-state management.
- Modular code organization.
- Debugging and iterative software improvement using AI-assisted development.

---

## Future Improvements

Possible future enhancements include:

- Sound effects for pulling and winning.
- Background music.
- Player names and customizable controls.
- Difficulty levels.
- Computer-controlled opponents.
- Animated rope movement.
- Improved graphics and player sprites.
- A score system across multiple rounds.
- Pause and resume functionality.
- A main menu and settings screen.
- Online multiplayer support.

---

## License

This project is intended for educational use as part of **Lab 4: Vibe Coding**.

Unless otherwise specified, all rights are reserved by the repository owner.

---

## Author

**Chigilar Nishanth**

GitHub Repository:  
https://github.com/ChigilarNishanth/56_tug_of_war
