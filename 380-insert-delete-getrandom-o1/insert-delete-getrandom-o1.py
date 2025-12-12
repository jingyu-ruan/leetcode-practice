import random
class RandomizedSet:

    def __init__(self):
        self.num_set = set()

    def insert(self, val: int) -> bool:
        if val in self.num_set:
            return False
        self.num_set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_set:
            return False
        self.num_set.remove(val)
        return True

    def getRandom(self) -> int:
        lst = list(self.num_set)
        a = random.randint(0, len(lst) - 1)
        return lst[a]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()