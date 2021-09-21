
"""
Q. 2

Given a number, write a function to its output its reverse digit.
"""
def rev():                                   #define function

    try:                                          # Exception Handling
        n= str(int(input("Enter any no: ")))
        if n[0]=="-":
            print("-"+"".join(reversed(n[1:])))
        else:
            print("".join(reversed(n)))
    except: 
        print("==== ERROR OCCURED ====")
rev()


