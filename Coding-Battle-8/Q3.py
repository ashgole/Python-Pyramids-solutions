def solution(n):
    word1=[]
    word2=[]
    for i,w in enumerate(n):
        if w.isupper():
            word1=n[:i]
            word2=n[i:]
            break
    print(word1)
    print(word2)

solution('helloAsh')