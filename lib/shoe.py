class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  # This will call the setter
        self.condition = "Used"  # Initial condition of the shoe

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")  # Output message
        self.condition = "New"  # Set the condition to "New" after repair