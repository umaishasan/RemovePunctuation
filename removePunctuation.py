import string

with open("input.txt","r") as f:
    text = f.read()
    print(text)
    word = text.split()
    print(word)
    print(string.punctuation)
    # table = str.maketrans("","",string.punctuation)
    # stripped = [w.translate(table) for w in word]
    # print(stripped)
    # assemble = " ".join(stripped)
    # print(assemble)
    # f.close()