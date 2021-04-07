class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        diffs = []
        elements = self.__elements
        n = len(elements)
        for i in range(len(elements[1:n])):
            for j in elements[i+1:n]:
                diffs.append(abs(elements[i]-j))
        self.maximumDifference = max(diffs)

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)