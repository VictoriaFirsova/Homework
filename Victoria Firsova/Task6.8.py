"""Task 4.8. Implement a Pagination class helpful to arrange text on pages
 and list content on given page.
The class should take in a text and a positive integer which indicate how many symbols will be
 allowed per each page (take spaces into account as well). You need to be able to get the amount 
 of whole symbols in text, get a number of pages that came out and method that accepts the page number
  and return quantity of symbols on this page. If the provided number of the page is missing print the 
  warning message "Invalid index. Page is missing". If you're familliar with using of Excpetions in Python 
  display the error message in this way. Pages indexing starts with 0.
"""
class Pagination:
    def __init__(self, string, number):
        self.string = string
        self.number = number
        self.pages = []
        start = 0
        a = len(string)
        index = 0
        while index+1!=a and index+1<a:
            self.pages.append(string[index:index+self.number])
            index += self.number
        self.page_count = len(self.pages)
        self.item_count = len(self.string)


    def count_items_on_page(self, num_of_page):
        try:
            result = len(self.pages[num_of_page])
            return result
        except Exception:
            result = 'Invalid index. Page is missing.'
        finally:
            return result

    def find_page(self, text):
        result = []
        try:
            count = 0
            last_index = self.string.find(text) + len(text)
            n = 0
            if text in self.string :
                index = self.string.find(text)
                while n < len(self.string) and index <= last_index :
                    for i in range(n, n + self.number) :
                        if i == index :
                            if count not in result :
                                result.append(count)
                            index += 1
                        else :
                            continue
                    n += self.number
                    count += 1
            else:
                raise Exception
        except Exception:
            result = f'No such string ({text}) in your first text'
        finally:
            return result

    def display_page(self, num_of_page):
        result = None
        try :
            result = self.pages[num_of_page]
            return result
        except Exception :
            result = 'Invalid index. Page is missing.'
        finally :
            return result


pages = Pagination('Your beautiful text', 5)
print(pages.page_count)
#4
print(pages.item_count)
#19
print(pages.count_items_on_page(0))
#5
print(pages.count_items_on_page(3))
#4
print(pages.count_items_on_page(4))
#Exception: Invalid index. Page is missing."""
"""Optional: implement searching/filtering pages by symblos/words and displaying pages with all the symbols on it.
 If you're querying by symbol that appears on many pages or if you are querying by the
  word that is splitted in two return an array of all the occurences.

Example:
"""
print(pages.find_page('Your'))
#[0]


print(pages.find_page('beautiful'))
#[1, 2]
print(pages.find_page('great'))
#Exception: 'great' is missing on the pages
print(pages.display_page(0))
#'Your '
