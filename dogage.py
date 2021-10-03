#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import traceback

def calculator():
    
    # Get dog age
    age = input("Input dog years: ")

    try:
        # Cast to float
        d_age = float(age)

        # If user enters negative number, print message
        # Otherwise, calculate dog's age in human years
        if d_age==1.0:
            h_age=round((15*d_age),2)
            print("The given dog age {} is {} human years".format(d_age,h_age))
        if d_age==2.0:
            h_age=round((12*d_age),2)
            print("The given dog age {} is {} human years".format(d_age,h_age))
        if d_age==3.0:
            h_age=round((9.3*d_age),2)
            print("The given dog age {} is {} human years".format(d_age,h_age))
        if d_age==4.0:
            h_age=round((8*d_age),2)
            print("The given dog age {} is {} human years".format(d_age,h_age))
        if d_age==5.0:
            h_age=round((7.2*d_age),2)
            print("The given dog age {} is {} human years".format(d_age,h_age))
        if d_age>5:
            h_age=round((7*d_age),2)
            print("The given dog age {} is {} human years".format(d_age,h_age))
        
        

    except:
        print(age, "is an invalid age.")
        print(traceback.format_exc())
    
calculator() # This line calls the calculator function


# In[ ]:




