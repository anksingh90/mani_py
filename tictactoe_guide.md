# Program 12: Tic-Tac-Toe with AI - Complete Guide

## Game Overview
Classic 3×3 grid game where user plays 'X' and system plays 'O'. First to get 3 in a row (horizontal, vertical, diagonal) wins.

---

## Data Structures Needed

### Board Representation (List)
- List of 9 positions representing the 3×3 grid
- Positions 0-8 map to grid locations
- Grid layout:
  ```
  0 | 1 | 2
  3 | 4 | 5
  6 | 7 | 8
  ```
- Empty positions marked with space ' '
- User moves marked with 'X'
- System moves marked with 'O'

### Player Symbols Dictionary
- Stores which symbol belongs to which player
- Keys: 'user', 'system'
- Values: 'X', 'O'

### Game Statistics Dictionary
Tracks:
- User wins count
- System wins count
- Draws count
- Total games played
- Current win streak

### Winning Combinations (List of Lists)
8 possible winning patterns:
- 3 rows: [0,1,2], [3,4,5], [6,7,8]
- 3 columns: [0,3,6], [1,4,7], [2,5,8]
- 2 diagonals: [0,4,8], [2,4,6]

### AI Difficulty Settings Dictionary
- Difficulty level: 'easy', 'medium', 'hard'
- First move preference: user or system goes first

### Move History List
- Stores all moves made during the game
- Each entry contains: player, position, move number

---

## Main Program Structure

### 1. Main Menu Function
**Purpose:** Display options and navigate to different modes

**Sub-parts:**
- Display game title and ASCII art banner
- Show current win/loss record from statistics
- Display menu options:
  1. Play Game
  2. View Statistics
  3. Settings
  4. How to Play
  0. Exit
- Get user choice with input validation
- Call appropriate function based on choice
- Loop until user chooses to exit

---

### 2. Play Game Function
**Purpose:** Main game loop for single match

**Sub-parts:**

**a) Initialize Game**
- Reset board to all empty spaces
- Clear move history list
- Decide who goes first based on settings
- Display starting message

**b) Display Board**
- Show current board state with position numbers
- Include row/column dividers for clarity
- Show which positions are taken by X or O
- Option to show position helper guide

**c) Game Loop** (runs until win or draw)

**User's Turn:**
- Display current board state
- Ask for position input (0-8)
- Validate position:
  * Check if input is numeric
  * Check if position is 0-8
  * Check if position is empty
- Place 'X' on selected position
- Add move to history
- Check for win condition
- Check for draw condition
- If game continues, switch to system turn

**System's Turn:**
- Call AI function to determine move
- Place 'O' on chosen position
- Display message: "System chose position X"
- Add move to history
- Check for win condition
- Check for draw condition
- If game continues, switch to user turn

**d) End Game**
- Display final board state
- Announce result (User Win / System Win / Draw)
- Update statistics dictionary
- Increment appropriate counters
- Ask user: "Play again? (Y/N)"
- If Yes: restart game
- If No: return to main menu

---

### 3. AI Move Function (Multiple Difficulty Levels)
**Purpose:** System decides where to place 'O' based on difficulty

#### Easy Mode Logic
- Get list of all empty positions on board
- Use randint() to select random empty position
- Return selected position
- No strategy, purely random

#### Medium Mode Logic

**Step 1 - Offensive Check (Can System Win?):**
- Loop through all 8 win patterns
- For each pattern, check if:
  * 2 positions contain 'O'
  * 1 position is empty
- If found: return that empty position (winning move!)

**Step 2 - Defensive Check (Can User Win?):**
- Loop through all 8 win patterns
- For each pattern, check if:
  * 2 positions contain 'X'
  * 1 position is empty
- If found: return that empty position (block user!)

**Step 3 - Random Move:**
- If no immediate threats or winning moves
- Get list of empty positions
- Pick random empty position using randint()
- Return position

#### Hard Mode Logic

**Same as Medium Mode, PLUS:**

**Step 3.5 - Strategic Center:**
- After offensive/defensive checks
- Check if center position (4) is empty
- If empty, take center (best strategic position)
- Return position 4

**Step 3.6 - Strategic Corners:**
- If center taken, check corners (0, 2, 6, 8)
- Get list of empty corners
- If any corner empty, pick random corner
- Return corner position

**Step 3.7 - Fallback:**
- Only if all strategic positions taken
- Pick random empty position
- Return position

---

### 4. Check Win Function
**Purpose:** Determine if someone has won the game

**Sub-parts:**
- Loop through all 8 win patterns in list
- For each pattern (3 positions):
  * Get values at those 3 board positions
  * Check if all 3 values are identical
  * Check if values are not empty spaces
  * If both conditions true: winner found!
