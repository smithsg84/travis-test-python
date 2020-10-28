class MyClass():
    """ A class for demo of TraviCI """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def do_something(self):
        """ Add two numbers as a simple behavior to test """
        self.add = self.a + self.b
        return self.add
