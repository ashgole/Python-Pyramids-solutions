"""
Q. 1:

List:  [0, 1, 3, 6, 10]

 Sum of parts of list put together in a new list:  [20, 20, 19, 16, 10, 0]
"""

def new():                                      # function

    try:                                        # Exception Handling
        ls=[0, 1, 3, 6, 10]                     # Declaring list
        nl=[]                                   # New list for storing sum of each part of list
        print("List: ", ls)
        for x in range(0,len(ls)):
            nl.append(sum(ls)) 
            ls.pop(0)
            if len(ls)==0:
                nl.append(0)

        print("\n Sum of parts of list put together in a new list: ", nl)       
    except: 
        print("==== ERROR OCCURED ====")
new()

