class BinarySearch:
    def __init__(self):
        self.lo = 1
        self.hi = 100

    def choose_guess(self):
        return (self.lo + self.hi) // 2

    def update(self, feedback):
        if feedback == "Try Higher":
            self.lo = (self.lo + self.hi) // 2 + 1
        elif feedback == "Try Lower":
            self.hi = (self.lo + self.hi) // 2 - 1