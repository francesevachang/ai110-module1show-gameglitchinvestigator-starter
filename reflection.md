# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?  

  In the Developer Info section, the number of attempts is set to 1 and the initial score is 0. History shows an empty list. The settings of the difficulty section seem to be a bit off -- higher difficulty does not neccessarily shows a larger range of numbers to guess from and less number of allowed guesses.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  * In the Developer Debug Info section, the number of attempts starts with 1 although I have not started guessing (I believe it should start with 0).
  * The history of the last guess is recorded only when I submit the next guess. The same applied for the update of the number of attempts.
  * When I start a new game, the history and score are not reset (while attempts is set to 0), and the page is showing "Game over. Start a new game to try again."

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess 55 when secret is 21 | hint should show go lower  | hint shows go higher| none |
| guess 20 when secret is 82 | hint should show go higher  | hint shows go lower| none |
| guess 102 when secret is 82 | should show 102 is out of range and keep the same number of attempts | hint shows go lower, and number of attempts is incremented by 1 | none |
|||||

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
