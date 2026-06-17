from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# Bug reproduction tests from reflection.md

def test_bug_hints_backwards_high_guess():
    """
    Bug: User inputs 99 as a guess against a secret of 50
    Expected: Hint suggests to guess lower (Too High)
    Previously: Hint suggested to guess higher
    """
    outcome, message = check_guess(99, 50)
    assert outcome == "Too High", "Guess of 99 against secret 50 should be 'Too High'"
    assert "LOWER" in message, "Message should suggest guessing lower"

def test_bug_hints_backwards_low_guess():
    """
    Bug: User inputs 1 as a guess against a secret of 50
    Expected: Hint suggests to guess higher (Too Low)
    Previously: Hint suggested to guess lower
    """
    outcome, message = check_guess(1, 50)
    assert outcome == "Too Low", "Guess of 1 against secret 50 should be 'Too Low'"
    assert "HIGHER" in message, "Message should suggest guessing higher"

def test_parse_guess_valid():
    """Test that valid guesses are parsed correctly."""
    ok, guess_int, err = parse_guess("42")
    assert ok is True
    assert guess_int == 42
    assert err is None

def test_parse_guess_float():
    """Test that float inputs are converted to integers."""
    ok, guess_int, err = parse_guess("42.5")
    assert ok is True
    assert guess_int == 42
    assert err is None

def test_parse_guess_invalid():
    """Test that invalid inputs are rejected."""
    ok, guess_int, err = parse_guess("abc")
    assert ok is False
    assert guess_int is None
    assert err is not None

def test_get_range_easy():
    """Test that Easy difficulty returns range 1-20."""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_get_range_normal():
    """Test that Normal difficulty returns range 1-100."""
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_get_range_hard():
    """Test that Hard difficulty returns range 1-50."""
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_update_score_win():
    """Test that winning on first attempt gives correct points."""
    score = update_score(0, "Win", 0)
    assert score == 90  # 100 - 10 * (0 + 1) = 90

def test_update_score_too_high_even_attempt():
    """Test score update for 'Too High' on even attempts (add points)."""
    score = update_score(0, "Too High", 0)
    assert score == 5  # Even attempt number, so +5

def test_update_score_too_high_odd_attempt():
    """Test score update for 'Too High' on odd attempts (subtract points)."""
    score = update_score(0, "Too High", 1)
    assert score == -5  # Odd attempt number, so -5

def test_update_score_too_low():
    """Test that 'Too Low' always subtracts 5 points."""
    score = update_score(100, "Too Low", 0)
    assert score == 95  # Always -5
