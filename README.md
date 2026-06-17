# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose.**  
  The "Number Guessing Game" is an interactive Streamlit application where players guess a random number between 1 and 100. The game provides hints ("Go Higher" or "Go Lower") after each guess and tracks attempts. The player wins when they correctly guess the secret number or loses if they exceed 8 attempts.

- [x] **Detail which bugs you found.**
  1. **Incorrect hint logic**: Hints were reversed—telling players to guess higher when they should guess lower and vice versa.
  2. **Attempt counter off-by-one**: Game started with 7 attempts instead of 8 because the counter was incremented before validation.
  3. **Broken game reset**: After the game ended, clicking "New Game" didn't properly reset the state (history, attempts, and secret number remained unchanged).

- [x] **Explain what fixes you applied.**
  1. **Fixed hint logic**: Reversed the comparison operators so hints now correctly guide players (if guess < secret then "Go HIGHER!", if guess > secret then "Go LOWER!").
  2. **Moved attempt increment**: Moved `st.session_state.attempts += 1` to execute AFTER input validation, ensuring invalid inputs don't consume attempts.
  3. **Added proper reset handler**: Implemented a "New Game" button that clears history, resets attempt counter to 8, and generates a new secret number using Streamlit session state.

## 📸 Demo Walkthrough

This walkthrough demonstrates the fixed guessing game in action:

1. **Game starts**: Player sees "Guess a number between 1 and 100" with an input field and a submit button.
2. **First guess (40)**: Player enters 40. Game correctly responds "Too Low" since the secret number is higher.
3. **Second guess (70)**: Player enters 70. Game correctly responds "Too High" since the secret number is lower.
4. **Score tracking**: After each guess, the score increments by 1. After guess 2, score shows "Attempts: 2".
5. **Third guess (55)**: Player enters 55. Game responds "Too Low" and score updates to "Attempts: 3".
6. **Fourth guess (62)**: Player enters 62. Game responds "Correct! You guessed the number 62 in 4 attempts!"
7. **Game reset**: Player can play again by entering a new guess, and the secret number remains consistent throughout each round (no resetting on button clicks).

The key differences from the broken version:
- ✅ Secret number stays constant (uses Streamlit session state)
- ✅ Hints are accurate ("Higher"/"Lower" logic is correct)
- ✅ Score increments properly with each guess
- ✅ Game ends with a congratulations message upon correct guess

## 🧪 Test Results

============================================= test session starts =============================================
platform win32 -- Python 3.13.14, pytest-9.0.2, pluggy-1.6.0
rootdir: C:\Users\gg\Desktop\codepath\ai-110\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.12.1, cov-7.0.0
collected 15 items                                                                                             

tests\test_game_logic.py ...............                                                                 [100%]

============================================= 15 passed in 0.08s ==============================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
