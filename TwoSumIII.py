class TwoSum:

    # initialize your data structure here
    def __init__(self):
        self.dtable = {}

    # @return nothing
    def add(self, number):
        if number not in self.dtable.keys():
            self.dtable[number] = 1
        else:
            self.dtable[number] += 1

    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        print self.dtable
        for k in self.dtable.keys():
            if k == (value - k) and self.dtable[k] > 1:
                return True
            elif k != (value - k) and self.dtable.has_key(value - k):
                return True
        return False

if __name__ == '__main__':
    s = TwoSum()
    s.add(1)
    s.add(3)
    s.add(5)
    print s.find(4)