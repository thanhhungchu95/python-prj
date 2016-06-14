
print("***PygLatin Translator***")

word = 'empty'

def trans(w):
    w = w + w[0] + 'ay'
    return w[1:]

while word.isalpha():
    word = input("Type word: ")
    if len(word) == 0:
        print("Exit")
        break
    print("Translate: {}".format(trans(word)))
