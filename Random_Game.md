# Game Programs List

## Program 1: Rock, Paper, Scissors (Extended Version)
You can build the classic version or even "Rock, Paper, Scissors."

### **The Logic:** Compare player input against a computer choice.

**Classic Version : **
Three options: Rock, Paper, Scissors
- Rock beats Scissors
- Paper beats Rock
- Scissors beats Paper

** What Does the Program Do? **
- Player makes a choice - You select Rock, Paper, or Scissors
- Computer makes a choice - The computer randomly picks one option
- Compare the choices - The program determines who wins based on the game rules
- Display the result - Shows whether you won, lost, or tied

Output - 
```python
***** Welcome to Game : ******
--- Rock, Paper, Scissors: Best of 5 ---

--- Round 1 ---
User : Enter your choice (rock, paper, or scissors) : Rock
Computer choice : rock
It's a tie!
Scoreboard -> User: 0 | Computer: 0

--- Round 2 ---
User : Enter your choice (rock, paper, or scissors) : Roc
Invalid input! Please try again.

--- Round 2 ---
User : Enter your choice (rock, paper, or scissors) : Rock
Computer choice : rock
It's a tie!
Scoreboard -> User: 0 | Computer: 0

```


<details>
  <summary>🔍 Click to see the hint</summary>
  * A List to act as the deck.
  -  * random.randrange() to "draw" a card by picking a random index and then removing it from the list.
  -  * A Dictionary to assign values to face cards (e.g., {'King': 10, 'Queen': 10}).
 
 * Why Use These Tools ?
   -  * Tuple for options: ('Rock', 'Paper', 'Scissors')
 * Stores the three game choices
    - * The options never change, so a tuple (unchangeable list) is perfect
        
 ** random.randrange()
  - Makes the computer pick randomly
  - Ensures the computer doesn't always pick the same thing
  - Makes the game fair and unpredictable
 * Dictionary for rules: {'Rock': 'Scissors', 'Paper': 'Rock'}
  - Shows what each choice defeats
  - Instead of writing many if-statements, you lookup the winner quickly
  - Example: Rock defeats Scissors, so 'Rock': 'Scissors'
 * Game Flow
    - You → Choose Rock/Paper/Scissors → Computer → Chooses randomly → Compare → Declare winner!

</details>


---

## Program 2: Deck of Cards / Blackjack Lite
**Program Overview : ** Create a simplified Blackjack card game where a player competes against a dealer to get as close to 21 points as possible without going over.

**Game Objective : ** Goal: Get a hand value closer to 21 than the dealer, without exceeding 21 (called **"busting"**).
* If your total is closer to 21 than the dealer's, you win
* If you go over 21, you bust and lose immediately
* If the dealer goes over 21, you win
* If both have the same total, it's a tie (push)

**Game Requirements**
***1. Create the Deck***
- Build a deck of 52 cards using a List
- Include all four suits: Hearts, Diamonds, Clubs, Spades
- Each suit has 13 cards: Ace, 2-10, Jack, Queen, King
- Example: ['Ace of Hearts', '2 of Hearts', ..., 'King of Spades']

***2. Assign Card Values***
- Number cards (2-10) are worth their face value
- Face cards (Jack, Queen, King) are worth 10 points
- Ace can be worth 1 or 11 (simplified: you can choose one value)
- Use a Dictionary to map face cards to their values:

**Output:**
```python
{'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
```

***3. Deal Cards Randomly***

- Use random.randrange() to pick a random index from the deck list
- Remove the dealt card from the deck so it can't be drawn again
- Deal 2 cards to the player at the start
- Deal 2 cards to the dealer at the start

***4. Player's Turn***

- Show the player's cards and total value
- Ask if the player wants to:
- Hit (draw another card)
- Stand (keep current hand and end turn)
- If the player hits and goes over 21, they bust and lose
- Player can keep hitting until they stand or bust

***6. Determine Winner***

- Compare final totals
- Announce who wins, loses, or if it's a tie

---

## Program 3: Treasure Hunt Game
Design a Python program to create a Treasure Hunt game using a dictionary.

