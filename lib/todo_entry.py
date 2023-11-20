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
