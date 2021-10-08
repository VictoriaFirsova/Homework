"""Task 4.1. Open file data/unsorted_names.txt in data folder.
Sort the names and write them to a new file called sorted_names.txt.
Each name should start with a new line as in the following example:"""

with open('unsorted_names.txt') as text:
    with open('sorted_names.txt', 'w') as result:
        d = sorted(text.readlines())
        result.write("".join(d))
