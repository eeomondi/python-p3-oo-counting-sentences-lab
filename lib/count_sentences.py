class MyString:
    def __init__(self, value=''):
        self.set_value(value)

    def set_value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        import re
        sentences = [s for s in re.split(r'[.!?]', self.value) if s.strip()]
        return len(sentences)


string = MyString()
string.set_value(123)  
# Example usage
# This will print: "The value must be a string."