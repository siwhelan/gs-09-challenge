# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

---

As a user
So that I can reflect on my experiences
I want to read my past diary entries

---

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

---

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

---

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries


## 2. Design the Class System

gs_09_challenge/initial_plan.png


```python
class Diary:
    def __init__(self):
        pass

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def get_all_contacts(self):
        # Extracts all contacts from all diary entries
        contacts = []

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass


# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass

    def add_contact(self, contact_number):
        # Create a new Contact instance and add it to the contacts list
        # new_contact = Contact(contact_number, self)
        # self.contacts.append(new_contact)

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning

    # File: lib/todo_list.py
class TodoList:
    def __init__(self):
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


# File: lib/todo.py
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass

class Contact:
    def __init__(self, number, associated_entry):
        # Parameters:
        #   number: a string representing the contact's phone number
        #   associated_entry: a reference to the DiaryEntry this contact is associated with
        self.number = number
        self.associated_entry = associated_entry


```

## 3. Create Examples as Integration Tests

Initial ideas for tests - will add as the program is built

```python
"""
Given a Diary with multiple DiaryEntries
When calculating total reading time for all entries
Then it should correctly sum up the reading times of individual entries
"""
diary = Diary()
diary.add(DiaryEntry("Morning Thoughts", "I had a great morning..."))
diary.add(DiaryEntry("Evening Reflections", "The evening was relaxing..."))
wpm = 100
total_time = diary.reading_time(wpm)



"""
Given a Diary with entries of varying lengths
When finding the best entry for a given reading time
Then it should return the most suitable entry based on user's reading speed and available time
"""
diary = Diary()
diary.add(DiaryEntry("Short Note", "Quick thoughts..."))
diary.add(DiaryEntry("Long Story", "This is a longer story..."))
wpm = 100
minutes = 5
best_entry = diary.find_best_entry_for_reading_time(wpm, minutes)

# diary & contacts

"""
Given a Diary with entries containing contact information
When extracting all contact numbers
Then it should return a list of all contact numbers from the diary entries
"""
diary = Diary()
entry1 = DiaryEntry("Meeting Notes", "Met with John, contact: 07979443221")
entry2 = DiaryEntry("Project Plan", "Collaborate with Alice, contact: 07989765765")
diary.add(entry1)
diary.add(entry2)
entry1.extract_contacts()
entry2.extract_contacts()
contacts = diary.get_all_contacts()

# 


```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

# Diary
"""
Given a Diary instance
When a DiaryEntry is added
Then it should appear in the diary's entries list
"""
diary = Diary()
entry = DiaryEntry("My Day", "Today was a great day...")
diary.add(entry)
assert entry in diary.all()

"""
Given a Diary with multiple entries
When count_words is called
Then it should return the total number of words in all entries
"""
diary = Diary()
diary.add(DiaryEntry("Day 1", "Sunny day"))
diary.add(DiaryEntry("Day 2", "Rainy day"))
assert diary.count_words() == 4 # Assuming 'Sunny day' and 'Rainy day' are 2 words each

# Diary Entry
"""
Given a DiaryEntry instance
When count_words is called
Then it should return the number of words in the entry
"""
entry = DiaryEntry("My Day", "Today was a great day...")
assert entry.count_words() == 5 # Assuming 5 words in the entry

"""
Given a DiaryEntry and a word-per-minute rate
When reading_time is called
Then it should return the time in minutes to read the entry
"""
entry = DiaryEntry("My Day", "Today was a great day...")
wpm = 100
assert entry.reading_time(wpm) == 0.05 # Assuming it takes 0.05 minutes to read at 100 WPM

# todolist

"""
Given a TodoList instance
When a Todo is added
Then it should appear in the incomplete list
"""
todo_list = TodoList()
todo = Todo("Buy groceries")
todo_list.add(todo)
assert todo in todo_list.incomplete()

"""
Given a Todo in a TodoList
When it is marked as complete
Then it should not appear in the incomplete list
"""
todo_list = TodoList()
todo = Todo("Buy groceries")
todo_list.add(todo)
todo.mark_complete()
assert todo not in todo_list.incomplete()
```