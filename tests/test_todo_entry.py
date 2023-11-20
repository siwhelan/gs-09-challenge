from lib.todo_entry import *


# test mark_complete returns TRUE when called
def test_complete_marks_task_completed_to_true():
    # add a task, assert completed = False
    todo = Todo("Water Plants")
    assert todo.complete == False
    # mark as complete
    todo.mark_complete()
    assert todo.complete == True