### **Game Requirements:**
* Create a dictionary with 5 locations numbered from 1 to 5.
* Initially, store the value "Empty" for all locations.
* Randomly select one location to hide the treasure and update its value to "Treasure".
* Allow the player 3 attempts to guess the treasure location.
* After each guess:
  * If the guess is correct, display a success message and end the game.
  * If incorrect, display an appropriate message and reduce the remaining attempts.
* If the player fails to find the treasure after all attempts, display the correct treasure location.


---

## Program 4: Dice Battle Game
Write a Python program to simulate a Dice Battle between two players.

### **Game Requirements:**
* Create a dictionary to store player names as keys and their scores as values.
* Each player should roll a dice **5 times**.
* Generate dice values randomly between 1 and 6.
* Add the dice value to the respective player's score.
* After all rolls, display:
  * Final scores of both players
  * Name of the player who wins, or a tie message if scores are equal


---

## Program 5: Monster Attack Game
Develop a Monster Attack game using dictionaries.

### **Game Requirements:**
* Create a dictionary to store the health points of:
  * Player
  * Monster
* Set initial health of both to 100.
* In each round:
  * Player inflicts random damage between 10 and 30.
  * Monster inflicts random damage between 5 and 25.
  * Subtract the damage values from the respective health.
  * Display health status after each round.
* Continue the game until either the player or the monster's health becomes zero or less.
* Display the winner at the end.

---

**Output:**
```python
**Round 1**
-------------------
Player attacks Monster for **25** damage.
Monster attacks Player for **21** damage.
Health Status:
Player: **79** HP
Monster: **75** HP

**Round 2**
-------------------
Player attacks Monster for **25** damage.
Monster attacks Player for **15** damage.
Health Status:
Player: **64** HP
Monster: **50** HP

**Round 3**
-------------------
Player attacks Monster for **30** damage.
Monster attacks Player for **11** damage.
Health Status:
Player: **53** HP
Monster: **20** HP

**Round 4**
-------------------
Player attacks Monster for **15** damage.
Monster attacks Player for **8** damage.
Health Status:
Player: **45** HP
Monster: **5** HP

**Round 5**
-------------------
Player attacks Monster for **16** damage.
Monster attacks Player for **11** damage.
Health Status:
Player: **34** HP
Monster: **-11** HP

**Game Over!**
Player wins!
```

---

## Program 6: Dice Frequency Analyzer
Write a Python program to analyze dice rolls.

### **Game Requirements:**
* Roll a dice **20 times** using a random function.
* Store the frequency of each dice number **(1–6)** in a dictionary.
* Display the final frequency table in a readable format.
* Add a simple probability forecast based on the previous rolls
* each dice roll is independent, the probability of the next number is always 1/6 (uniform distribution). However, we can show the relative frequency of each number so far, which can give an idea of the "trend".


### **Output - **

```python
**Dice Frequency Table**
------------------------
🎲 1: *** (3 times)
🎲 2: ***** (5 times)
🎲 3: * (1 times)
🎲 4: **** (4 times)
🎲 5: *** (3 times)
🎲 6: **** (4 times)

**Forecast (Relative Frequencies)**
---------------------------------
🎲 1: 15.0% chance (based on past 20 rolls)
🎲 2: 25.0% chance (based on past 20 rolls)
🎲 3: 5.0% chance (based on past 20 rolls)
🎲 4: 20.0% chance (based on past 20 rolls)
🎲 5: 15.0% chance (based on past 20 rolls)
🎲 6: 20.0% chance (based on past 20 rolls)

```

---

## Program 7: High Card Wins
Player and computer draw one random card; higher card value wins.

### ** List → cards : **
```python
['2','3',...,'10','Jack','Queen','King','Ace']
```
* Dictionary → card values

### **Key Functionalities**
- Create card deck (no suits required)
- Randomly select one card for player
- Randomly select one card for computer
- Compare values
- Display winner

### **Functions Required**
- draw_card(deck)
- get_card_value(card)
- compare_cards(player, computer)

### **Learning Outcome**
- Random selection without repetition
- Value comparison logic
- Modular coding using functions

---

