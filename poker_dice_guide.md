# Program 19: Poker Dice Game - Complete Development Guide

## Game Overview
A dice-based poker game where players roll 5 dice and try to make poker-style combinations. Players get an initial roll plus 2 chances to re-roll selected dice to improve their hand. Hands are scored based on poker rankings from One Pair (50 points) to Five of a Kind (500 points).

---

## Core Game Mechanics

### Basic Rules
- Player rolls 5 dice (each showing 1-6)
- After seeing results, player can keep any dice and re-roll the rest
- Player gets 2 re-roll opportunities per round
- Final hand is evaluated and scored
- Multiple rounds can be played in tournament mode

### Winning Concept
Unlike traditional poker with cards, this uses dice:
- Instead of suits (hearts, spades), all dice show numbers 1-6
- Combinations are based on matching numbers
- Higher-ranked hands score more points
- Goal: Maximize score over multiple rounds

---

## Poker Hand Rankings (Detailed)

### 1. Five of a Kind (500 points)
**Description:** All 5 dice show the same number
**Examples:**
- [4, 4, 4, 4, 4] ✓
- [1, 1, 1, 1, 1] ✓
- [6, 6, 6, 6, 6] ✓

**Rarity:** Very rare (1.29% chance on single roll)

---

### 2. Four of a Kind (400 points)
**Description:** Four dice show the same number, one different
**Examples:**
- [3, 3, 3, 3, 5] ✓
- [2, 6, 6, 6, 6] ✓
- [1, 1, 1, 1, 4] ✓

**Rarity:** Rare (3.86% chance on single roll)

---

### 3. Full House (300 points)
**Description:** Three dice of one number + Two dice of another number
**Examples:**
- [2, 2, 2, 5, 5] ✓ (Three 2s, Two 5s)
- [4, 4, 6, 6, 6] ✓ (Three 6s, Two 4s)
- [1, 3, 3, 3, 1] ✓ (Three 3s, Two 1s)

**Not Full House:**
- [2, 2, 2, 5, 6] ✗ (Three 2s but no pair)
- [4, 4, 4, 4, 6] ✗ (This is Four of a Kind)

**Rarity:** Uncommon (3.86% chance on single roll)

---

### 4. Straight (200 points)
**Description:** Five consecutive numbers
**Valid Straights:**
- [1, 2, 3, 4, 5] ✓ (Low Straight)
- [2, 3, 4, 5, 6] ✓ (High Straight)

**Order doesn't matter:**
- [3, 1, 4, 2, 5] ✓ (Same as [1,2,3,4,5] when sorted)
- [6, 4, 2, 5, 3] ✓ (Same as [2,3,4,5,6] when sorted)

**Not Straight:**
- [1, 2, 3, 4, 6] ✗ (Missing 5)
- [1, 2, 3, 5, 6] ✗ (Missing 4)

**Rarity:** Uncommon (3.09% chance on single roll)

---

### 5. Three of a Kind (150 points)
**Description:** Three dice show the same number, other two are different
**Examples:**
- [5, 5, 5, 2, 1] ✓
- [6, 3, 6, 1, 6] ✓
- [2, 4, 2, 2, 6] ✓

**Not Three of a Kind:**
- [5, 5, 5, 2, 2] ✗ (This is Full House)
- [5, 5, 5, 5, 1] ✗ (This is Four of a Kind)

**Rarity:** Common (15.43% chance on single roll)

---

### 6. Two Pair (100 points)
**Description:** Two different pairs, one single die
**Examples:**
- [3, 3, 5, 5, 1] ✓ (Pair of 3s, Pair of 5s)
- [2, 4, 2, 6, 4] ✓ (Pair of 2s, Pair of 4s)
- [1, 1, 6, 6, 3] ✓ (Pair of 1s, Pair of 6s)

**Not Two Pair:**
- [3, 3, 3, 5, 5] ✗ (This is Full House)
- [3, 3, 5, 2, 1] ✗ (Only One Pair)

**Rarity:** Common (23.15% chance on single roll)

---

### 7. One Pair (50 points)
**Description:** Two dice show the same number, other three are different
**Examples:**
- [4, 4, 1, 2, 6] ✓
- [3, 5, 3, 1, 6] ✓
- [2, 6, 4, 2, 1] ✓

**Not One Pair:**
- [4, 4, 1, 1, 6] ✗ (This is Two Pair)
- [4, 4, 4, 2, 6] ✗ (This is Three of a Kind)

**Rarity:** Very Common (46.30% chance on single roll)

---

### 8. Nothing / High Card (0 points)
**Description:** No matching numbers at all
**Examples:**
- [1, 2, 3, 4, 6] ✓ (All different, not consecutive)
- [1, 2, 4, 5, 6] ✓ (All different, not consecutive)
- [1, 3, 4, 5, 6] ✓ (All different, not consecutive)

**Not Nothing:**
- [1, 2, 3, 4, 5] ✗ (This is Straight)
- [1, 1, 2, 3, 4] ✗ (This is One Pair)

**Rarity:** Uncommon (9.26% chance on single roll, but often improved with re-rolls)

---

## Data Structures Needed

### 1. Dice List
```
Purpose: Store current values of 5 dice
Type: List of integers
Range: Each element 1-6
Example: [3, 5, 3, 2, 6]
```

