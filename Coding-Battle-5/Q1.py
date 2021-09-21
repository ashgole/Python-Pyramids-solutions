"""
Q. 1

Program:
print:
1
2*2
3*3*3
4*4*4*4
5*5*5*5*5
5*5*5*5*5
4*4*4*4
3*3*3
2*2
1
               
    and so on...
    input: integer
"""
def solution(n):                            #defining function
    try:                                        # Exception handling
        #n= int(input("Enter number of rows:"))
        for i in range(n):
            print(((str(i+1)+'*')*(i+1))[:-1])
        for i in range(n):
            print(((str(n-i)+'*')*(n-i))[:-1])
    except:
            print("========== Error Occured ===========")

if __name__ == "__main__":                              # Testcase
    solution(4)