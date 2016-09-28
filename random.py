import random

class Solution():
    def __init__(self):
        self.weights = []

    def setWeight(self, letter, weight):
        if not self.weights:
            self.weights = [[letter, weight]]
        else:
            sum = self.weights[-1][1]
            self.weights.append([letter, weight + sum])

    def getRandomObj(self):
        if not self.weights:
            return 0

        token = random.random() * self.weights[-1][1]
        #
        # for letter, weight in self.weights:
        #     if weight >= token:
        #         return letter

        start = 0
        end = len(self.weights)

        while start + 1 < end:
            mid = start + (end - start)/2
            if self.weights[mid][1] >= token:
                end = mid
            else:
                start = mid

        if self.weights[start][1] >= token:
            return self.weights[start][0]
        else:
            return self.weights[end][0]


so = Solution()
so.setWeight('a', 3)
so.setWeight('b', 1)
so.setWeight('c', 2)
so.setWeight('d', 1)

counts = {}
for i in range(1000):
    ret = so.getRandomObj()
    if ret in counts:
        counts[ret] += 1
    else:
        counts[ret] = 1

print counts
