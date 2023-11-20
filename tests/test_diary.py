from lib.diary import *
import pytest


# test initial state is empty
def test_diary_is_initially_empty():
    diary = Diary()
    assert diary.all() == []


# initial word count = 0
def test_initial_word_count_is_zero():
    diary = Diary()
    assert diary.count_words() == 0


# initially raise an error if reading_time is called
def test_reading_time_initially_raises_an_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(2)
    assert str(err.value) == "No entries!"


# initially raise an error if find_best_entry is called
def test_find_best_entry_initially_raises_an_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(2, 2)
    assert str(err.value) == "No entries!"
