"""Task 4.2. Implement custom dictionary that will memorize 10 latest changed keys.
Using method "get_history" return this keys."""


class HistoryDict:
    key_list = []

    def __init__(self, dicts: dict):
        self.dicts = dicts

    def set_value(self, key, value):
        if len(self.key_list) > 10:
            del self.key_list[0]
        self.dicts[key] = value
        self.key_list.append(key)

    def get_history(self):
        print(self.key_list)

# Example:


d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
d.get_history()

# ["bar"]
# After your own implementation of the class have a look at collections.deque
# https://docs.python.org/3/library/collections.html#collections.deque
