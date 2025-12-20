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

### **How to use your tools:**
* A Tuple to store the fixed options: ('Rock', 'Paper', 'Scissors').
* random.choice() (or randrange() to pick an index from your tuple).
* A Dictionary to map what beats what (e.g., {'Rock': 'Scissors', 'Paper': 'Rock'}).

---

## Program 2: Deck of Cards / Blackjack Lite
A simplified version of a card game without the complex betting.

### **The Logic:** Deal cards to a player and a dealer; see who gets closest to 21.

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


### **How to use your tools:**



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


---


