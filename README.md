# Tug of War - Pygame Edition (Lab 4: Vibe Coding)

A 2-player local multiplayer Tug of War game built with Python and Pygame. This repository was debugged, modularized, and enhanced using **Vibe Coding** techniques as part of **Lab 4: Vibe Coding**.

---

## 📌 Project Overview

The application simulates a two-player Tug of War match. Players compete in real-time by rapidly pressing assigned keys to pull the center knot across visual winning threshold markers before the countdown timer expires.

### Key Features & Bug Fixes
- **Event Handling & Physics Fix**: Corrected player key event listeners and rope positioning logic.
- **Boundary Clamping**: Clamped the central knot marker position to remain within visible screen dimensions.
- **Countdown Timer (30s)**: Implemented a 30-second match timer displayed in the main HUD header.
- **Tie-Breaker Logic**: Evaluates knot positioning when time expires to declare the player closest to their boundary as the winner.
- **Visual Thresholds & HUD**: Added clear win boundary lines (Red for Player 1, Blue for Player 2) and real-time status text.
- **Instant Match Reset**: Added key event listener (`R`) to reset the timer, rope position, and match outcome without exiting the game.

---

## 🕹️ Controls

| Action | Control Key | Description |
| :--- | :---: | :--- |
| **Player 1 Pull** | `A` | Pulls the knot marker to the **Left** |
| **Player 2 Pull** | `L` | Pulls the knot marker to the **Right** |
| **Restart Match** | `R` | Resets rope position, timer, and winner state |

---

## 📁 Repository Structure

56_tug_of_war/
├── game/
│   ├── game_engine.py   # Core game loop, rendering engine, timer, and event handling
│   ├── player.py        # Player entity definition and keypress logic
│   └── rope.py          # Rope state, pull steps, boundary clamping, and win validation
├── main.py              # Main execution entry point
└── README.md            # Repository documentation


### Lab 4 Required Submission Hierarchy (`/Lab-4`)
Lab-4/
├── 56_tug_of_war/      # Updated project source files
├── video_before.mp4    # 10-second screen recording of broken/initial code execution
├── video_after.mp4     # 10-second screen recording of fixed, fully working game
└── chat_history.pdf    # Exported prompt history from Vibe Coding AI sessions


---

## 💻 Technical Setup & Requirements

### Dependencies
- **Python**: Version 3.8+
- **Pygame**: Version 2.0+

### Installation & Execution

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/ChigilarNishanth/56_tug_of_war.git](https://github.com/ChigilarNishanth/56_tug_of_war.git)
   cd 56_tug_of_war
Install Required Packages:

Bash
pip install pygame
Run the Application:

Bash
python main.py
🎯 Match Rules
Boundary Victory: The first player to pull the knot past their colored threshold line (Red on the left, Blue on the right) wins immediately.

Time Limit: Each match runs for 30 seconds.

Timeout Rule: If the timer hits 0s without either threshold being crossed, the player who pulled the knot closest to their side is declared winner. If the knot is at exact center, the match ends in a Tie.
