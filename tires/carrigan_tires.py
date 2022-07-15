class CarriganTires:

    def __init__(self, arr):
        self.arr = arr

    def needs_service(self):
        for x in self.arr:
            if x >= 0.9:
                return True

        return False
