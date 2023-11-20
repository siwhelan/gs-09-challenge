from lib.diary_entry import *
import pytest


# test that an error is raised when a
# missing title is added to the diary
def test_empty_title_raises_an_error():
    with pytest.raises(Exception) as err:
        DiaryEntry("", "Entry contents")
    assert str(err.value) == "Title missing!"


# test that an error is raised when an entry with
# missing contents is added to the diary
def test_empty_contents_raises_an_error():
    with pytest.raises(Exception) as err:
        DiaryEntry("Title 1", "")
    assert str(err.value) == "Contents missing!"


# test adding contact to existing entry
def test_adding_contact_to_diary_entry():
    entry = DiaryEntry("Meeting with John", "Discussed project details")
    entry.add_contact("07979657483")

    assert entry.title == "Meeting with John"
    assert entry.contents == "Discussed project details"
    assert entry.contact == "07979657483"


# when adding an entry, count_words should return
# the number of words in that entry
def test_count_words_returns_the_number_of_words_in_the_contents():
    entry = DiaryEntry("My Day", "Today was a great day indeed")
    assert entry.count_words() == 6


# test reading_time with a wpm of 2 and five word content, it should return 3
def test_reading_time():
    diary_entry = DiaryEntry("Entry 1 Title", "One two three Four five")
    assert diary_entry.reading_time(2) == 3


# test A string representing a chunk of the contents that the user could
# read in the given number of minutes.
def test_readable_first_chunk():
    diary_entry = DiaryEntry("Entry 1 Title", "One two three Four five")
    assert diary_entry.reading_chunk(2, 1) == "One two"


# If called again, `reading_chunk` should return the next chunk,
# skipping what has already been read, until the contents is fully read.
def test_readable_second_chunk():
    diary_entry = DiaryEntry("Entry 1 Title", "One two three Four five")
    assert diary_entry.reading_chunk(2, 1) == "One two"
    assert diary_entry.reading_chunk(2, 1) == "three Four"
    assert diary_entry.reading_chunk(2, 1) == "five"


# The next call after that it should restart from the beginning.
def test_reading_chunk_resets_after_completion():
    diary_entry = DiaryEntry("Entry 1 Title", "One two three Four five")
    assert diary_entry.reading_chunk(2, 1) == "One two"
    assert diary_entry.reading_chunk(2, 1) == "three Four"
    assert diary_entry.reading_chunk(2, 1) == "five"
    assert diary_entry.reading_chunk(2, 1) == "One two"
