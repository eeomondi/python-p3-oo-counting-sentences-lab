#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("Value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the string into sentences based on '.', '!', and '?'.
        sentences = [s for s in re.split(r'[.!?]', self.value) if s.strip()]
        return len(sentences)
  