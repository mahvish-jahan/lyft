class OctoprimeTires:

    def __init__(self, arr):
        self.arr = arr

    def needs_service(self):
        arr_sum = sum(self.arr)
        return True if arr_sum >= 3 else False
