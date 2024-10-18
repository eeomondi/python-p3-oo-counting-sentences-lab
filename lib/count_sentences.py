class MyString:
    def __init__(self, value=''):
        self._value = value  # Use a private variable to store the value
        self.value = value   # This will call the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value
