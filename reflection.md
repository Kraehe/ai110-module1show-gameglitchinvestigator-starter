# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
- The 'hints' were not accurate, giving players incorrect information (ex. suggesting to guess a higher number than 100 when the previous guess already was 100).
- Upon loading the page for the first time the game shows that the player has already used 1 attempt, starting with 7 attempts left instead of 8.
- The game over state continues even after pressing new game, not allowing players to play again without refreshing the page.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Refresh | Game starts with 8 attempts | Game starts with 7 attempts | Uncaught ReferenceError: jw is not defined
    at <anonymous>:1:9
    at <anonymous>:1:54 |
| User inputs 99 as a guess | Win, or hint suggests to guess lower | Hint suggests to guess higher. Wins if the guess is correct. | VM595:1 Uncaught ReferenceError: jw is not defined
    at <anonymous>:1:9
    at <anonymous>:1:54 |
| user inputs 1 as a guess | Win, or hint suggests to guess higher | Hint suggests to guess lower. Wins if the guess is correct. | VM595:1 Uncaught ReferenceError: jw is not defined
    at <anonymous>:1:9
    at <anonymous>:1:54 |
| Press New Game button after running out of attempts | Game resets with 8 attempts |  User is unable to submit additional guesses.  History of previous attempts are not cleared and attempts left are not reset even though the UI shows that the user now has 8 attempts.| Uncaught ReferenceError: jw is not defined

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  I used GitHub Copilot (Copilot CLI and VS Code agent).

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  **Correct AI Suggestion: Identifying the off-by-one error in the attempts counter**
  
  The AI agent correctly diagnosed that `st.session_state.attempts += 1` was being executed BEFORE validating whether the guess was valid. The AI suggested moving this increment to AFTER the `parse_guess()` validation check. This meant invalid inputs (empty strings, non-numbers) would no longer consume an attempt. 
  
  **Verification:** I manually tested by entering invalid guesses (blank input, random letters) and confirmed that the attempts counter no longer decremented. Then I ran the game with valid guesses and confirmed it properly started with 8 attempts instead of 7. The "Attempts left" display now correctly shows 8 on page load.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  **Incorrect AI Suggestion: Misunderstanding the hint logic**
  
  The AI agent initially suggested that the hint logic was correct and that the issue might be with how the secret number was generated. However, upon reviewing the code myself, I realized that the hint logic was indeed reversed (it was telling players to guess higher when they should guess lower and vice versa). The AI's suggestion led me down a rabbit hole of checking the random number generation instead of looking at the hint conditions.

  **Verification:** I manually tested by entering guesses of 1 and 100 and observed that the hints were incorrect (told me to go higher when I guessed 100, which is impossible). This confirmed that the issue was with the hint logic, not the secret number generation.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I verified each fix by running the Streamlit app locally and testing the specific scenarios mentioned in the bug report. For the attempts counter, I reloaded the page and confirmed it showed 8 attempts instead of 7. For the hint reversal, I tested with guesses of 1, 50, and 99 to confirm the hints were correct in both directions. I also tested the reset functionality by playing through a game, losing, and then hitting "New Game" to confirm the game state properly reset (attempts, history, and secret number).

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

  **Manual Integration Test:** I played through a complete game on Normal difficulty (range 1-100, 8 attempts). Testing sequence:
  1. Entered invalid input (blank) → confirmed attempts counter stayed at 8
  2. Entered guess 50 (assuming secret was different) → received valid hint
  3. Continued guessing with hints guiding me correctly → won the game
  4. Hit "New Game" button → verified the game properly reset (history cleared, attempts reset to 8, new secret generated)
  5. Entered guess 1,received "Go HIGHER!" (correct)
  6. Entered guess 100, received "Go LOWER!" (correct)
  
  This showed that all three bugs were fixed: attempts initialization, hint direction, and game reset.

- Did AI help you design or understand any tests? How?

  The AI agent helped structure the debugging process by identifying  and explaining the fixes and tests for each bug (entering invalid input, testing edge guesses like 1 and 100, testing the reset flow). This systematic approach helped me verify that the fixes were complete and not causing new issues.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - Using one session to fix a bug, keeps AI suggestions focused and prevents me from getting overwhelmed by too many changes at once. It also allows me to verify that each fix is working before moving on to the next issue.
- What is one thing you would do differently next time you work with AI on a coding task?
  - I would try to be more specific in my prompts to the AI, especially when asking for help with debugging. For example, instead of asking "How do I fix this bug?" I could ask "How do I fix the off-by-one error in my attempts counter?" This would help the AI provide more targeted suggestions and reduce the chances of it giving me misleading information.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project showed me that while AI can be a powerful tool for generating code and suggesting fixes, it's crucial to critically evaluate its suggestions and not take them at face value. I also learned that AI can critically misunderstand the context or logic of the code, so it's imperitave to really understand the codebase and to test changes thoroughly.
