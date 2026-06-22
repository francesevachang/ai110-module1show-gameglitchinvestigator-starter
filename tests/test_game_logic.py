from logic_utils import check_guess, update_score, HINT_MESSAGES

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_hint_messages_point_the_right_way():
    # Bug #1: the hint advice was swapped. A guess that is TOO HIGH should
    # tell the player to go LOWER, and TOO LOW should say go HIGHER.
    assert HINT_MESSAGES["Too High"] == "📉 Go LOWER!"
    assert HINT_MESSAGES["Too Low"] == "📈 Go HIGHER!"
    assert HINT_MESSAGES["Win"] == "🎉 Correct!"


def test_check_guess_compares_numerically_not_as_strings():
    # Bug #3: the secret was cast to str on even attempts, so comparisons
    # ran lexicographically ("9" > "50" is True). Numerically, 9 < 50,
    # so this must be "Too Low".
    assert check_guess(9, 50) == "Too Low"
    # "100" < "99" as strings, but 100 > 99 as numbers -> "Too High".
    assert check_guess(100, 99) == "Too High"


def test_too_high_always_deducts_on_even_attempt():
    # Regression: "Too High" used to ADD +5 on even attempt numbers.
    # A wrong guess should always cost 5 points, regardless of parity.
    assert update_score(100, "Too High", 2) == 95
    assert update_score(100, "Too High", 4) == 95


def test_wrong_guesses_are_symmetric():
    # "Too High" and "Too Low" should deduct the same amount.
    high = update_score(100, "Too High", 3)
    low = update_score(100, "Too Low", 3)
    assert high == low == 95
