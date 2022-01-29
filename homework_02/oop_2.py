class Basket:
    def __init__(self):
        self.items= []

    def add(self, items):
        self.items.append(items)

b = Basket()
b.add({1:'1'})
print(b.items)