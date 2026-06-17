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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
