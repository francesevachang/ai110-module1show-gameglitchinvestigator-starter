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

- [ ] Describe the game's purpose.

   The program acts as a simple number guessing game that lets the user choose a game difficulty level and guess the correct number according to the given hints. If the user enters a number that is too high, the hint prompts the user to go lower, and if the user enters a number that is too low, the hint prompts the user to go higher. This process repeats until the user guesses the correct number or the allowed attempts have all been used, in which case the user loses the game.

- [ ] Detail which bugs you found.

   I found and fixed many bugs in the program. Some includes:

   1. The game gives misleading hints (e.g says go higher when the guess is already too high).

   2. The number of attempts being initialized as 1 when the user has not evem started guessing.

   3. When you select a difficulty level other than the regular level, the secret number might be out of range of the level's range.

- [ ] Explain what fixes you applied.

   I applied many fixes. Some includes:

   1. Swapping the hints so the game gives the correct hint that a user can follow to approach the correct answer.

   2. Set the correct number of initial attempts.

   3. Change the hardcoded number ranges into variables so that selecting each difficulty level actually actually leads to that level's number range.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The user guesses 60.
2. Game shows "too low".
3. The user guesses 90.
4. Game shows "too high".
5. The user repeats the above steps several times until they guess the correct number or loses the game if they reach the allowed attempts and have not yet guessed the right answer.
6. Game ends after the user enters the correct number or the allowed attempts have been run out.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

```
(base) fchang@Francess-MacBook-Air ai110-module1show-gameglitchinvestigator-starter % python -m pytest tests/ -v 2>&1 | tail -16
============================= test session starts ==============================
platform darwin -- Python 3.12.7, pytest-7.4.4, pluggy-1.0.0 -- /Users/fchang/opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/fchang/Desktop/ai110/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.2.0
collecting ... collected 7 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 14%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 28%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 42%]
tests/test_game_logic.py::test_hint_messages_point_the_right_way PASSED  [ 57%]
tests/test_game_logic.py::test_check_guess_compares_numerically_not_as_strings PASSED [ 71%]
tests/test_game_logic.py::test_too_high_always_deducts_on_even_attempt PASSED [ 85%]
tests/test_game_logic.py::test_wrong_guesses_are_symmetric PASSED        [100%]
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