- Return winner symbol ('X' or 'O')
- If no winner found after checking all patterns, return None

**Logic Example:**
- Pattern [0,1,2] represents top row
- Check: board[0] == board[1] == board[2] and board[0] != ' '
- If true: player with that symbol wins

---

### 5. Check Draw Function
**Purpose:** Check if board is full with no winner

**Sub-parts:**
- Loop through entire board list
- Count number of empty spaces (' ')
- If count equals 0 (board full)
- AND no winner found
- Return True (game is draw)
- Otherwise return False (game continues)

---

### 6. Get Valid Move Function
**Purpose:** Get and validate user's position choice

**Sub-parts:**
- Create input validation loop
- Loop until valid input received:
  * Display prompt: "Enter position (0-8):"
  * Get user input as string
  * Check if input is a digit using isdigit()
  * If not digit: show error, continue loop
  * Convert input to integer
  * Check if position is between 0 and 8
  * If not in range: show error, continue loop
  * Check if board position is empty (' ')
  * If position taken: show "Already occupied" error, continue loop
  * If all validations pass: return position
- Return validated position number

---

### 7. Display Board Function
**Purpose:** Show current game state visually

**Sub-parts:**
- Print position reference guide (optional):
  * "Positions: 0|1|2 / 3|4|5 / 6|7|8"
- Print blank line for spacing
- Print current board state:
  * Row 1: board[0] | board[1] | board[2]
  * Divider: -----------
  * Row 2: board[3] | board[4] | board[5]
  * Divider: -----------
  * Row 3: board[6] | board[7] | board[8]
- Print blank line for spacing
- Make display clean and readable

---

### 8. View Statistics Function
**Purpose:** Show player's game history and performance

**Sub-parts:**
- Display header: "=== GAME STATISTICS ==="
- Display total games played
- Display user wins count
- Display system wins count
- Display draws count
- Calculate and display win percentage:
  * Formula: (user_wins / total_games) × 100
  * Handle division by zero if no games played
- Display current win streak
- Display longest win streak (if tracked)
- Show additional stats:
  * Games against Easy AI
  * Games against Medium AI
  * Games against Hard AI
- Press Enter to return to menu

---

### 9. Settings Function
**Purpose:** Customize game options

**Sub-parts:**
- Display current settings
- Show settings menu:
  1. Change AI difficulty (Easy/Medium/Hard)
  2. Toggle who goes first (User/System)
  3. Reset statistics
  4. Back to main menu
- Get user choice with validation
- Handle each option:

**Change Difficulty:**
- Display difficulty options with numbers
- Get user choice (1/2/3)
- Update ai_settings dictionary
- Display confirmation message

**Toggle First Move:**
- Show current setting
- Ask if system should go first (Y/N)
- Update ai_settings dictionary
- Display new setting

**Reset Statistics:**
- Display warning message
- Ask for confirmation (Y/N)
- If confirmed:
  * Reset all stats to 0
  * Display "Statistics reset" message
- If not confirmed: return to settings menu

- Loop until user chooses back to menu

---

### 10. How to Play Function
**Purpose:** Tutorial for new players

**Sub-parts:**
- Display game title
- Explain objective: "Get 3 of your symbols in a row to win"
- Show empty board with position numbers
- Explain winning patterns:
  * Horizontal rows (show example)
  * Vertical columns (show example)
  * Diagonal lines (show example)
- Show example of winning board:
  * Display board with X winning
- Explain AI difficulty levels:
  * Easy: Random moves
  * Medium: Blocks and attacks
  * Hard: Strategic play
- Explain controls:
  * Enter position number 0-8
  * X is user, O is system
- Display tips:
  * Take center if available
  * Block opponent's winning moves
  * Create multiple winning threats
- Press Enter to return to menu

---

## Program Flow

```
START
  ↓
Initialize all data structures
  ↓
Display welcome message
  ↓
Main Menu Loop:
  ├→ Option 1: Play Game 
  │    ↓
  │    Game Loop (user vs system)
  │    ↓
  │    Update Statistics
  │    ↓
  │    Back to Menu
  │
  ├→ Option 2: View Stats 
  │    ↓
  │    Display Statistics
  │    ↓
  │    Back to Menu
  │
  ├→ Option 3: Settings 
  │    ↓
  │    Modify Settings
  │    ↓
  │    Back to Menu
  │
  ├→ Option 4: How to Play 
  │    ↓
  │    Show Tutorial
  │    ↓
  │    Back to Menu
  │
  └→ Option 0: Exit
       ↓
       Display goodbye message
       ↓
       END
```

---

## Detailed Game Loop Flow

```
1. Reset board to empty
2. Clear move history
3. Determine first player (from settings)
4. Display starting message

5. MAIN GAME LOOP (until game ends):
   
   IF User's Turn:
     a. Display current board
     b. Get valid move from user (0-8)
     c. Place 'X' on board[position]
     d. Add move to history
     e. Check if user won:
        - If YES: 
          * Display "You Win!"
          * Update user_wins
          * Increment total_games
          * Update current_streak
          * END LOOP
     f. Check if draw:
        - If YES:
          * Display "It's a Draw!"
          * Update draws counter
          * Increment total_games
          * Reset current_streak to 0
          * END LOOP
     g. Switch to system's turn
   
   IF System's Turn:
     a. Call AI function to get move position
     b. Place 'O' on board[position]
     c. Display "System chose position X"
     d. Add move to history
     e. Check if system won:
        - If YES:
          * Display "System Wins!"
          * Update system_wins
          * Increment total_games
          * Reset current_streak to 0
          * END LOOP
     f. Check if draw:
        - If YES:
          * Display "It's a Draw!"
          * Update draws counter
          * Increment total_games
          * Reset current_streak to 0
          * END LOOP
     g. Switch to user's turn

6. Display final board
7. Show game summary
8. Ask "Play again? (Y/N)"
   - If Y: Go to step 1
   - If N: Return to main menu
```

---

## AI Strategy Examples

### Easy AI Example
**Scenario:** Random move selection
```
Board State:
 X |   | O 
-----------
   | X |   
-----------
   |   |   

Empty positions: [1, 3, 5, 6, 7, 8]
AI uses randint(0, 5) to pick from empty list
Random choice: index 3 → position 6
AI places O at position 6
```

### Medium AI - Offensive Example
**Scenario:** AI can win in one move
```
Board State:
 O |   | X 
-----------
   | O |   
-----------
   |   |   

Checking win pattern [0,4,8]:
- Position 0: O ✓
- Position 4: O ✓
- Position 8: empty ✓
This is a winning move!
AI places O at position 8 and wins!
```

### Medium AI - Defensive Example
**Scenario:** Block user from winning
```
Board State:
 X |   | X 
-----------
 O |   |   
-----------
   |   |   

Checking win pattern [0,1,2]:
- Position 0: X ✓
- Position 1: empty
- Position 2: X ✓
User can win next turn!
AI blocks by placing O at position 1
```

### Hard AI - Strategic Example
**Scenario:** Take center when available
```
Board State:
 X |   |   
-----------
   |   |   
-----------
   |   |   

AI checks:
1. No winning move available
2. No blocking needed
3. Center (position 4) is empty ✓
AI takes strategic center position 4
```

---

## Sample Output Scenarios

### Scenario 1: User Wins (Easy AI)

```
=== TIC-TAC-TOE GAME ===

Main Menu:
1. Play Game
2. View Statistics
3. Settings
4. How to Play
0. Exit

Your choice: 1

Starting new game! You are X, System is O.
You go first!

Current Board:
Positions: 0|1|2 / 3|4|5 / 6|7|8

   |   |   
-----------
   |   |   
-----------
   |   |   

Enter position (0-8): 4

Current Board:
   |   |   
-----------
   | X |   
-----------
   |   |   

System's turn...
System chose position 2

Current Board:
   |   | O 
-----------
   | X |   
-----------
   |   |   

Enter position (0-8): 0

Current Board:
 X |   | O 
-----------
   | X |   
-----------
   |   |   

System's turn...
System chose position 7

Current Board:
 X |   | O 
-----------
   | X |   
-----------
   | O |   

Enter position (0-8): 8

Current Board:
 X |   | O 
-----------
   | X |   
-----------
   | O | X 

🎉 CONGRATULATIONS! YOU WIN! 🎉

Winning pattern: Diagonal [0,4,8]

Final Board:
 X |   | O 
-----------
   | X |   
-----------
   | O | X 

Statistics Updated:
- Games Played: 1
- Your Wins: 1
- System Wins: 0
- Draws: 0
- Win Rate: 100%

Play again? (Y/N): N

Returning to main menu...
```

---

### Scenario 2: System Wins (Medium AI)

```
=== TIC-TAC-TOE GAME ===

Starting new game! You are X, System is O.
You go first!

Current Board:
   |   |   
-----------
   |   |   
-----------
   |   |   

Enter position (0-8): 1

Current Board:
   | X |   
-----------
   |   |   
-----------
   |   |   

System's turn...
System chose position 4 (taking center)

Current Board:
   | X |   
-----------
   | O |   
-----------
   |   |   

Enter position (0-8): 3

Current Board:
   | X |   
-----------
 X | O |   
-----------
   |   |   

System's turn...
System chose position 5 (blocking your win on row 2)

Current Board:
   | X |   
-----------
 X | O | O 
-----------
   |   |   

Enter position (0-8): 6

Current Board:
   | X |   
-----------
 X | O | O 
-----------
 X |   |   

System's turn...
System chose position 2 (winning move!)

Current Board:
   | X | O 
-----------
 X | O | O 
-----------
 X |   |   

❌ SYSTEM WINS! ❌

Winning pattern: Diagonal [2,4,6]

Final Board:
   | X | O 
-----------
 X | O | O 
-----------
 X |   |   

Analysis:
- You had a good strategy with column 1
- System blocked your win and created a diagonal threat
- System won in 4 moves

Statistics Updated:
- Games Played: 2
- Your Wins: 1
- System Wins: 1
- Draws: 0
- Win Rate: 50%
- Current Streak: 0 (streak broken)

Play again? (Y/N): N
```

---

### Scenario 3: Draw Game (Hard AI)

```
=== TIC-TAC-TOE GAME ===

Starting new game! You are X, System is O.
System goes first! (Hard difficulty)

System's turn...
System chose position 4 (taking center)

Current Board:
   |   |   
-----------
   | O |   
-----------
   |   |   

Enter position (0-8): 0

Current Board:
 X |   |   
-----------
   | O |   
-----------
   |   |   

System's turn...
System chose position 8 (strategic corner)

Current Board:
 X |   |   
-----------
   | O |   
-----------
   |   | O 

Enter position (0-8): 2

Current Board:
 X |   | X 
-----------
   | O |   
-----------
   |   | O 

System's turn...
System chose position 1 (blocking your win on row 1)

Current Board:
 X | O | X 
-----------
   | O |   
-----------
   |   | O 

Enter position (0-8): 6

Current Board:
 X | O | X 
-----------
   | O |   
-----------
 X |   | O 

System's turn...
System chose position 3 (blocking diagonal)

Current Board:
 X | O | X 
-----------
 O | O |   
-----------
 X |   | O 

Enter position (0-8): 5

Current Board:
 X | O | X 
-----------
 O | O | X 
-----------
 X |   | O 

System's turn...
System chose position 7 (last empty space)

Current Board:
 X | O | X 
-----------
 O | O | X 
-----------
 X | O | O 

🤝 IT'S A DRAW! 🤝

The board is full with no winner!

Final Board:
 X | O | X 
-----------
 O | O | X 
-----------
 X | O | O 

Game Analysis:
- Well played! You held your own against Hard AI
- Both players blocked each other's winning moves
- Strategic play resulted in a fair draw

Statistics Updated:
- Games Played: 3
- Your Wins: 1
- System Wins: 1
- Draws: 1
- Win Rate: 33%
- Draw Rate: 33%

Play again? (Y/N): Y

[New game starts...]
```

---

## Additional Features (Optional Enhancements)

### 1. Best of 3/5 Tournament Mode
- Play multiple games in succession
- Track wins across all tournament games
- Declare overall champion at the end
- Award tournament points per win
- Bonus points for winning streak

### 2. Two Player Mode
- User 1 vs User 2 (no AI involved)
- Alternate between X and O
- Track separate statistics for each player
- Player names customization
- Turn indicator shows whose turn it is

### 3. Move Hints System
- User can request hint (limited to 2 per game)
- System suggests best move using Hard AI logic
- Show why that move is recommended
- Using hints reduces final score
- Hints only available in single player mode

### 4. Replay Last Game
- Store complete move history
- Replay game move-by-move
- Show board state after each move
- Identify critical turning points
- Analyze where mistakes were made
- Educational tool for improvement

### 5. Custom Board Symbols
- Let users choose their own symbols
- Instead of X and O, use custom characters
- Examples: ★ vs ☆, 😊 vs 🤖, A vs B
- Store preferences in dictionary
- Visual customization for fun

### 6. Achievement System
**Achievements to track:**
- "First Victory" - Win your first game
- "Undefeated Champion" - Win 5 games in a row
- "Giant Slayer" - Beat Hard AI
- "Perfect Game" - Win in 5 moves (minimum possible)
- "Come Back Kid" - Win after being close to losing
- "AI Tamer" - Beat each difficulty level at least once
- "Marathon Player" - Play 50 total games
- "Draw Master" - Achieve 10 draws

### 7. Game Timer
- Track time taken per move
- Display total game duration
- Add optional time limit per move
- Speed bonus for quick wins
- Leaderboard for fastest wins

### 8. Sound Effects (Text-based)
- Display "DING!" for valid move
- Display "BUZZ!" for invalid move
- Display "VICTORY!" for wins
- ASCII art celebrations
- Makes game more engaging

### 9. Color-coded Display
- Use text formatting if terminal supports
- X in one color, O in another
- Highlight winning combination
- Different color for position numbers
- Enhanced visual experience

### 10. Save/Load Game
- Save current game state to continue later
- Store board, statistics, settings
- Resume from where you left off
- Useful for longer gaming sessions
- Simple file-based storage

---

## Learning Points for Students

### Concepts Covered:

**1. Lists:**
- Board representation using single list
- Win patterns stored as list of lists
- Move history tracking
- Getting empty positions
- List indexing and manipulation

**2. Loops:**
- Main game loop (while not game_over)
- Input validation loops
- Checking all win patterns
- Displaying board elements
- Menu navigation loops

**3. Conditionals:**
- Win condition checking
- Draw detection
- Input validation
- AI decision making (if-elif-else chains)
- Turn switching logic

**4. Dictionaries:**
- Statistics tracking with multiple keys
- Player symbols mapping
- Settings storage
- Achievement tracking (if implemented)

**5. Random Module:**
- Easy AI random moves: randint()
- Random corner selection in Hard AI
- Deciding who goes first: randrange()

**6. Functions:**
- Modular code organization
- Each feature as separate function
- Function parameters and return values
- Code reusability
- Easier debugging and testing

### Problem-Solving Skills:

**Pattern Recognition:**
- Identifying winning combinations
- Checking multiple patterns efficiently
- Understanding board symmetry

**Game State Management:**
- Tracking current board state
- Managing turn-based gameplay
- Updating statistics properly

**AI Logic:**
- Offensive vs defensive strategies
- Priority-based decision making
- Strategic position evaluation

**User Input Handling:**
- Validation and error handling
- Providing helpful error messages
- Creating user-friendly interface

**Data Organization:**
- Choosing appropriate data structures
- Efficient data access patterns
- Managing related information together

---

## Implementation Tips for Students

### Start Simple:
1. First create basic board display
2. Then add user input for moves
3. Add simple win checking (one pattern at a time)
4. Build Easy AI (random moves)
5. Add statistics tracking
6. Enhance AI to Medium/Hard
7. Add menus and features last

### Testing Strategy:
- Test each function independently
- Use print statements to debug
- Try edge cases (full board, first move, etc.)
- Test all win patterns work correctly
- Verify statistics update properly

### Common Mistakes to Avoid:
- Forgetting to check if position is empty
- Not converting input to integer
- Incorrect win pattern coordinates
- Not resetting board between games
- Infinite loops without exit condition

### Code Organization:
- Keep functions short and focused
- Use meaningful variable names
- Add comments for complex logic
- Group related functions together
- Test frequently while building

---

## Game Difficulty Comparison

| Feature | Easy | Medium | Hard |
|---------|------|--------|------|
| Move Strategy | Random | Block + Attack | Strategic + Block + Attack |
| Takes Center | No | Sometimes | Always (if available) |
| Takes Corners | No | Random | Prioritized |
| Blocks User | No | Yes | Yes |
| Looks for Win | No | Yes | Yes |
| Difficulty Level | Beginner | Intermediate | Advanced |
| Win Rate (vs novice) | ~30% | ~60% | ~85% |

---

## Winning Patterns Visual Reference

### Horizontal Wins:
```
Row 1: [0,1,2]
 X | X | X 
-----------
   |   |   
-----------
   |   |   

Row 2: [3,4,5]
   |   |   
-----------
 O | O | O 
-----------
   |   |   

Row 3: [6,7,8]
   |   |   
-----------
   |   |   
-----------
 X | X | X 
```

### Vertical Wins:
```
Column 1: [0,3,6]
 O |   |   
-----------
 O |   |   
-----------
 O |   |   

Column 2: [1,4,7]
   | X |   
-----------
   | X |   
-----------
   | X |   

Column 3: [2,5,8]
   |   | O 
-----------
   |   | O 
-----------
   |   | O 
```

### Diagonal Wins:
```
Main Diagonal: [0,4,8]
 X |   |   
-----------
   | X |   
-----------
   |   | X 

Anti-Diagonal: [2,4,6]
   |   | O 
-----------
   | O |   
-----------
 O |   |   
```

---

**END OF DOCUMENT**

This game teaches fundamental programming concepts while being fun and engaging for students. The complexity can be adjusted based on student level by implementing features gradually.

Good luck with your coding project!