class FirstClass:
    def __init__(self, first_param):
        self.first_param = first_param

    def first_method(self):
        pass

FS = FirstClass("Hello")
FS.first_method()


class SimpleClass:
    variable = "This is a class variable."
    def simple_method(self):
        """A simple method that returns a greeting."""
        return "Hello, this is a simple method!"


# Usage
simple_obj = SimpleClass()
print(simple_obj.simple_method())


