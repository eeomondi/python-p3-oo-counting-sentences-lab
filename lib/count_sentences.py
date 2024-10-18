class MyString:
    def __init__(self, value=''):
        self.value = value  # This will call the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        """Returns True if value ends with a period, False otherwise."""
        return self.value.endswith('.')

    def is_question(self):
        """Returns True if value ends with a question mark, False otherwise."""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Returns True if value ends with an exclamation mark, False otherwise."""
        return self.value.endswith('!')

    def count_sentences(self):
        """Returns the number of sentences in the value."""
        if not self.value:
            return 0
        # Split on '.', '!', or '?' and filter out empty strings
        sentences = [sentence.strip() for sentence in 
                     self.value.replace('!', '.').replace('?', '.').split('.') if sentence]
        return len(sentences)

