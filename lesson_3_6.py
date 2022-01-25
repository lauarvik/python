# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(word):
    return word.capitalize()

if __name__ == '__main__':
    print(int_func('text'))
