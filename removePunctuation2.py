f = open("input.txt","r")
text = f.read()
word = text.split()
a = ['a', 'an', 'the']
b = ["!","$","&","'","(",")","-",".",",","?","\""]
c = ["he","she","it","they","who","where","when","there","you","we"]
fi = open("out.txt","w")
for i in range(len(word)):
    for j in range(len(a)):
        for k in range(len(b)):
            for l in range(len(c)):
                if word[i] in a[j]:
                    word[i] = "<Article>"
                elif word[i] in b[k]:
                    word[i] = "<Punctuation>"
                elif word[i] in c[l]:
                    word[i] = "<Pronoun>"
    fi.write(word[i])
f.close()
fi.close()
fil = open("out.txt","r")
txt = fil.read()
print(txt)
fil.close()