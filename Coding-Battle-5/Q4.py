"""
Q. 4

Program:
print:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28

    and so on...
    input: integer
"""



def solution(n):                # defining function
    try:                        # exception handling

        j=1
        for i in range(1,n+1):
            print(" ".join(str(x) for x in range(j,j+i)))
            j=j+i
    except:
            print("========== Error Occured ===========")

if __name__ == "__main__":                              # Testcase
    solution(7)