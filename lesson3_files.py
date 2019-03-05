

def text_letters_counter(text):
    with open(text, 'r', encoding='UTF-8') as f:
        content = f.read()
        letters = len(content)
        return letters


def text_words_counter(text):
    with open(text, 'r', encoding='UTF-8') as f:
        content = f.read()
        words = len(content.split())
        return words

def text_dots_replacer(text):
    with open(text, 'r', encoding='UTF-8') as f:
        content = f.read()
        content2 = content.replace('.', '!')
    with open('referat2.txt', 'w', encoding='UTF-8') as f2:
        f2.write(content2)


if __name__ == '__main__':
    text = 'referat.txt'
    text_length = text_letters_counter(text)
    text_words = text_words_counter(text)
    text_dots_replacer(text)
    print("В тексте '{}'  {} символов.".format(text, text_length))
    print("В тексте '{}'  {} слова.".format(text, text_words))
