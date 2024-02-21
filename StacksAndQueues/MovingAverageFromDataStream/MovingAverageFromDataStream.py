from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque(maxlen=size)

    def next(self, val: int) -> float:
        self.queue.append(val)
        currentSum = 0
        for element in self.queue:
            currentSum += element
        return currentSum / len(self.queue)

class MovingAverageImproved:
    def __init__(self, size: int):
        self.queue = deque(maxlen=size)

    def next(self, val: int) -> float:
        self.queue.append(val)
        return sum(self.queue) / len(self.queue)

class MovingAverageEvenBetter:
    def __init__(self, size: int):
        self.queue = deque()
        self.max_size = size
        self.moving_sum = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.max_size:
            removed_element = self.queue.popleft()
            self.moving_sum -= removed_element

        self.queue.append(val)
        self.moving_sum += val
        return self.moving_sum / len(self.queue)


obj = MovingAverageEvenBetter(3)
print(obj.next(1))  # 1
print(obj.next(10))  # 5.5
print(obj.next(3))  # 4.66667
print(obj.next(5))  # 6
