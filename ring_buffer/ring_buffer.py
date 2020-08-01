class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.counter = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        elif len(self.data) == self.capacity:
            self.data.pop(self.counter)
            self.data.insert(self.counter, item)
            self.counter = (self.counter + 1) % self.capacity

    def get(self):
        return self.data