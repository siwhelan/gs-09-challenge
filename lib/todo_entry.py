from lib.todo_list import *


class Todo:
    def __init__(self, task):
        self.task = task
        self.complete = False

    def mark_complete(self):
        self.complete = True