## Output : 
Output 1: Single Round - Player Wins
```python
Welcome to High Card Wins!
1. Play Single Round
2. Play Multiple Rounds with Score Tracking

Choose game mode (1 or 2): 1

========================================
    🎴 HIGH CARD WINS 🎴
========================================

Rules: Draw a card. Higher card wins!
Card values: 2-10 < Jack < Queen < King < Ace

Press Enter to draw your card...

🎴 YOUR CARD:
 _____ 
| Ace |
|     |
|  Ace|
|_____|

🎴 COMPUTER'S CARD:
 _____ 
|King |
|     |
| King|
|_____|

========================================
  Player's Card: Ace (Value: 14)
  Computer's Card: King (Value: 13)
========================================

🎉 YOU WIN! 🎉

========================================
Play again? (yes/no): no
```

Output 2: Single Round - Computer Wins
```python
Welcome to High Card Wins!
1. Play Single Round
2. Play Multiple Rounds with Score Tracking

Choose game mode (1 or 2): 1

========================================
    🎴 HIGH CARD WINS 🎴
========================================

Rules: Draw a card. Higher card wins!
Card values: 2-10 < Jack < Queen < King < Ace

Press Enter to draw your card...

🎴 YOUR CARD:
 _____ 
|  5  |
|     |
|  5  |
|_____|

🎴 COMPUTER'S CARD:
 _____ 
|Queen|
|     |
|Queen|
|_____|

========================================
  Player's Card: 5 (Value: 5)
  Computer's Card: Queen (Value: 12)
========================================

💻 COMPUTER WINS! 💻

========================================
Play again? (yes/no): no
```

Output 3: Single Round - Tie
```python
Welcome to High Card Wins!
1. Play Single Round
2. Play Multiple Rounds with Score Tracking

Choose game mode (1 or 2): 1

========================================
    🎴 HIGH CARD WINS 🎴
========================================

Rules: Draw a card. Higher card wins!
Card values: 2-10 < Jack < Queen < King < Ace

Press Enter to draw your card...

🎴 YOUR CARD:
 _____ 
| 10  |
|     |
| 10  |
|_____|

🎴 COMPUTER'S CARD:
 _____ 
| 10  |
|     |
| 10  |
|_____|

========================================
  Player's Card: 10 (Value: 10)
  Computer's Card: 10 (Value: 10)
========================================

🤝 IT'S A TIE! 🤝

========================================
Play again? (yes/no): no
```

---


** Program 8 : High Card Wins (Mini Project) **
*** Project Description ***

Design and implement a card game simulation called “High Card Wins”, where a user plays against the computer.
Both the user and the system choose cards from the same deck, and the player with the higher-value card wins the round.

---

Game Rules & Requirements

### 1. Card Deck
Create a list of cards containing only card ranks (no suits):
```python
['Ace', 'King', 'Queen', 'Jack', '2', '3', '4', '5', '6', '7', '8', '9', '10']
```
Use a dictionary to assign values to cards :
- Ace = 14
- King = 13
- Queen = 12
- Jack = 11
- Number cards = their face value

### 2. Round Setup
- The game consists of exactly 5 rounds.
- At the start of each round :
  - Create a fresh deck.
  - Randomly select 5 unique cards from the deck.
  - These 5 cards form a shared deck for that round.

### 3. Gameplay
- The system plays first:
  - Randomly selects one card from the 5-card deck.
  - The selected card is removed from the deck.

- The user plays next:
  - Display the remaining cards.
  - Allow the user to choose one card.

- Display:
  - System’s card
  - User’s card

### 4. Winner of the Round
- Compare card values using the dictionary.
- Declare:
  - User wins the round
  - System wins the round
  - Draw (if both cards have equal value)

### 5. Score Tracking
- Maintain:
  - User score
  - System score
  - Number of draws
- Store the winner of each round.

### 6. Final Result
- After all 5 rounds:
  - Display round-wise results.
  - Show total scores.
  - Announce the final winner or declare the match a draw.

---

## Expected Output (Sample) - 
```python
Round 1:
System card: King
Your cards: ['Ace', '7', '3', '10']
Your choice: Ace
You win this round!
Score → User: 1 | System: 0 | Draws: 0
```


---


