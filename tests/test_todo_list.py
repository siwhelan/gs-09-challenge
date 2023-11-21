from lib.todo_entry import Todo
from lib.todo_list import TodoList


# test that the initial todo list is empty
def test_initial_completed_state_is_an_empty_list():
    tdl = TodoList()
    assert tdl.complete() == []
    assert tdl.incomplete() == []
