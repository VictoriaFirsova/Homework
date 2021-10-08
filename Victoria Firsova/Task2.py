"""Task 4.2. Implement a function which search for most common words in the file. Use data/lorem_ipsum.txt file as a
example. """
import pandas as pd


def most_common_words(filepath, number_of_words=3):
    result_list = []
    with open(filepath) as text:
        result = {}
        for line in text.readlines():
            line = line.split(' ' or ',' or '.')
            for word in line[:]:
                word = word.lower()
                if '\n' in word:
                    word = word.replace('\n', '')
                if '.' in word:
                    word = word.replace('.', '')
                if ',' in word:
                    word = word.replace(',', '')
                if len(word) > 0:
                    if word not in result:
                        result[word] = 1
                    else:
                        result[word] = result[word] + 1

        with open("result.csv", mode="w", encoding='utf-8') as w_file:
            for key in result.keys():
                w_file.write("%s,%s\n" % (key, result[key]))
    df = pd.read_csv('result.csv', delimiter=',', names=['word', 'count'], index_col='word')
    df = df.sort_values(by=['count', 'word'], ascending=[False, True])
    words = df.index
    words = words.tolist()
    for word in words[:number_of_words]:
        result_list.append(word)

    return result_list


print(most_common_words('lorem_ipsum.txt'))