### 2. Hand Scores Dictionary
```
Purpose: Map hand names to point values
Structure:
{
    'Five of a Kind': 500,
    'Four of a Kind': 400,
    'Full House': 300,
    'Straight': 200,
    'Three of a Kind': 150,
    'Two Pair': 100,
    'One Pair': 50,
    'Nothing': 0
}
```

### 3. Player Statistics Dictionary
```
Purpose: Track player performance across games
Structure:
{
    'total_rounds': 0,
    'total_score': 0,
    'highest_round_score': 0,
    'best_hand_ever': 'Nothing',
    'five_of_kind_count': 0,
    'four_of_kind_count': 0,
    'full_house_count': 0,
    'straight_count': 0,
    'average_score': 0.0,
    'games_played': 0
}
```

### 4. Tournament Data Dictionary
```
Purpose: Track multi-round tournament progress
Structure:
{
    'round_number': 1,
    'total_rounds': 5,
    'cumulative_score': 0,
    'round_scores': [],  # List of scores per round
    'round_hands': []    # List of hand names per round
}
```

### 5. Frequency Counter Dictionary
```
Purpose: Count occurrences of each die value
Used in: Hand evaluation logic
Structure: {1: count, 2: count, 3: count, 4: count, 5: count, 6: count}
Example: For dice [3,3,5,2,6] → {1:0, 2:1, 3:2, 4:0, 5:1, 6:1}
```

---

## Main Program Structure

### 1. Main Menu Function
**Purpose:** Primary navigation hub

**Display Elements:**
- Game title/banner
- Current statistics summary (if any games played)
- Menu options numbered list

**Menu Options:**
1. Play Single Round
2. Play Tournament (5 Rounds)
3. View Statistics
4. How to Play
5. Settings
0. Exit

**Logic Flow:**
- Display menu
- Get user input (0-5)
- Validate input is a digit and in range
- Call appropriate function based on choice
- Loop until user selects exit
- When exiting, display goodbye message

---

### 2. Play Single Round Function
**Purpose:** Execute one complete game round

**Steps:**

**Step 1: Initial Setup**
- Display round header
- Initialize re-rolls remaining to 2
- Prepare empty dice list

**Step 2: First Roll**
- Roll all 5 dice using random
- Store results in dice list
- Display dice with position numbers
- Evaluate and display current hand
- Show score potential

**Step 3: Re-roll Loop (up to 2 iterations)**
- Check if re-rolls remaining > 0
- Ask user: "Re-roll? (Y/N)"
- If No: skip to final evaluation
- If Yes:
  * Ask which dice to keep
  * Validate input
  * Re-roll unkept dice
  * Display new dice
  * Evaluate new hand
  * Show improvement/downgrade from previous
  * Decrement re-rolls remaining
  * Continue loop

**Step 4: Final Evaluation**
- Display final dice configuration
- Evaluate final hand
- Display hand name prominently
- Display score earned
- Update player statistics
- Show statistics change

**Step 5: Completion**
- Ask if play again
- If Yes: restart function
- If No: return to main menu

---

### 3. Play Tournament Function
**Purpose:** Execute 5-round tournament with cumulative scoring

**Steps:**

**Tournament Setup:**
- Display tournament banner
- Explain rules: 5 rounds, cumulative scoring
- Initialize tournament dictionary
- Set total_rounds to 5
- Set cumulative_score to 0

**Tournament Loop (5 iterations):**

For each round (1 to 5):

**a) Round Header**
- Display "Round X of 5"
- Show current cumulative score
- Show average score so far (if not first round)

**b) Play Round**
- Roll initial 5 dice
- Display dice and hand
- Allow up to 2 re-rolls (same as single round)
- Get final hand and score

**c) Round Summary**
- Display round score
- Add to cumulative_score
- Store round_score in list
- Store hand_name in list
- Display updated cumulative total

**d) Progress Display**
- Show all rounds played so far with scores
- Example: "R1: 150 | R2: 300 | R3: 100"
- Show running average
- Brief pause before next round

**Tournament Completion:**
- Display tournament complete banner
- Show final cumulative score
- Show average per round
- Display round-by-round breakdown
- Identify best round (highest score)
- Identify worst round (lowest score)
- Show hand distribution (how many of each hand type)
- Update global statistics
- Check if tournament score is personal best
- Ask to play another tournament
- Return to main menu

---

### 4. Roll Dice Function
**Purpose:** Generate random dice values

**Parameters:**
- num_dice: How many dice to roll (1-5)

**Logic:**
- Create empty list
- Loop num_dice times:
  * Generate random number 1-6 using randint(1, 6)
  * Append to list
- Return list of dice values

**Return Example:**
- roll_dice(5) → [3, 6, 2, 3, 1]
- roll_dice(3) → [4, 4, 2]

---

### 5. Evaluate Hand Function
**Purpose:** Determine poker hand type from dice

**Parameters:**
- dice: List of 5 integers (1-6)

**Logic:**

