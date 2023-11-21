from lib.diary import *
from lib.diary_entry import *
from lib.todo_entry import *
from lib.todo_list import *


# test when a DiaryEntry is added it appears in the diary's entries list
def test_can_add_diary_entry_and_call_it_back():
    diary = Diary()
    entry = DiaryEntry("My Day", "Today was a great day...", "07979657483")
    diary.add(entry)
    assert entry in diary.all()


# test we can add multiple entries
def test_can_add_multiple_diary_entries():
    diary = Diary()
    entry1 = DiaryEntry("My Day", "Today was a great day...")
    entry2 = DiaryEntry("Meeting", "Met John for coffee at 3pm")
    diary.add(entry1)
    diary.add(entry2)
    assert entry1, entry2 in diary.all()


# add two entries, call count_words and have it return
# the total sum of words in the diary contents
def test_diary_count_words_returns_sum_of_all_words_in_entry_contents():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1 Title", "one two")
    entry_2 = DiaryEntry("Entry 2 Title", "three Four five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 5


# Adding two entries with a total content length of 5 words, we can call
# reading_time with wpm of 2 and have it return '3' to represent the length of time
# it would take to read at that speed after rounding up
def test_reading_time_returns_3_minutes_to_read_5_words_at_2wpm():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1 Title", "one two")
    entry_2 = DiaryEntry("Entry 2 Title", "three Four five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3


# Test adding todos - initial state is 'incomplete'
def test_adding_todo():
    tdl = TodoList()
    todo1 = Todo("Water Plants")
    todo2 = Todo("Read Book")
    tdl.add(todo1)
    tdl.add(todo2)
    assert tdl.incomplete() == [todo1, todo2]


# test marking todo as complete, second todo should remain incomplete
def test_mark_todo_as_complete():
    tdl = TodoList()
    todo1 = Todo("Water Plants")
    todo2 = Todo("Read Book")
    tdl.add(todo1)
    tdl.add(todo2)
    todo1.mark_complete()
    assert tdl.complete() == [todo1]
    assert tdl.incomplete() == [todo2]


# test adding a todo - can get that todo back
def test_add_and_recall_todo():
    tdl = TodoList()
    todo = Todo("Water Plants")
    tdl.add(todo)
    assert tdl.incomplete() == [todo]
    assert todo not in tdl.complete()


# test that when adding a todo, it is not added to the 'completed' list
def test_new_todo_is_not_complete():
    tdl = TodoList()
    todo = Todo("Water Plants")
    tdl.add(todo)
    assert todo not in tdl.complete()


"""
Given a Todo in a TodoList
When it is marked as complete
Then it should not appear in the incomplete list
"""


def test_mark_todo_as_complete_adds_it_tocompleted_list():
    todo_list = TodoList()
    todo = Todo("Buy groceries")
    todo_list.add(todo)
    todo.mark_complete()
    assert todo not in todo_list.incomplete()


# test marking all as complete - i.e. 'give up'
# incomplete should now be empty
def test_mark_all_as_complete():
    tdl = TodoList()
    todo1 = Todo("Water Plants")
    todo2 = Todo("Read Book")
    tdl.add(todo1)
    tdl.add(todo2)
    tdl.give_up()
    assert tdl.complete() == [todo1, todo2]
    assert tdl.incomplete() == []


# test that asserts all contact information is returned
# from multiple sample diary entries


def test_retrieving_all_contacts():
    diary = Diary()
    entry1 = DiaryEntry("My Day", "Today was a great day!")
    entry2 = DiaryEntry(
        "Meeting with Alice", "Discussion about project.", "07979657483"
    )
    entry3 = DiaryEntry(
        "Lunch with Bob", "Had a great lunch at the café.", "07979657987"
    )
    entry4 = DiaryEntry(
        "Conference Debrief", "Summarizing the key points.", "07979657484"
    )

    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    diary.add(entry4)

    expected_contacts = ["07979657987", "07979657483", "07979657484"]
    retrieved_contacts = diary.get_all_contacts()

    assert sorted(retrieved_contacts) == sorted(expected_contacts)
