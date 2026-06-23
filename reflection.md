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
  * Logic of updating the score is unclear to me.
  * When you select a difficulty level other than the regular level, the secret number might be out of range of the level's range.

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
I used Claude Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Claude Code suggested that the hint messages in the `check_guess` function were flipped for result "Too High" and "Too Low", and that they should be swapped. It later suggested to factor out the hint messages from `check_guess`'s returned value because the unit tests only accept a value -- the outcome. These were both correct, and I verified these using my own knowledge/judgement from looking at the code, as well as writing and running new unit tests and actually playing the game.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

In this activity, I tried to be specific on describing my needs and the discrepencies between the expected behaviors and the actual behaviors of the program, and Claude Code did pretty well in suggesting potential bugs and their fixes and I found most of its advice helpful, so there was not really something incorrect or misleading during the process. However, I do want to note that based on reading the codebase, I found that sometimes Claude Code would make assumptions on the game's behaviors or rules that might not be intended. For example, it made assumptions on how the scores are calculated even though neither I nor the documentation specified those. Therefore, it is best to always be wary about the assumptions (that are potentially wrong) AI is making and be more specific about expected behaviors / rules / assumptions while prompting the agent.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decide whether a bug was really fixed by: 1. reading the code and making judgements based on logic 2. writing new unit tests that tackle that specific bug and see if they pass after the fix 3. actually playing the game to see if it performs expectedly

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

By running the first three test cases and also observing the game's behavior in an actual game, I know the original bug of misleading hints is fixed, and the user can now use the hint to approach the correct answer.

- Did AI help you design or understand any tests? How?

Yes. Claude Code helps design the last four test cases 1. to see if the outcome matches the corresponding hint, 2. to check if the wrong casting problem is solved by comparing two numerical values in two scenarios (> and <), 3. to see if wrong guesses always result in the same penalty regardless of whether the number of attempts is even or odd and whether the guess is too high or too low.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
