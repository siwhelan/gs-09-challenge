from math import ceil


class Diary:
    def __init__(self):
        self.diary = []

    def add(self, entry):
        # Adds the entry to the entries list
        self.diary.append(entry)

    def all(self):
        # A list of instances of DiaryEntry
        return self.diary

    def get_all_contacts(self):
        # Extracts all contacts from all diary entries
        contacts = []
        for entry in self.diary:
            if entry.contact:  # Only append if contact exists
                contacts.append(entry.contact)
        return contacts

    def count_words(self):
        total_words = 0
        for entry in self.diary:
            total_words += entry.count_words()
        return total_words

    def reading_time(self, wpm):
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        if self.diary == []:
            raise Exception("No entries!")
        word_count = self.count_words()
        return ceil(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        if self.diary == []:
            raise Exception("No entries!")
        # find the max no of words that can be read in the time given
        max_words_read = wpm * minutes
        most_readable = None
        longest_so_far = 0
        # loop throgh the diary entries
        for entry in self.diary:
            # if the word count is less than or equal to
            # the max readable words in that time
            if entry.count_words() <= max_words_read:
                # if that word's count is longer than the existing longest entry
                if entry.count_words() > longest_so_far:
                    # reassign the current longest & most readable to that entry
                    most_readable = entry
                    longest_so_far = entry.count_words()
        return most_readable
