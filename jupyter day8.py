#!/usr/bin/env python
# coding: utf-8

# # Day Objective
# 
# * Python data structure
#    * list
#    * Tuples
#    * dictionaries
# * basic program sets on data structures
# * Advanced problem set 
# * contact application(dictionary objects)
# 
# 
# Data structures :
# * to store, search and sort the data
# 
# 

# ## python data Structure
# ### lists
# * It's one of the common data structures supported by python , seperated by comma operator and enclosed in square brackets
# * Example:
#    * list1=[1,8,9,10]
#    * list2=["Gtam",12,13,5,"hyderabad"]

# In[1]:


lst = [1,8,16,9,2] #  Creating the list object in python
print(lst)  # access the entire list
print(lst[0])  # access the first item list
print(lst[1])  # access the second item list
print(lst[-1])  # access the last item list
print(lst[-2])
print(lst[1:])
print(lst[1:4])


# In[2]:


# Update the list item values using index
li = ["Gitam","Python",1989,2002]
print(li)
li[2] = 2019
print(li)


# In[3]:


# delete the specific item in the list
print(li)
del li[2]
print(li)


# In[4]:


# Basic list operations
lst1 = [1,9,6,18,2]
print(len(lst1)) # length of the list
print(lst1*2) # Repetation of the list
print(len(lst1)) # even after above step the length of list does not change
print(9 in lst1) # check if given list item is in the list or not
print(15 in lst1)
# Access the list items using iteration
for x in range(len(lst1)):
    print(lst1[x],end=" ")


# In[5]:


