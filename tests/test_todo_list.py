from lib.todo_entry import Todo
from lib.todo_list import TodoList


# test that the initial todo list is empty
def test_initial_completed_state_is_an_empty_list():
    tdl = TodoList()
    assert tdl.complete() == []
    assert tdl.incomplete() == []


# test adding a todo - can get that todo back
def test_add_and_recall_todo():
    tdl = TodoList()
    todo = Todo("Water Plants")
    tdl.add(todo)
    assert tdl.incomplete() == [todo]
