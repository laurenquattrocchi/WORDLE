# test_wyrdl.py

import wyrdl

def test_generate_word():
    """Test that a random word from the word list is chosen."""
    word_list = ["SNAKE", "CRANE", "WYRDL"]
    assert wyrdl.generate_word(word_list) in word_list