#gunction of the list
lst1
print(min(lst1)) # minimum item/element of the list
print(max(lst1)) # max element of the list
print(sum(lst1)) # sum of all the elements of the list
print(sum(lst1)//len(lst1)) # average of list elements
print(sum(lst1[1::2])/len(lst1[1::2])) # Average of all 


# In[6]:


# Methods of list Object
lst1
lst1.append(24) # adding a new element at the end of the list
lst1
lst1.insert(2,56) # adding an element at particular index
lst1
lst1.count(18) # return the value how many times the object repeated
lst1.index(56) # returns the index of object
lst1.sort() # it's sort the list in ascending order
lst1
lst1.pop() # removes the last element from the list
lst1
lst1.pop(1) # remove an element from a particular index
lst2 = [123,23,45]
lst1.extend(lst2) # Merge the list1 into list1
lst1.reverse() # reverse the list
lst1.remove(123) # remove the element from the list
lst1


# In[7]:


li = [1,9,8,2,6,3]
print(li[-1:0:-2])
li = [1,9,8,2,6,3]
print(li[-1:2:-2])


# In[8]:


# Function to find the second large item from the list
# input : [1,19,6,2,8,18,3]
# output : 18
def secondlarge(li):
    li.sort()
    return li[-2]
def genericlarge(li,n):
        li.sort()
        return li[-n]
li = [1,19,6,2,8,18,3]
genericlarge(li,4)


# In[9]:


# FUnction to find the least item from the list
# input : [1,19,6,2,8,18,3]
# output : 2
def secondleast(li):
    li.sort()
    return li[1]
def genericleast(li,n):
        li.sort()
        return li[n-1]
li = [1,19,6,2,8,18,3]
genericleast(li,4)


# ### Searching Algorithm
#  * linear search
#  * Binary search

# ### Linear Search*
# * linear search algorithm can be applied on duplicate and Unique list
#    - Unique list : The all items of the list is appeared only one 
#    - DUPLICATE LIST : The items of the list can be appeared more than once
# * Linear search algorithm can be applied on sorted list or unsorted list   
# 

# In[10]:


# Function to search the data in a list
# Search is found then return the index if not return -1
def linearsearch1(li,tarItem):
    for x in range(len(li)):
        if li[x] == tarItem:
            return x
    return -1
li =[1,19,6,2,8,18,3]
linearsearch1(li,225)


# In[11]:


# function
# input : [1,5,9,6,5,15,1,2,5],key=5 #duplicate
# output : 1 4 8
def linearsearch2(li,tarItem):
    for x in range(len(li)):
        if li[x] == tarItem:
            print(x,end=" ")
    return
li = [1,5,9,6,5,15,1,2,5]
linearsearch2(li,5) #1 4 8


# In[12]:


# Function
# input : list
# Output : seq of characters
# test case 
# [1,5,9,6,5,15,1,2,5],tar=5 --!! !!!!! !!!!!!!!!
def linearsearch3(li,tarItem):
    for x in range(len(li)):
        if li[x] == tarItem:
            j = 0
            while j != x+1:
                print("!",end="")
                j = j + 1
            print(end=" ")
    return
li = [1,5,9,6,5,15,1,2,5]
linearsearch3(li,5)


# In[13]:


# Function
# input : list
# Output : formatted 
# test case:
# [12,2,45,9,18,15,36] --60
# A list item which is perfectly multiple of 3 and 5
def linearsearch4(li):
    sum = 0
    for x in range(len(li)):
        if li[x] % 3 ==0 and li[x] % 5 ==0:
            sum += li[x] 
    return sum 
li = [12,2,45,9,18,15,36]
linearsearch4(li) # 60


# In[14]:


# Function
# Input : list
# Output : FOrmatted Output
# test case :
#[1,2,3,4,5] -- [1,3,8,15,5]
# [6,5,2,8,2] -- [6,12,40,4,2]
# print first and last number because first has no previous no. and last has no.. next no..
def linearsearch5(li):
    for x in range(len(li)):
        if x ==0 or x == len(li) - 1:
            print(li[x],end=" ")
        else:
            print(li[x-1]*li[x+1],end=" ")
    return
li = [1,2,3,4,5]
linearsearch5(li)


# In[15]:


# function
# Input : list 
#output : formatted output
# test case:
# [1,6,9,4,16,19,22] -- 1 9 19 22 
#1. first and last elements are printed as it is
#2. if a number has it's both sides even number then print it
def linearsearch6(li):
    # implement the logic 
    for x in range(len(li)):
        if x == 0 or x == len(li)-1:
            print(li[x],end=" ")
        elif li[x-1]%2 == 0 and li[x+1]%2 == 0:
            print(li[x],end=" ")
    return
li = [1,6,9,4,16,19,22]
linearsearch6(li)


# # Numbers to list
# 
# * input as number
# * expected output will be list

# In[16]:


# Function for convertions - number to list
# input : number
# output : list
#Test cases:-
#14569 --[1,4,5,6,9]
#1990 -- [1,9,9,0]
def numberlistconvertion(n):
    li=[]
    while n != 0:
        r = n % 10
        li.append(r)
        n =n //10
    li.reverse()
    return li
numberlistconvertion(14569)


# In[17]:


# Function 
# "Python Programming",p-> 2
# "Python Programming",m-> 2
def countcharOccurances(s,c):
    cnt = 0
    for ch in s:
        if ch == c:
            cnt += 1
    return cnt
def countcharOccurances(s,c):
    return s.count(c)
countcharOccurances("Python Programming",'m')


# In[20]:


# Function to convert the string to list
# test case
# "1 2 3 4 5 6" -- [1,2,3,4,5,6]
def stringtolistconvertion(s):
    li = s.split()
    numberslist = []
    for i in li :
        numberslist.append(int(i))
    return numberslist
s = "1 2 3 4 5 6"
stringtolistconvertion(s)


# # Sorting Algorithms:
# * Alll the sorting algorithms makes the list into ascending order
#   * Bubble sort
#   * selection sort
#   * insertion sort

# ### Bubble Sort
# * this algorithm compares the adj elements ,if the first element is grater
# * then second element then it's required to swap the elements
# 
# 

# In[21]:


# Function to represent the Bubble sort
def bubblesort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1],li[j]
    return li
li =[19,1,25,6,18,3]
bubblesort(li)


# In[ ]:




