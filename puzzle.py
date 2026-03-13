import tkinter as tk
from tkinter import messagebox
import random

class LudoGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ludo Game")
        self.root.geometry("800x800")
        
        # Game state - initialize these first
        self.players = ['Red', 'Green', 'Yellow', 'Blue']
        self.current_player = 0
        self.dice_value = 0
        self.selected_token = None
        self.game_started = False
        
        # Colors
        self.colors = {
            'Red': '#FF4444',
            'Green': '#44FF44',
            'Yellow': '#FFFF44',
            'Blue': '#4444FF'
        }
        
        # Board layout (simplified - 52 steps path)
        self.path = self.create_path()
        self.safe_positions = [0, 8, 13, 21, 26, 34, 39, 47]  # Safe spots
        
        # Home positions for each player
        self.home_positions = {
            'Red': [-1, -2, -3, -4],
            'Green': [-5, -6, -7, -8],
            'Yellow': [-9, -10, -11, -12],
            'Blue': [-13, -14, -15, -16]
        }
        
        # Starting positions on main path
        self.start_positions = {
            'Red': 0,
            'Green': 13,
            'Yellow': 26,
            'Blue': 39
        }
        
        # CRITICAL: Initialize tokens BEFORE setting up GUI
        self.tokens = {}
        self.token_positions = {}
        self.initialize_tokens()  # This must come before setup_gui
        
        # Now setup GUI
        self.setup_gui()
        
    def initialize_tokens(self):
        """Initialize all tokens"""
        token_id = 0
        for player in self.players:
            self.tokens[player] = []
            for i in range(4):
                self.tokens[player].append(token_id)
                self.token_positions[token_id] = self.home_positions[player][i]
                token_id += 1
        
        print("Tokens initialized:", self.tokens)  # Debug print
        
    def create_path(self):
        """Create the path positions for the game (52 steps)"""
        path = []
        for i in range(52):
            path.append(i)
        return path
    
    def setup_gui(self):
        """Setup the game GUI"""
        # Control frame
        control_frame = tk.Frame(self.root, bg='gray', height=100)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Dice display
        self.dice_label = tk.Label(control_frame, text="🎲", font=('Arial', 48), bg='white')
        self.dice_label.pack(side=tk.LEFT, padx=20)
        
        # Current player display
        self.player_label = tk.Label(control_frame, text="Current: Red", font=('Arial', 16))
        self.player_label.pack(side=tk.LEFT, padx=20)
        
        # Roll button
        self.roll_button = tk.Button(control_frame, text="Roll Dice", command=self.roll_dice, 
                                     font=('Arial', 14), bg='lightblue')
        self.roll_button.pack(side=tk.LEFT, padx=20)
        
        # Reset button
        reset_button = tk.Button(control_frame, text="New Game", command=self.reset_game,
                                font=('Arial', 14), bg='lightcoral')
        reset_button.pack(side=tk.LEFT, padx=20)
        
        # Game board
        self.board_frame = tk.Frame(self.root, bg='white', width=600, height=600)
        self.board_frame.pack(expand=True, padx=20, pady=20)
        
        self.canvas = tk.Canvas(self.board_frame, width=600, height=600, bg='white')
        self.canvas.pack()
        
        # Draw the board
        self.draw_board()
        
    def draw_board(self):
        """Draw the Ludo board"""
        self.canvas.delete("all")
        
        # Draw the main board (simplified version)
        # Central square
        self.canvas.create_rectangle(200, 200, 400, 400, fill='lightgray')
        
        # Draw colored homes
        # Red home (top-left)
        self.canvas.create_rectangle(50, 50, 200, 200, fill=self.colors['Red'], outline='black')
        self.canvas.create_text(125, 125, text="RED", font=('Arial', 16, 'bold'))
        
        # Green home (top-right)
        self.canvas.create_rectangle(400, 50, 550, 200, fill=self.colors['Green'], outline='black')
        self.canvas.create_text(475, 125, text="GREEN", font=('Arial', 16, 'bold'))
        
        # Yellow home (bottom-left)
        self.canvas.create_rectangle(50, 400, 200, 550, fill=self.colors['Yellow'], outline='black')
        self.canvas.create_text(125, 475, text="YELLOW", font=('Arial', 16, 'bold'))
        
        # Blue home (bottom-right)
        self.canvas.create_rectangle(400, 400, 550, 550, fill=self.colors['Blue'], outline='black')
        self.canvas.create_text(475, 475, text="BLUE", font=('Arial', 16, 'bold'))
        
        # Draw path (simplified)
        # Horizontal paths
        self.canvas.create_rectangle(200, 150, 400, 200, fill='white', outline='black')
        self.canvas.create_rectangle(200, 400, 400, 450, fill='white', outline='black')
        
        # Vertical paths
        self.canvas.create_rectangle(150, 200, 200, 400, fill='white', outline='black')
        self.canvas.create_rectangle(400, 200, 450, 400, fill='white', outline='black')
        
        # Draw safe spots
        safe_spots = [(200, 150), (400, 200), (400, 400), (200, 400), 
                     (150, 200), (200, 200), (400, 200), (400, 400)]
        
        for spot in safe_spots:
            x, y = spot
            self.canvas.create_oval(x-10, y-10, x+10, y+10, fill='white', outline='black')
        
        # Draw tokens
        self.draw_tokens()
        
    def draw_tokens(self):
        """Draw all tokens on the board"""
        # Define token positions in homes
        home_offsets = {
            'Red': [(75, 75), (125, 75), (75, 125), (125, 125)],
            'Green': [(425, 75), (475, 75), (425, 125), (475, 125)],
            'Yellow': [(75, 425), (125, 425), (75, 475), (125, 475)],
            'Blue': [(425, 425), (475, 425), (425, 475), (475, 475)]
        }
        
        # Path positions mapping (simplified)
        path_positions = {
            0: (250, 175), 1: (300, 175), 2: (350, 175), 3: (350, 225),
            4: (350, 275), 5: (350, 325), 6: (350, 375), 7: (300, 375),
            8: (250, 375), 9: (200, 375), 10: (150, 375), 11: (150, 325),
            12: (150, 275), 13: (150, 225), 14: (150, 175), 15: (200, 175),
            # Add more positions as needed
        }
        
        # Draw each token
        for player in self.players:
            if player in self.tokens:  # Safety check
                for i, token_id in enumerate(self.tokens[player]):
                    if token_id in self.token_positions:
                        pos = self.token_positions[token_id]
                        
                        if pos < 0:  # Token in home
                            # Find which home position this is
                            try:
                                home_index = self.home_positions[player].index(pos)
                            except ValueError:
                                home_index = i
                            x, y = home_offsets[player][home_index]
                        elif pos in path_positions:  # Token on path
                            x, y = path_positions[pos]
                        elif pos == 52:  # Token reached home
                            x, y = (300, 300)  # Center of board
                        else:
                            continue
                        
                        # Draw token
                        self.canvas.create_oval(x-15, y-15, x+15, y+15, 
                                              fill=self.colors[player], 
                                              outline='black', width=2,
                                              tags=(f"token_{token_id}",))
                        
                        # Add token number
                        self.canvas.create_text(x, y, text=str(i+1), 
                                              font=('Arial', 10, 'bold'))
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.current_player = 0
        self.game_started = False
        self.selected_token = None
        self.dice_value = 0
        self.initialize_tokens()  # Reinitialize tokens
        self.update_display()
        self.draw_board()
        
    def roll_dice(self):
        """Roll the dice"""
        if not self.game_started:
            self.game_started = True
            
        self.dice_value = random.randint(1, 6)
        self.dice_label.config(text=f"🎲 {self.dice_value}")
        
        # Check if current player can move
        can_move = self.check_moves()
        
        if not can_move:
            messagebox.showinfo("No Moves", f"{self.players[self.current_player]} has no valid moves!")
            self.next_player()
        else:
            self.highlight_tokens()
        
    def check_moves(self):
        """Check if current player has any valid moves"""
        player = self.players[self.current_player]
        
        for token_id in self.tokens[player]:
            pos = self.token_positions[token_id]
            
            # Token in home
            if pos < 0:
                if self.dice_value == 6:
                    return True
            
            # Token on path
            elif pos >= 0 and pos < 52:
                new_pos = pos + self.dice_value
                if new_pos <= 52:  # Haven't reached home yet
                    return True
        
        return False
    
    def move_token(self, token_id):
        """Move a token"""
        player = self.players[self.current_player]
        current_pos = self.token_positions[token_id]
        
        # Token in home
        if current_pos < 0:
            if self.dice_value == 6:
                # Move token to start position
                self.token_positions[token_id] = self.start_positions[player]
                self.after_move()
            else:
                messagebox.showinfo("Invalid Move", "Need a 6 to bring token out!")
                return
        
        # Token on path
        elif current_pos < 52:
            new_pos = current_pos + self.dice_value
            
            if new_pos < 52:
                # Check if position is occupied
                self.token_positions[token_id] = new_pos
                self.check_capture(token_id, new_pos)
                self.after_move()
            elif new_pos == 52:
                # Token reached home
                messagebox.showinfo("Success", f"{player} token reached home!")
                self.token_positions[token_id] = 52  # Home position
                self.after_move()
            else:
                messagebox.showinfo("Invalid Move", "Move exceeds board limit!")
                return
        else:
            messagebox.showinfo("Invalid Move", "Token already at home!")
            return
        
        self.draw_board()
    
    def check_capture(self, moved_token, position):
        """Check if any opponent token is captured"""
        for player in self.players:
            if player != self.players[self.current_player]:
                for token_id in self.tokens[player]:
                    if self.token_positions[token_id] == position and position not in self.safe_positions:
                        # Send token back home
                        try:
                            home_pos = self.home_positions[player][self.tokens[player].index(token_id)]
                            self.token_positions[token_id] = home_pos
                            messagebox.showinfo("Captured!", f"{player}'s token was sent home!")
                        except (ValueError, IndexError):
                            pass
    
    def after_move(self):
        """Actions after a move"""
        if self.check_win():
            return
        
        if self.dice_value != 6:
            self.next_player()
        else:
            messagebox.showinfo("Extra Turn!", f"{self.players[self.current_player]} gets another turn!")
        
        self.selected_token = None
        self.update_display()
    
    def next_player(self):
        """Move to next player"""
        self.current_player = (self.current_player + 1) % 4
        self.dice_value = 0
        self.dice_label.config(text="🎲")
        self.update_display()
    
    def check_win(self):
        """Check if current player has won"""
        player = self.players[self.current_player]
        all_home = all(self.token_positions[token_id] == 52 
                      for token_id in self.tokens[player])
        
        if all_home:
            messagebox.showinfo("Winner!", f"{player} wins the game!")
            if messagebox.askyesno("New Game", "Play again?"):
                self.reset_game()
            return True
        return False
    
    def highlight_tokens(self):
        """Highlight tokens that can be moved"""
        player = self.players[self.current_player]
        
        # First remove all existing bindings
        for p in self.players:
            if p in self.tokens:
                for token_id in self.tokens[p]:
                    self.canvas.tag_unbind(f"token_{token_id}", "<Button-1>")
                    self.canvas.itemconfig(f"token_{token_id}", width=1, outline='black')
        
        # Bind click events to current player's tokens that can move
        for token_id in self.tokens[player]:
            pos = self.token_positions[token_id]
            
            # Check if token can move
            can_move = False
            if pos < 0 and self.dice_value == 6:
                can_move = True
            elif 0 <= pos < 52 and pos + self.dice_value <= 52:
                can_move = True
            
            if can_move:
                self.canvas.tag_bind(f"token_{token_id}", "<Button-1>", 
                                   lambda e, tid=token_id: self.token_click(tid))
                # Highlight token
                self.canvas.itemconfig(f"token_{token_id}", width=3, outline='gold')
    
    def token_click(self, token_id):
        """Handle token click"""
        if self.dice_value == 0:
            messagebox.showinfo("Error", "Roll the dice first!")
            return
        
        self.move_token(token_id)
    
    def update_display(self):
        """Update the display"""
        self.player_label.config(text=f"Current: {self.players[self.current_player]}")
        self.root.update()
    
    def run(self):
        """Run the game"""
        self.root.mainloop()

if __name__ == "__main__":
    game = LudoGame()
    game.run()