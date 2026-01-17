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

