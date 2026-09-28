# 1. Built-in Iterable & Iterator
numbers = [10, 20]
my_iterator = iter(numbers)

print(next(my_iterator))  # Output: 10
print(next(my_iterator))  # Output: 20
# next(my_iterator)       # Raises StopIteration exception


# 2. Custom Iterator Class
class TopThree:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 3:
            val = self.num
            self.num += 1
            return val
        raise StopIteration

# Usage
for x in TopThree():
    print(x)  # Output: 1, 2, 3