**Step 1: Count Frequencies**
- Create frequency dictionary: {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
- Loop through dice list
- For each die value, increment count in dictionary
- Example: [3,3,5,2,6] → {1:0, 2:1, 3:2, 4:0, 5:1, 6:1}

**Step 2: Get Frequency Counts**
- Extract just the counts from dictionary
- Create list of counts: [0, 1, 2, 0, 1, 1]
- Sort counts in descending order: [2, 1, 1, 1, 0, 0]

**Step 3: Pattern Matching (Check in this order!)**

**Check Five of a Kind:**
- If maximum count == 5
- Return ('Five of a Kind', 500)

**Check Four of a Kind:**
- If maximum count == 4
- Return ('Four of a Kind', 400)

**Check Full House:**
- If sorted counts == [3, 2, 0, 0, 0, 0]
- One value appears 3 times, another appears 2 times
- Return ('Full House', 300)

**Check Straight:**
- Sort dice list
- Check if equals [1,2,3,4,5] OR [2,3,4,5,6]
- Return ('Straight', 200)

**Check Three of a Kind:**
- If maximum count == 3
- And NOT Full House (already checked above)
- Return ('Three of a Kind', 150)

**Check Two Pair:**
- Count how many values appear exactly 2 times
- If count == 2 (two different pairs)
- Return ('Two Pair', 100)

**Check One Pair:**
- If maximum count == 2
- And NOT Two Pair (already checked above)
- Return ('One Pair', 50)

**Check Nothing:**
- If all checks failed
- Return ('Nothing', 0)

**Return Format:**
- Tuple: (hand_name, score)
- Example: ('Full House', 300)

---

### 6. Get Dice to Keep Function
**Purpose:** Ask user which dice to preserve during re-roll

**Parameters:**
- dice: Current dice list
- positions: List [0,1,2,3,4]

**Display:**
- Show dice with position numbers
```
Position:  0   1   2   3   4
Dice:     [3] [3] [5] [2] [6]
```

**Prompt Options:**
- Enter specific positions: "0,2,4"
- Enter "all" to keep all dice (no re-roll)
- Enter "none" to re-roll all dice

**Validation:**
- Check if input is "all" or "none" (special cases)
- Otherwise, split by comma
- Convert each to integer
- Check each position is 0-4
- Check no duplicate positions
- If invalid, show error and ask again

**Return:**
- List of positions to keep
- Example: [0, 1] (keep positions 0 and 1)
- Special cases: [0,1,2,3,4] for "all", [] for "none"

---

### 7. Re-roll Dice Function
**Purpose:** Roll new values for selected dice positions

**Parameters:**
- dice: Current dice list
- positions_to_reroll: List of positions to change

**Logic:**
- Loop through positions_to_reroll
- For each position:
  * Generate new random value 1-6
  * Replace dice[position] with new value
- Return updated dice list

**Example:**
```
Input: dice=[3,3,5,2,6], positions=[2,3,4]
Process: Keep [3,3] at positions 0,1
         Re-roll positions 2,3,4
         New values: [1,4,3]
Output: [3,3,1,4,3]
```

---

### 8. Display Dice Function
**Purpose:** Show dice in formatted way

**Parameters:**
- dice: List of 5 integers
- show_positions: Boolean (show position numbers or not)

**Display Format Option 1 (with positions):**
```
Position:  0   1   2   3   4
Dice:     [3] [3] [5] [2] [6]
```

**Display Format Option 2 (dice only):**
```
🎲 Your Dice: [3] [3] [5] [2] [6]
```

**Display Format Option 3 (visual dice):**
```
┌─────┬─────┬─────┬─────┬─────┐
│  3  │  3  │  5  │  2  │  6  │
└─────┴─────┴─────┴─────┴─────┘
  0     1     2     3     4
```

**Logic:**
- Choose format based on preference
- Loop through dice list
- Format each die value
- Add spacing for readability
- Print result

---

### 9. View Statistics Function
**Purpose:** Display comprehensive player performance data

**Display Sections:**

**Section 1: Overview**
- Total games played
- Total rounds played
- Overall total score
- Average score per round

**Section 2: Best Performances**
- Highest single round score
- Best hand ever achieved
- Date/time of best performance (if tracked)

**Section 3: Hand Distribution**
- Five of a Kind: X times
- Four of a Kind: X times
- Full House: X times
- Straight: X times
- Three of a Kind: X times
- Two Pair: X times
- One Pair: X times
- Nothing: X times

**Section 4: Percentages**
- Calculate percentage for each hand type
- Display as bar chart (text-based):
```
Five of a Kind:  █░░░░░░░░░ 2%
Four of a Kind:  ███░░░░░░░ 5%
Full House:      █████░░░░░ 8%
```

**Section 5: Trends (if multiple games)**
- Score improving/declining trend
- Most common hand
- Luckiest number (appears most often)

**Footer:**
- Press Enter to return to menu

---

### 10. How to Play Function
**Purpose:** Tutorial and rules explanation

**Content Sections:**

**Section 1: Game Objective**
- Explain goal: Make highest-scoring poker hands with dice
- Mention cumulative scoring in tournaments

**Section 2: How to Play**
- Step-by-step walkthrough:
  1. Roll 5 dice initially
  2. Decide which to keep
  3. Re-roll others (up to 2 times)
  4. Final hand is scored

**Section 3: Hand Rankings**
- List all 8 hands from best to worst
- Show example of each
- Display point values

**Section 4: Strategy Tips**
- When to keep a hand vs. risk re-roll
- Which hands to aim for
- Re-roll strategy examples

**Section 5: Game Modes**
- Single Round: Practice, no pressure
- Tournament: 5 rounds, cumulative scoring

**Section 6: Controls**
- How to enter dice positions
- Special commands ("all", "none")
- Navigation through menus

**Section 7: Example Round**
- Show complete round playthrough
- Demonstrate decision-making

**Footer:**
- Press Enter to return to menu

---

### 11. Settings Function
**Purpose:** Customize game preferences

**Settings Options:**

**1. Change Tournament Length**
- Default: 5 rounds
- Options: 3, 5, 7, 10 rounds
- Validate input
- Update tournament settings

**2. Toggle Visual Dice**
- Enable/disable fancy dice display
- Simple brackets vs. ASCII art
- Update display preference

**3. Set Re-roll Limit**
- Default: 2 re-rolls
- Options: 1, 2, 3 re-rolls
- Affects difficulty
- Update game settings

**4. Reset All Statistics**
- Display warning
- Confirm with user (Y/N)
- If confirmed:
  * Reset player_stats to defaults
  * Clear history
  * Display confirmation
- If cancelled: return to settings

**5. Auto-suggest Best Dice to Keep**
- Enable/disable hint system
- Shows recommended dice to keep
- Helps beginners learn

**Navigation:**
- Display all settings with current values
- Number each option
- Get user choice
- Apply changes
- Loop until user exits to menu

---

### 12. Update Statistics Function
**Purpose:** Record round results in player stats

**Parameters:**
- hand_name: String (e.g., "Full House")
- score: Integer points earned

**Logic:**

**Update Counters:**
- Increment total_rounds by 1
- Add score to total_score
- Increment specific hand counter (e.g., full_house_count)

**Update Bests:**
- If score > highest_round_score:
  * Update highest_round_score
  * Update best_hand_ever

**Calculate Averages:**
- average_score = total_score / total_rounds
- Round to 2 decimal places

**Special Achievements Check:**
- If five_of_kind_count == 1:
  * Display "First Five of a Kind!" achievement
- If total_rounds == 50:
  * Display "Veteran Player!" achievement
- If average_score > 200:
  * Display "High Roller!" achievement

**Save Statistics:**
- Update player_stats dictionary
- Persist changes (if using file storage)

---

## Program Flow Diagram

```
START PROGRAM
    ↓
Initialize Data Structures
    ↓
Load Saved Statistics (if exists)
    ↓
Display Welcome Banner
    ↓
┌──────────────────────────┐
│     MAIN MENU LOOP       │
│                          │
│  1. Single Round ────────┼──→ Play Round → Update Stats → Back to Menu
│  2. Tournament ──────────┼──→ 5 Round Loop → Final Summary → Back to Menu
│  3. View Statistics ─────┼──→ Display Stats → Back to Menu
│  4. How to Play ─────────┼──→ Show Tutorial → Back to Menu
│  5. Settings ────────────┼──→ Change Settings → Back to Menu
│  0. Exit ────────────────┼──→ Save Stats → Goodbye → END
│                          │
└──────────────────────────┘
```

---

## Detailed Single Round Flow

```
PLAY SINGLE ROUND
    ↓
Initialize: rerolls_left = 2
    ↓
Roll all 5 dice
    ↓
Display dice with positions
    ↓
Evaluate hand
    ↓
Display current hand & score
    ↓
┌─────────────────────────────┐
│     RE-ROLL LOOP            │
│     (while rerolls_left > 0)│
│                             │
│  Ask: "Re-roll? (Y/N)"      │
│      ↓                      │
│     NO → Skip to Final      │
│     YES ↓                   │
│  Ask which dice to keep     │
│      ↓                      │
│  Validate input             │
│      ↓                      │
│  Re-roll unkept dice        │
│      ↓                      │
│  Display new dice           │
│      ↓                      │
│  Evaluate new hand          │
│      ↓                      │
│  Show comparison to previous│
│      ↓                      │
│  Decrement rerolls_left     │
│      ↓                      │
│  Loop back if rerolls > 0   │
└─────────────────────────────┘
    ↓
FINAL EVALUATION
    ↓
Display final dice
    ↓
Display final hand name
    ↓
Display score earned
    ↓
Update statistics
    ↓
Show stats change
    ↓
Ask: "Play again? (Y/N)"
    ↓
YES → Restart Round
NO → Return to Main Menu
```

---

## Hand Evaluation Logic Flow

```
EVALUATE HAND (dice list input)
    ↓
Create frequency counter {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    ↓
Loop through dice, count each value
    ↓
Extract counts to list, sort descending
    ↓
┌──────────────────────────┐
│  CHECK PATTERNS          │
│  (in priority order)     │
├──────────────────────────┤
│  Max count = 5?          │
│  YES → Five of a Kind    │
│  NO ↓                    │
├──────────────────────────┤
│  Max count = 4?          │
│  YES → Four of a Kind    │
│  NO ↓                    │
├──────────────────────────┤
│  Counts = [3,2,...]?     │
│  YES → Full House        │
│  NO ↓                    │
├──────────────────────────┤
│  Sorted = [1,2,3,4,5]    │
│  or [2,3,4,5,6]?         │
│  YES → Straight          │
│  NO ↓                    │
├──────────────────────────┤
│  Max count = 3?          │
│  YES → Three of a Kind   │
│  NO ↓                    │
├──────────────────────────┤
│  Two values count = 2?   │
│  YES → Two Pair          │
│  NO ↓                    │
├──────────────────────────┤
│  Max count = 2?          │
│  YES → One Pair          │
│  NO ↓                    │
├──────────────────────────┤
│  Nothing                 │
└──────────────────────────┘
    ↓
Return (hand_name, score)
```

---

## Sample Program Outputs

### Output 1: Successful Five of a Kind (Best Possible)

```
╔═══════════════════════════════════╗
║    POKER DICE GAME - ROUND 1     ║
╚═══════════════════════════════════╝

Rolling 5 dice...

Position:  0   1   2   3   4
Dice:     [2] [4] [2] [6] [2]

Current Hand: Three of a Kind (three 2s)
Potential Score: 150 points
Re-rolls remaining: 2

Keep this hand or try to improve? (Y to keep, N to re-roll): N

Which dice to keep? (Enter positions like 0,2,4 or 'all' or 'none'): 0,2,4
You chose to keep dice at positions: 0, 2, 4
Keeping: [2] [2] [2]
Re-rolling positions: 1, 3

--- Re-roll 1/2 ---

Position:  0   1   2   3   4
Dice:     [2] [2] [2] [5] [2]

🎉 IMPROVED! Four of a Kind (four 2s)
Potential Score: 400 points (+250 from previous)
Re-rolls remaining: 1

This is an excellent hand! Risk it for Five of a Kind? (Y/N): Y
Brave choice! Going for the jackpot!

Which dice to keep? (Enter positions like 0,2,4 or 'all' or 'none'): 0,1,2,4
You chose to keep dice at positions: 0, 1, 2, 4
Keeping: [2] [2] [2] [2]
Re-rolling position: 3

--- Re-roll 2/2 (FINAL ROLL) ---

Position:  0   1   2   3   4
Dice:     [2] [2] [2] [2] [2]

╔═══════════════════════════════════╗
║   🎰 JACKPOT! FIVE OF A KIND! 🎰  ║
╚═══════════════════════════════════╝

Final Dice:
┌─────┬─────┬─────┬─────┬─────┐
│  2  │  2  │  2  │  2  │  2  │
└─────┴─────┴─────┴─────┴─────┘

Hand: FIVE OF A KIND (All 2s)
Score: 500 POINTS! ⭐⭐⭐

🏆 NEW PERSONAL RECORD! 🏆
This is the highest possible hand!

Statistics Updated:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Rounds Played: 16 → 17
Total Score: 2,950 → 3,250
Full House Count: 3 → 4
Average Score: 184.4 → 191.2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Play another round? (Y/N): N

Returning to Main Menu...
```

---

### Output 3: Tournament Mode - Complete 5 Round Game

```
╔═══════════════════════════════════════════╗
║   POKER DICE TOURNAMENT - BEST OF 5      ║
║   Compete for the highest total score!   ║
╚═══════════════════════════════════════════╝

Tournament Rules:
• Play 5 complete rounds
• Each round: 1 initial roll + 2 re-rolls
• Scores accumulate across all rounds
• Goal: Maximize total score

Press Enter to begin...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 ROUND 1 of 5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Rolling 5 dice...

Position:  0   1   2   3   4
Dice:     [1] [4] [3] [6] [2]

Current Hand: Nothing
Score: 0 points
Re-rolls remaining: 2

Re-roll? (Y/N): Y
Which dice to keep? (Enter positions or 'none'): none
Re-rolling all dice...

Position:  0   1   2   3   4
Dice:     [3] [3] [5] [1] [3]

Current Hand: Three of a Kind (three 3s)
Score: 150 points
Re-rolls remaining: 1

Keep this hand? (Y/N): Y

━━━━ ROUND 1 COMPLETE ━━━━
Final Hand: Three of a Kind
Round Score: 150 points
━━━━━━━━━━━━━━━━━━━━━━━━

Tournament Status:
Round 1: 150 pts
━━━━━━━━━━━━━━━━━━━━━━━━
Cumulative Total: 150 points

Press Enter for Round 2...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 ROUND 2 of 5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Rolling 5 dice...

Position:  0   1   2   3   4
Dice:     [2] [3] [4] [5] [6]

Current Hand: Straight [2,3,4,5,6]
Score: 200 points
Re-rolls remaining: 2

🎯 STRAIGHT! This is a rare hand (3% chance)
Recommended: KEEP IT!

Keep this hand? (Y/N): Y

━━━━ ROUND 2 COMPLETE ━━━━
Final Hand: Straight
Round Score: 200 points
━━━━━━━━━━━━━━━━━━━━━━━━

Tournament Status:
Round 1: 150 pts (Three of a Kind)
Round 2: 200 pts (Straight) ⭐
━━━━━━━━━━━━━━━━━━━━━━━━
Cumulative Total: 350 points
Average: 175 pts/round

Press Enter for Round 3...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 ROUND 3 of 5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Rolling 5 dice...

Position:  0   1   2   3   4
Dice:     [4] [4] [2] [5] [2]

Current Hand: Two Pair (4s and 2s)
Score: 100 points
Re-rolls remaining: 2

Re-roll? (Y/N): Y
Which dice to keep? (Enter positions): 0,1,2,4
Keeping: [4] [4] [2] [2]
Re-rolling position: 3

Position:  0   1   2   3   4
Dice:     [4] [4] [2] [2] [2]

🎊 IMPROVED! Full House (three 2s, pair of 4s)
Score: 300 points (+200 from previous)
Re-rolls remaining: 1

Excellent improvement! Keep it? (Y/N): Y

━━━━ ROUND 3 COMPLETE ━━━━
Final Hand: Full House
Round Score: 300 points
━━━━━━━━━━━━━━━━━━━━━━━━

Tournament Status:
Round 1: 150 pts (Three of a Kind)
Round 2: 200 pts (Straight)
Round 3: 300 pts (Full House) ⭐⭐
━━━━━━━━━━━━━━━━━━━━━━━━
Cumulative Total: 650 points
Average: 217 pts/round

You're doing great! Halfway there!

Press Enter for Round 4...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 ROUND 4 of 5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Rolling 5 dice...

Position:  0   1   2   3   4
Dice:     [6] [1] [3] [5] [4]

Current Hand: Nothing
Score: 0 points
Re-rolls remaining: 2

Re-roll? (Y/N): Y
Which dice to keep? (Enter positions): none
Re-rolling all dice...

Position:  0   1   2   3   4
Dice:     [5] [5] [1] [4] [3]

Current Hand: One Pair (pair of 5s)
Score: 50 points
Re-rolls remaining: 1

Re-roll? (Y/N): Y
Which dice to keep? (Enter positions): 0,1
Keeping: [5] [5]
Re-rolling positions: 2, 3, 4

Position:  0   1   2   3   4
Dice:     [5] [5] [2] [6] [1]

Current Hand: One Pair (pair of 5s)
Score: 50 points (no change)

━━━━ ROUND 4 COMPLETE ━━━━
Final Hand: One Pair
Round Score: 50 points
━━━━━━━━━━━━━━━━━━━━━━━━

Tournament Status:
Round 1: 150 pts (Three of a Kind)
Round 2: 200 pts (Straight)
Round 3: 300 pts (Full House)
Round 4: 50 pts (One Pair)
━━━━━━━━━━━━━━━━━━━━━━━━
Cumulative Total: 700 points
Average: 175 pts/round

One more round to go!

Press Enter for Round 5 (FINAL)...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
             ROUND 5 of 5 (FINAL)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Rolling 5 dice...

Position:  0   1   2   3   4
Dice:     [3] [3] [3] [6] [6]

Current Hand: Full House (three 3s, pair of 6s)
Score: 300 points
Re-rolls remaining: 2

🎊 FULL HOUSE on first roll! Lucky final round!

Keep this hand? (Y/N): Y

━━━━ ROUND 5 COMPLETE ━━━━
Final Hand: Full House
Round Score: 300 points
━━━━━━━━━━━━━━━━━━━━━━━━

╔═══════════════════════════════════════════╗
║       🏆 TOURNAMENT COMPLETE! 🏆          ║
╚═══════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              FINAL RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Round-by-Round Breakdown:
┌────────┬──────────────────────┬─────────┐
│ Round  │ Hand                 │ Score   │
├────────┼──────────────────────┼─────────┤
│   1    │ Three of a Kind      │  150    │
│   2    │ Straight             │  200 ⭐ │
│   3    │ Full House           │  300 ⭐⭐│
│   4    │ One Pair             │   50    │
│   5    │ Full House           │  300 ⭐⭐│
└────────┴──────────────────────┴─────────┘

Performance Summary:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Score: 1,000 points
Average per Round: 200 points
Best Round: Round 3 & 5 (Full House, 300 pts)
Worst Round: Round 4 (One Pair, 50 pts)

Hand Distribution:
Full House: 2 (40%)
Straight: 1 (20%)
Three of a Kind: 1 (20%)
One Pair: 1 (20%)

Performance Rating: EXCELLENT! ⭐⭐⭐⭐

Achievements Unlocked:
✓ "Double Full House" - Get 2 Full Houses in one tournament
✓ "Consistent Player" - Average score above 150

Global Statistics Updated:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Tournaments: 5 → 6
Best Tournament Score: 950 → 1,000 🎉 NEW RECORD!
Total Score All-Time: 8,450 → 9,450
Average Tournament Score: 845 → 875
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏅 NEW PERSONAL BEST TOURNAMENT! 🏅

Play another tournament? (Y/N): N

Returning to Main Menu...
```

---

### Output 4: Unlucky Round - Nothing to One Pair

```
╔═══════════════════════════════════╗
║    POKER DICE GAME - ROUND 1     ║
╚═══════════════════════════════════╝

Rolling 5 dice...

Position:  0   1   2   3   4
Dice:     [1] [2] [4] [5] [6]

Current Hand: Nothing
Score: 0 points
Re-rolls remaining: 2

Tip: All dice are different and not in sequence.
Recommended: Re-roll all

Re-roll? (Y/N): Y
Which dice to keep? (Enter positions): none
Re-rolling all 5 dice...

--- Re-roll 1/2 ---

Position:  0   1   2   3   4
Dice:     [3] [1] [5] [2] [6]

Current Hand: Nothing
Score: 0 points (no change)
Re-rolls remaining: 1

Still no matching dice. Last chance!

Re-roll? (Y/N): Y
Which dice to keep? (Enter positions): none
Re-rolling all 5 dice...

--- Re-roll 2/2 (FINAL ROLL) ---

Position:  0   1   2   3   4
Dice:     [4] [2] [4] [6] [1]

Current Hand: One Pair (pair of 4s)
Score: 50 points

━━━━━━━━━━━━━━━━━━━━━━━━
Final Dice:
Position:  0   1   2   3   4
Dice:     [4] [2] [4] [6] [1]

Hand: ONE PAIR (pair of 4s)
Score: 50 POINTS

Better luck next time! 
At least you got a pair on the final roll.

Statistics Updated:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Rounds Played: 17 → 18
Total Score: 3,250 → 3,300
One Pair Count: 25 → 26
Average Score: 191.2 → 183.3 ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Tip: Sometimes luck isn't on your side. 
Try again for better results!

Play another round? (Y/N): Y

Starting new round...
```

---

### Output 5: Statistics Screen (After Multiple Games)

```
╔═══════════════════════════════════════════╗
║         POKER DICE STATISTICS            ║
╚═══════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                OVERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total Games Played: 6 tournaments + 12 single rounds
Total Rounds Played: 42
Overall Score: 7,650 points
Average Score per Round: 182.1 points

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            BEST PERFORMANCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Highest Single Round: 500 points (Five of a Kind)
Best Tournament Score: 1,000 points
Best Hand Ever: Five of a Kind (all 2s)
Longest Streak: 7 rounds above 150 points

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            HAND DISTRIBUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Five of a Kind:    1  (2.4%)  ████████████████████░░░░ 500 pts
Four of a Kind:    2  (4.8%)  ████████████████░░░░░░░░ 400 pts
Full House:        5  (11.9%) ████████████░░░░░░░░░░░░ 300 pts
Straight:          3  (7.1%)  ██████████░░░░░░░░░░░░░░ 200 pts
Three of a Kind:   8  (19.0%) ████████░░░░░░░░░░░░░░░░ 150 pts
Two Pair:          11 (26.2%) ████░░░░░░░░░░░░░░░░░░░░ 100 pts
One Pair:          10 (23.8%) ████░░░░░░░░░░░░░░░░░░░░  50 pts
Nothing:           2  (4.8%)  ████████████████░░░░░░░░   0 pts

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Most Common Hand: Two Pair (26.2% of rounds)
Rarest Hand (achieved): Five of a Kind (2.4%)
Success Rate: 95.2% (at least One Pair or better)

Score Trend: ↗ IMPROVING
• Last 10 rounds average: 205 pts
• Previous 10 rounds average: 165 pts
• Improvement: +40 pts (+24%)

Lucky Number: 3
(Appears in winning hands 18 times)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
             ACHIEVEMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Jackpot Master - Roll Five of a Kind
✓ Full House Fan - Get 5 Full Houses
✓ Veteran Player - Play 50 rounds
✓ High Roller - Average above 150 pts
✓ Double Full House - 2 Full Houses in one tournament
✓ Consistent Player - Tournament average above 150

Locked Achievements:
⚠ Perfect Tournament - Score 2,000+ in tournament (Best: 1,000)
⚠ Double Jackpot - Get 2 Five of a Kinds (Count: 1)
⚠ Straight Shooter - Get 10 Straights (Count: 3)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Press Enter to return to Main Menu...
```

---

## Additional Features (Optional Enhancements)

### 1. Hint System
**Purpose:** Help beginners learn strategy

**Implementation:**
- Analyze current dice
- Suggest which dice to keep
- Explain reasoning
- Display probability of improvement

**Example Output:**
```
💡 HINT: Keep the three 4s (positions 0,2,3)
   Re-roll positions 1 and 4
   
   Reasoning:
   • You have Three of a Kind (150 pts)
   • Chance of Four of a Kind: ~8%
   • Chance of Full House: ~11%
   • Risk of downgrade: Low
```

### 2. Probability Display
**Purpose:** Show odds of getting each hand

**Display During Game:**
```
Current: One Pair (50 pts)
Re-roll odds with 2 dice:
━━━━━━━━━━━━━━━━━━━━━━━━
Two Pair:        16.7% 
Three of a Kind: 5.6%
Full House:      2.8%
Four of a Kind:  0.5%
━━━━━━━━━━━━━━━━━━━━━━━━
```

### 3. Leaderboard System
**Purpose:** Track top scores across all players

**Features:**
- Top 10 single rounds
- Top 10 tournaments
- Hall of Fame for Five of a Kind
- Weekly/monthly rankings

### 4. Custom Scoring
**Purpose:** Let players adjust point values

**Settings:**
- Set custom points for each hand
- Create "High Risk" mode (higher rewards, harder hands)
- "Quick Game" mode (lower scores, faster games)

### 5. Multiplayer Mode
**Purpose:** Compete against another player

**Features:**
- Take turns rolling
- Same number of re-rolls
- Compare final hands
- Best hand wins round
- Best of 5 rounds tournament

### 6. Sound Effects (Text-based)
**Purpose:** Add excitement to gameplay

**Examples:**
```
Rolling dice... 
🎲 *CLATTER CLATTER* 🎲

Five of a Kind!
🎺 *FANFARE!* 🎺 🎉

Nothing...
💨 *whomp whomp* 💨
```

### 7. Dice Themes
**Purpose:** Visual customization

**Theme Options:**
- Classic: [1] [2] [3] [4] [5] [6]
- Dots: [⚀] [⚁] [⚂] [⚃] [⚄] [⚅]
- Emoji: [1️⃣] [2️⃣] [3️⃣] [4️⃣] [5️⃣] [6️⃣]
- ASCII Art: Full dice faces

### 8. Achievement Badges
**Purpose:** Reward milestones

**Achievement List:**
- 🏆 "First Win" - Complete first round
- 🎰 "Jackpot Master" - Roll Five of a Kind
- 🏠 "Full House Fan" - Get 5 Full Houses
- 🎲 "Dice Veteran" - Play 100 rounds
- ⭐ "Perfect Score" - Get 500 points in a round
- 🔥 "Hot Streak" - 5 rounds above 200 points
- 💎 "High Roller" - Average above 200 points
- 🎯 "Straight Shooter" - Get 10 Straights
- 👑 "Tournament King" - Win 10 tournaments
- 🌟 "Lucky Number" - Roll specific number 100 times

### 9. Save/Load Game
**Purpose:** Continue later

**Features:**
- Save current statistics
- Save tournament progress
- Load previous session
- Multiple save slots

### 10. Tutorial Mode
**Purpose:** Interactive learning

**Features:**
- Guided first round
- Explains each decision
- Shows probabilities
- Practice specific scenarios
- No stats tracking

---

## Implementation Tips for Students

### Start Simple - Build in Phases

**Phase 1: Basic Dice Rolling**
- Create roll_dice() function
- Display dice simply
- Test random generation

**Phase 2: Hand Evaluation**
- Implement evaluate_hand() function
- Test with known dice combinations
- Verify all 8 hand types work

**Phase 3: Single Round**
- Add re-roll logic
- Implement keep/re-roll choice
- Complete one full round

**Phase 4: Statistics**
- Add stat tracking
- Display after each round
- Persist between rounds

**Phase 5: Tournament Mode**
- Loop 5 rounds
- Track cumulative scores
- Display final summary

**Phase 6: Polish**
- Add menus
- Improve displays
- Add features

### Testing Strategy

**Test Each Hand Type:**
- Manually set dice to test patterns
- Verify correct hand identification
- Check score calculation

**Test Edge Cases:**
- All same number (Five of a Kind)
- Sequential numbers (Straight)
- Empty input handling
- Invalid position numbers

**Test User Input:**
- Non-numeric input
- Out of range positions
- Duplicate positions
- Special commands ("all", "none")

### Common Mistakes to Avoid

**Mistake 1: Wrong Hand Priority**
- Full House must check BEFORE Three of a Kind
- Two Pair must check BEFORE One Pair
- Order matters in evaluation!

**Mistake 2: Not Sorting for Straight**
- Dice [3,1,5,2,4] is a Straight
- Must sort first: [1,2,3,4,5]

**Mistake 3: Frequency Counting**
- Don't forget to initialize all numbers 1-6
- Count correctly in dictionary

**Mistake 4: Re-roll Logic**
- Keep track of which dice to preserve
- Don't accidentally re-roll kept dice
- Update dice list correctly

**Mistake 5: Statistics Not Updating**
- Remember to call update function
- Update after EVERY round
- Save changes properly

### Debugging Tips

**Print Statements:**
- Print dice after each roll
- Print frequency dictionary
- Print hand evaluation result
- Print positions to keep/re-roll

**Test Known Scenarios:**
- Set dice manually: dice = [4,4,4,4,4]
- Test hand evaluation
- Verify correct output

**Step Through Logic:**
- Comment out re-roll loops
- Test one feature at a time
- Isolate problems

---

## Learning Outcomes

### Programming Concepts Mastered

**1. Lists:**
- Storing multiple values (5 dice)
- Accessing by index (positions 0-4)
- Modifying elements (re-rolling)
- Sorting (for Straight detection)
- List comprehension (filtering)━━━━━━━━━━━━━━━━━━━━
Total Rounds Played: 15 → 16
Total Score: 2,450 → 2,950
Five of a Kind Count: 0 → 1 🎉
Best Hand Ever: Four of a Kind → Five of a Kind
Average Score: 163.3 → 184.4
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Achievement Unlocked: "JACKPOT MASTER" 🏅
(Roll your first Five of a Kind)

Play another round? (Y/N): N

Returning to Main Menu...
```

---

### Output 2: Strategic Play - Full House Achievement

```
╔═══════════════════════════════════╗
║    POKER DICE GAME - ROUND 1     ║
╚═══════════════════════════════════╝

Rolling 5 dice...

Position:  0   1   2   3   4
Dice:     [5] [5] [3] [1] [6]

Current Hand: One Pair (pair of 5s)
Potential Score: 50 points
Re-rolls remaining: 2

This is a low-scoring hand. Recommended: Re-roll positions 2, 3, 4

Re-roll? (Y/N): Y

Which dice to keep? (Enter positions like 0,2,4 or 'all' or 'none'): 0,1
You chose to keep dice at positions: 0, 1
Keeping: [5] [5]
Re-rolling positions: 2, 3, 4

--- Re-roll 1/2 ---

Position:  0   1   2   3   4
Dice:     [5] [5] [5] [3] [3]

╔═════════════════════════════════╗
║   🎊 FULL HOUSE! 🎊             ║
╚═════════════════════════════════╝

Potential Score: 300 points (+250 from previous)
Re-rolls remaining: 1

Analysis: Three 5s + Pair of 3s
This is an excellent hand (3rd best possible)

Keep this hand? (Y/N): Y
Smart choice! Full House is hard to beat.

Final Dice:
Position:  0   1   2   3   4
Dice:     [5] [5] [5] [3] [3]

Hand: FULL HOUSE
Score: 300 POINTS

Congratulations! Excellent strategic play:
• Started with One Pair (50 pts)
• Kept the pair and re-rolled
• Achieved Full House (300 pts)
• Net gain: +250 points (600% improvement!)

Statistics Updated:
━━━━━━━━━━━━━