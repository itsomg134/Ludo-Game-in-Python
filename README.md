#  Ludo Game in Python

A colorful and interactive Ludo game built with Python and Tkinter. This classic board game supports 4 players with a graphical interface and implements core Ludo mechanics.

<img width="1920" height="1080" alt="Screenshot (15)" src="https://github.com/user-attachments/assets/c7d5147b-7458-4584-9d5e-b54aa7b2706c" />

##  Features

- **4 Players**: Red, Green, Yellow, and Blue
- **Interactive GUI**: Built with Tkinter for a user-friendly experience
- **Dice Rolling**: Random dice rolls with visual feedback
- **Token Movement**: Click-to-move token mechanics
- **Game Rules**:
  - Need a 6 to bring tokens out of home
  - Extra turn on rolling a 6
  - Token capture system
  - Safe spots protection
  - Win condition (all tokens reach home)

##  Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually comes with Python)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ludo-game-python.git
cd ludo-game-python
```

2. Run the game:
```bash
python ludo_game.py
```

##  How to Play

1. **Start the Game**: Run the script to open the game window
2. **Roll the Dice**: Click the "Roll Dice" button
3. **Move Tokens**: Click on any highlighted token to move it
4. **Bring Out Tokens**: You need a 6 to move a token from home to the start position
5. **Capture Opponents**: Land on an opponent's token (except safe spots) to send it home
6. **Extra Turns**: Rolling a 6 gives you another turn
7. **Win**: Get all 4 of your tokens to the center to win!

##  Game Interface

- **Top Panel**: 
  - Dice display
  - Current player indicator
  - Roll Dice button
  - New Game button
  
- **Game Board**:
  - Colored home areas for each player
  - Path with safe spots
  - Player tokens (numbered 1-4)

##  Project Structure

```
ludo-game-python/
│
├── ludo_game.py          # Main game file
├── README.md             # This file
└── screenshot.png        # Game screenshot
```

##  Technical Implementation

### Key Classes and Methods

- `LudoGame`: Main game class
  - `initialize_tokens()`: Sets up player tokens
  - `draw_board()`: Renders the game board
  - `roll_dice()`: Handles dice rolling logic
  - `move_token()`: Manages token movement
  - `check_capture()`: Handles token capture mechanics
  - `check_win()`: Checks win conditions

### Game State Management

- Player turns
- Token positions (home, path, or finished)
- Dice value tracking
- Safe spot positions

##  Contributing

Contributions are welcome! Here are some ways you can contribute:

-  Report bugs
-  Suggest new features
-  Submit pull requests

### Possible Enhancements

- Complete board layout with all 52 positions
- Sound effects
- AI opponents
- Network multiplayer
- Score tracking
- Animation effects

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Acknowledgments

- Inspired by the classic board game Ludo
- Built with Python and Tkinter
- Special thanks to all contributors

## Contact

Om Gedam

GitHub: [https://github.com/itsomg134](https://github.com/itsomg134)

Email: [omgedam123098@gmail.com](mailto:omgedam123098@gmail.com)

Twitter (X): [https://twitter.com/omgedam](https://twitter.com/omgedam)

LinkedIn: [https://linkedin.com/in/omgedam](https://linkedin.com/in/omgedam)

Portfolio: [https://ogworks.lovable.app](https://ogworks.lovable.app)

##  Future Roadmap

- [ ] Complete board layout with all path positions
- [ ] Add sound effects
- [ ] Implement AI players
- [ ] Add multiplayer support
- [ ] Create mobile version
- [ ] Add animations
- [ ] Include game statistics
