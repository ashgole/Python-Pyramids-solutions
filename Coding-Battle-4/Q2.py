
"""
Q. 2

Program:
print:
        *
      *    *
    *        *
  *            *
*                *
*                *
  *            *
    *        *
      *    *
        *

    and so on...
    input: integer
"""
def solution(n):                            # Defining function
    try:                                    # Exception Handling
        # n= int(input ("Enter n value: "))
        for i in range(n):
            print("  "* (n-i-1)+ "* ", end=" ")
            if i>=1:
                print("  "* (2*i-1)+ "* ", end=" ")
            print()

        for j in range(n):
            print("  " * j + "* ", end= " ")
            if j !=n-1:
                print("  "* (2*n-2*j-3) + "*", end= " ")
            print()
    except:
            print("========== Error Occured ===========")

if __name__ == "__main__":                              # Testcase

    n= 5
    solution(n)