#!/usr/bin/env python
# coding: utf-8

# Q1. Create one variable containing following type of data:
# 
# (i)	string
# 
# (ii)	list
# 
# (iii)	float
# 
# (iv)	tuple
# 

# In[8]:


a = 'kshitij'
type(a)


# In[9]:


b = ["kshitij", "saxena", 1,2,23.4, True]
type(b)


# In[10]:


c = (23.56)
type(c)


# In[11]:


d = ("kshitij", "saxena", 1,2,23.4, True)
type(d)


# Q2. Given are some following variables containing data:
# 
# (i)	var1 = ‘ ‘
# 
# (ii)	var2 = ‘[ DS , ML , Python]’
# 
# (iii)	var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
# 
# (iv)	var4 = 1
# 
# What will be the data type of the above given variable

# In[12]:


var1 = ''
type(var1)


# In[13]:


var2 = '[DS, ML, Python]'
type(var2)


# In[14]:


var3 = ['DS', 'ML', 'Python']
type(var3)


# In[15]:


var4 = 1
type(var4)


# Q3. Explain the use of the following operators using an example:
# 
# (i)	/
# 
# (ii)	% 
# 
# (iii)	//
# 
# (iv)	**

# In[17]:


a = 2
b= 3

print(a/b)
print(a%b)
print(a//b)
print(a**b)


# Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the 
# element and its data type.

# In[18]:


list = [1,2,3,4,5,6,'kshitij', 23.45, True, False]

for i in list:
    print(i)
    print(type(i))


# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many 
# times it can be divisible.

# In[23]:


A = int(input())  
B = int(input())  

count = 0  

while A % B == 0:
    A /= B
    count += 1

if count > 0:
    print(f"{A} is divisible by {B} and can be divided {count} times.")
else:
    print(f"{A} is not divisible by {B}.")


# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is 
# divisible by 3 or not.

# In[24]:


list = range(0,25)

for i in list:
    if i % 3 == 0:
        print("Number is divisible by 3")
    else:
        print("Number is not divisible ny 3")


# Q7. What do you understand about mutable and immutable data types? Give examples for both showing 
# this property.

# Mutable data types are those in which the value of a variable can be changed.
# Immutable data types are those in which the value of a variable cannot be changed. In case of append also a new object gets created.
# 

# In[25]:


a = 'kshitij'
type(a)


# In[27]:


a(0) = 'm'


# In[28]:


b = ['kshitij', 1,2,3,4, 234.56, True]
type(b)


# In[29]:


b[3] = 'Mohan'


# In[30]:


print(b)


# In[31]:


type(b)


# a is a string which is not mutable whereas b is a list which is mutable and value of a variable is changed

# In[ ]:




