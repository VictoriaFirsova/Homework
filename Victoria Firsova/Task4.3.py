"""Task 4.3. Implement a function which works the same as str.split method
(without using str.split itself, of course)."""


def split_function(text, sep, max_split=-1):
    """Функция работает так же, как метод str.split()

        Первый аргумент - строка, которую нужно разделить.
        Второй аргумент - разделитель.
        Третий аргумент - количество делений. Если оставить пустым, то будет неограничено.
        """
    total_list = []
    if max_split == -1:
        for i in text:
            if i == sep:
                ind = text.index(i)
                total_list.append(text[:ind])
                text = text[ind+1:]
        total_list.append(text)
    else:
        count = 0
        for i in text:
            if count < max_split:
                if i == sep:
                    ind = text.index(i)
                    total_list.append(text[0:ind])
                    text = text[ind+1:]
                    count += 1

        total_list.append(text)

    return total_list


print(split_function('Ты, или я, мы, они', ',', 1))
