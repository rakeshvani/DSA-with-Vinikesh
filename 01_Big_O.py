#!/usr/bin/env python
# coding: utf-8

# # O(1) - Constant Time

# 
# The no. of operations do not depend on the size of the input and are always constant.

# In[1]:


import time

array_small = ['vinny' for i in range(10)]
array_medium = ['vinny' for i in range(100)]
array_large = ['vinny' for i in range(10000)]

def finding_vinny(array):
    t0 = time.time()
    for i in array:
        pass
    t1 = time.time()
    print(f'Time taken = {t1-t0}')

finding_vinny(array_small)
finding_vinny(array_medium)
finding_vinny(array_large)


# In[2]:


#Time taken in all 3 cases would be 0.0 seconds because we are only extracting the first and second elements of the arays.
#We are not looping over the entire array.
#We are performing two O(1) operations, which equal to O(2)
#Any constant number can be considered as 1. There we can say this function is of O(1) - Constant Time Complexity.


# # O(m + n)

# In[3]:


import time

large1 = ['vinny' for i in range(100000)]
large2 = ['vinny' for i in range(100000)]

def find_vinny(array1, array2):
    
    #Here there are two different variables array1 and array2.
    #They have to be represented by 2 different variables in the Big-O representation as well.
    #Let array1 correspond to m and array2 correspond to n

    t0 = time.time() #O(1)
    for i in range(0,len(array1)): #O(m)
        if array1[i] == 'vinny': #m*O(1)
            print("Found vinny!!") #k1*O(1) where k1 <= m because this statement will be executed only if the if statement returns True, which can be k1(<=m) times
    t1 = time.time() #O(1)
    print(f'The search took {t1-t0} seconds.') #O(1)

    t0 = time.time() #O(1)
    for i in range(0, len(array2)): #O(n)
        if array2[i] == 'vinny': #n*O(1)
            print("Found vinny!!") #k2*O(1) where k2 <= m because this statement will be executed only if the if statement returns True, which can be k2(<=m) times
    t1 = time.time() #O(1)
    print(f'The search took {t1 - t0} seconds.')#O(1)

find_vinny(large1, large2)

#Total time complexity of the find_vinny function =
#O(1 + m + m*1 + k1*1 + 1 + 1 + 1 + n + n*1 + k2*1 + 1 + 1) = O(6 + 2m + 2n + k1 + k2)
#Now k1<=m and k2<=n. In the worst case, k1 can be m and k2 can be n. We'll consider the worst case and calculate the Big-O
#O(6 + 2m + 2n + m + n) = O(3m + 3n + 6) = O(3(m + n + 2))
#The constants can be safely ignored.
#Therefore, O(m + n + 2) = O(m + n)


# In[4]:


#!jupyter notebook --generate-config -y
#!jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10


# # O(m * n)

# In[5]:


import time

start = time.time()

array1 = ['V','I','N','N','Y']
array2 = [14,'JR','1A',0,430]

# print("time ", time.time() - start)

def pair(array1,array2):
    
    # Here there are two different variables array1 and array2.
    # They have to be represented by 2 different variables in the Big-O representation as well.
    # Let array1 correspond to m and array2 correspond to n
    
    for i in range(len(array1)): #n*O(m)
        for j in range(len(array2)): #m*O(n)
                print(array1[i],array2[j]) #m*n*O(1)
pair(array1,array2)

end =  time.time() - start

print("time taken by : ", end)


# In[6]:


#Total time complexity of the pair function =
#O(n*m + m*n + m*n*1) = O(3*m*n)
#The constants can be safely ignored.
#Therefore, O(m * n * 3) = O(m * n)


# # O(n^2)

# In[7]:


array = ['a','b','c','d','e']

def log_all_pairs(array):

    #There are nested for loops in this function but there is only one variable array. So we don't need two variables for the Big-O

    for i in range(len(array)): #n*O(n)
        for j in range(len(array)): #n*O(n)
            print(array[i], array[j]) #n*n*O(1)

log_all_pairs(array)


# In[8]:


#Total time complexity of the log_all_pairs function =
#O(n*n + n*n + n*n*1) = O(3n^2)
#The constants can be safely ignored.
#Therefore, O(3n^2) = O(n^2)


# In[9]:


new_array = [1,2,3,4,5]
def print_numbers_then_pairs(array):

    #There are a total of three loops here but only one variable. So we need only variable for our Big-O notation

    print("The numbers are : ") #O(1)
    for i in range(len(array)): #O(n)
        print(array[i]) #n*O(1)

    print("The pairs are :") #O(1)
    for i in range(len(array)): #n*O(n)
        for j in range(len(array)): #n*O(n)
            print(array[i],array[j]) #n*n*O(1)

print_numbers_then_pairs(new_array)


# In[10]:


#Total time complexity of the print_numbers_then_pairs function =
#O(1 + n + n*1 + 1 + n*n + n*n + n*n*1) = O(3n^2 + 2n + 2)
#Now, Big-O presents scalability of the cod, i.e., how the code will behave as the inputs grow larger and larger
#Therefore if the expression contains terms of different degrees and the size of inputs is huge, the terms of the smaller degrees become negligible in comparison to those of the higher degrees
#Therefore, we can ignore the terms of the smaller degrees and only keep the highest degree term
#O(3n^2 + 2n + 2) = O(3n2)
#The constants can be safely ignored.
#Therefore, O(3n^2) = O(n^2)


# # O(n)

# In[11]:


import time

ranjan = ['vinny']
everyone = ['ranjan', 'dev', 'sonu', 'vinny', 'sunil', 'raj', 'shivam', 'rakesh', 'nitish']
large = ['vinny' for i in range(100000)]
def find_vinny(array):
    t0 = time.time()
    for i in range(0,len(array)):
        if array[i] == 'vinny':
            print("Found Vinny!")
    t1 = time.time()
    print(f'The search took {t1-t0} seconds.')
find_vinny(ranjan)
find_vinny(everyone)
find_vinny(large)


def funchallenge(input):
    temp = 10 #O(1)
    temp = temp +50 #O(1)
    for i in range(len(input)): #O(n)
        var = True #n*O(1)
        temp += 1 #n*O(1)
    return temp #O(1)

funchallenge(ranjan)
funchallenge(everyone)
funchallenge(large)


# In[12]:


#Total running time of the funchallenge function =
#O(1 + 1 + n + n*1 + n*1 + n*1 + 1) = O(3n +3) = O(3(n+1))
#Any constant in the Big-O representation can be replaced by 1, as it doesn't really matter what constant it is.
#Therefore, O(3(n+1)) becomes O(n+1)
#Similarly, any constant number added or subtracted to n or multiplied or divided by n can also be safely written as just n
#This is because the constant that operates upon n, doesn't depend on n, i.e., the input size
#Therefore, the funchallenge function can be said to be of O(n) or Linear Time Complexity.


# In[ ]:




