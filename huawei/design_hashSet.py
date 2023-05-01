# class MyHashSet:

#     def __init__(self):
#         self.elements = set()


#     def add(self, key: int) -> None:
#         self.elements.add(key)

#     def remove(self, key: int) -> None:
#         if key not in self.elements:
#             return
#         # print(self.elements)
#         self.elements.remove(key)
#         # print(self.elements)


#     def contains(self, key: int) -> bool:
#         return key in self.elements

class MyHashSet:
    def __init__(self):
        self.hashSet = {}

    def add(self, key: int) -> None:
        self.hashSet[key] = 1

    def remove(self, key: int) -> None:
        if key in self.hashSet:
            self.hashSet.pop(key)

    def contains(self, key: int) -> bool:
        return key in self.hashSet

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)