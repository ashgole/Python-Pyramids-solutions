list=['','a','e','i','o','u']
listIndex=['','1','2','3','4','5']

def encode(word):
    encoded=''
    for w in word:
        if w in list:
            encoded += str(list.index(w))
        else:
            encoded+=w
    print(encoded)
encode('hello')
print('*'*20)
def decode(word):
    decoded=''
    for w in word:
        if w in listIndex:
            decoded +=list[int(w)]
        else:
            decoded+=w
    print(decoded)

decode('h3 th2r2')