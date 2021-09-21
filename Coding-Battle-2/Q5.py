"""
Q. 5

Program:
print:
    1
   1 2
  1   3
 1     4
1 2 3 4 5
                               
    and so on...
    input: integer
"""


def solution(n):                                         #  defining function
    try:                                                 # Exception handling definig function

        #n=int(input("Enter No. of Rows: "))            # input
         
        for i in range(1, n+1):
            for j in range (1, n-i+1):
                print(end=" ")
            for j in range(1, i+1):
                if j ==1 or j == i or i==n:
                    print(j,end=" ")
                else:
                   print(' ',end=" ")     
                    
            print()
    except:
        print("========== Error Occured ===========")   

if __name__ == "__main__":                              #Testcase
    n=5
    output=solution(n)