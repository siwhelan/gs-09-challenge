class Contact:
    def __init__(self, number, associated_entry):
        # Parameters:
        #   number: a string representing the contact's phone number
        #   associated_entry: a reference to the DiaryEntry this contact is associated with
        self.number = number
        self.associated_entry = associated_entry
