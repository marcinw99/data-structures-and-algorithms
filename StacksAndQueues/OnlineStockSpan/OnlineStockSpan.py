from collections import deque


class StockSpannerMonoStackUnoptimised:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        removed_elements = []
        while self.stack and self.stack[-1] <= price:
            removed_elements.append(self.stack.pop())
        answer = 1 + len(removed_elements)
        while removed_elements:
            self.stack.append(removed_elements.pop())
        self.stack.append(price)
        return answer


# more like a sliding window
class StockSpannerStackWithQueuePosition:
    def __init__(self):
        self.queue = []
        self.queue_position = 0
        self.stack = deque()

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1] > price:
            self.stack.popleft()
            self.queue_position += 1
        self.queue.append(price)
        self.stack.append(price)

        while self.queue_position > 0 and self.stack[-1] >= self.queue[self.queue_position - 1]:
            self.stack.appendleft(self.queue[self.queue_position - 1])
            self.queue_position -= 1

        return len(self.stack)


class StockSpannerMonoStack:
    def __init__(self):
        self.stack = deque()

    def next(self, price: int) -> int:
        return 0


obj = StockSpannerMonoStack()
print(obj.next(100))  # 1
print(obj.next(80))  # 1
print(obj.next(60))  # 1
print(obj.next(70))  # 2
print(obj.next(60))  # 1
print(obj.next(75))  # 4
print(obj.next(85))  # 6

# obj2 = StockSpanner()
# print(obj2.next(28))
# print(obj2.next(14))
# print(obj2.next(28))
# print(obj2.next(35))
# print(obj2.next(46))
# print(obj2.next(53))
# print(obj2.next(66))
# print(obj2.next(80))
# print(obj2.next(87))
# print(obj2.next(88))
# 1,1,3,4,5,6,7,8,9,10
