# 1. Programming Project: Casino Slot Machine (User vs System) #

## Objective ##
Design and implement a Casino Slot Machine game in Python where a user plays against the system. The game must use only basic Python concepts such as loops, conditional statements, lists, dictionaries, and random number generation.

---

## *Game Rules and Requirements* ##
### 1. Symbols and Slots ###
 * The slot machine uses 7 symbols, represented using numbers and stored in a dictionary:

`symbols = {1: 'Cherry', 2: 'Lemon', 3: 'Orange', 4: 'Star', 5: 'Diamond', 6: 'Seven', 7: 'Jackpot'}`

 * Each spin generates three random symbols.

---

### 2. Wallet System ###
 * Both User and System have wallets (coin balance).
 * Initial balance :
    - `User: 1000 coins`
    - `System: 1000 coins`
 * All bets and winnings must update these wallets correctly.

---

### 3. Game Modes ###
The program must display a menu with the following options:
1. Single Spin Mode
2. Multi-Round Mode `*(Best of 5)*`
3. Exit
The menu must run in a loop until the user chooses to exit.

---

### *4. Single Spin Mode (User vs System)* ###
In this mode :
1. User enters a bet amount.
2. System places a **random bet** based on its wallet.
3. Both bets are **held temporarily**.
4. User spins (3 symbols).
5. System spins (3 symbols).
6. Determine the winner:
    - Higher winning amount wins the round.
    - If both results are equal → *Draw*.
7. Settlement rules:
    - Winner receives both bets.
    - In case of draw, **both bets are refunded**.
8. Display:
    - Slot results
    - Round winner
    - Updated wallets

---

### 5. Multi-Round Mode (Best of 5) ###
In this mode :
* The game runs exactly 5 rounds.
* Each round follows the same rules as Single Spin Mode.
* User places a bet in every round.
* System places a new random bet every round.
* Keep track of : 
    * Rounds won by user
    * Rounds won by system

After 5 rounds : 
* Declare the overall winner:
    * User wins more rounds → User wins
    * System wins more rounds → System wins
    * Equal wins → Match Draw
* Display final wallet balances of both user and system.

---

### 6. Winning Rules ###

| Condition | Winning Amount |
| :--- | :--- |
|  3 identical symbols | Bet × 10 |
|  3 Sevens or 3 Jackpots | Bet × 50 |
|  Any 2 identical symbols | Bet × 3 |
|  No match | 0 |

---

### 7. System Betting Rules ###
* System bet must:
    * Be greater than or equal to a minimum bet (e.g., 10 coins)
    * Not exceed its available balance
    * Be chosen randomly
* System should be between `10% - 25% of its wallet` in one round.

---

## Sample Input / Output ##
### Program Start ###

### Output : ###
```python
Welcome to CASINO SLOT MACHINE
------------------------------
User Balance   : 1000 coins
System Balance : 1000 coins

1. Single Spin Mode
2. Multi-Round Mode (Best of 5)
0. Exit

Enter your choice: 1
```

### 1. Sample Output: Single Spin Mode ###

```python
--- SINGLE SPIN MODE ---

Your current balance   : 1000
System current balance : 1000

Enter your bet amount: 100

System bets: 80

Spinning slots...

User Slots   : [ Cherry | Cherry | Star ]
System Slots : [ Lemon | Lemon | Orange ]

User wins this round!

User wins 300 coins
System loses 80 coins

Updated Balances:
User Balance   : 1200
System Balance : 920
```

### 2. Sample Output: Draw Case (Important) ###

```python
--- SINGLE SPIN MODE ---

Your current balance   : 1200
System current balance : 920

Enter your bet amount: 200

System bets: 200

Spinning slots...

User Slots   : [ Star | Star | Lemon ]
System Slots : [ Orange | Orange | Diamond ]

Result: DRAW

Both bets refunded.

Updated Balances:
User Balance   : 1200
System Balance : 920
```
###3. Sample Output: Multi-Round Mode (Best of 5)###

```python
--- MULTI-ROUND MODE (BEST OF 5) ---

Round 1
-------
User Balance   : 1000
System Balance : 1000

Enter your bet: 100
System bets: 150

User Slots   : [ Seven | Seven | Seven ]
System Slots : [ Cherry | Lemon | Star ]

User wins Round 1
User wins 5000 coins

--------------------------------

Round 2
-------
User Balance   : 5900
System Balance : 850

Enter your bet: 300
System bets: 200

User Slots   : [ Lemon | Star | Orange ]
System Slots : [ Diamond | Diamond | Lemon ]

System wins Round 2

--------------------------------

Round 3
-------
Enter your bet: 200
System bets: 100

User Slots   : [ Star | Star | Lemon ]
System Slots : [ Star | Star | Lemon ]

Result: DRAW
Bets refunded

--------------------------------

Round 4
-------
Enter your bet: 400
System bets: 300

User Slots   : [ Cherry | Cherry | Cherry ]
System Slots : [ Lemon | Orange | Star ]

User wins Round 4

--------------------------------

Round 5
-------
Enter your bet: 200
System bets: 150

User Slots   : [ Lemon | Orange | Star ]
System Slots : [ Diamond | Diamond | Seven ]

System wins Round 5
```

### 4. Final Tournament Result ###

```python
--- FINAL RESULT ---

Rounds won by User   : 2
Rounds won by System : 2
Draw Rounds          : 1

MATCH RESULT : DRAW

Final Wallet Balances:
User Balance   : 6100
System Balance : 700
```

---
---





