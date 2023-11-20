from lib.diary import *
from lib.diary_entry import *

"""
Given a Diary instance
When a DiaryEntry is added
Then it should appear in the diary's entries list
"""


def test_can_add_diary_entry_and_call_it_back():
    diary = Diary()
    entry = DiaryEntry("My Day", "Today was a great day...")
    diary.add(entry)
    assert entry in diary.all()
