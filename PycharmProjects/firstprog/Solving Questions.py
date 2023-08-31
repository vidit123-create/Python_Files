"""
str1=''
count=0
for i in range(0,5):
    str=input("Enter any four digit binary no:")
    str1=str1+str+' '
for i in str1:
    if i==' ':
        count+=1
    else: pass
str1=str1.replace(' ',',',count-1)
print("Sample Input: ",str1)
str1=str1.split(',')
for i in str1:
    if int(i)%5==0:
        print(i)
    else: pass

str=input("Enter any string:")
count1=0;count2=0
for i in str:
    if i.isalpha()==True:
        count1+=1
    elif i.isnumeric()==True:
        count2+=1
    else: pass
print(f"No of letters in given string: {count1}")
print(f"No of digits in given string: {count2}")

str=input("Enter any number:")
count1=0;count2=0
for i in str:
    if int(i)%2 == 0:
        count1+=1
    else:
        count2+=1
print(f"Count of even no in given string: {count1}")
print(f"Count of odd no in given string: {count2}")
for i in range(1,6,1):
    for j in range(0,i,1):
        if j<=i:
            print('*',end=' ')
        else:pass
    print('\n')
for i in range(5,0,-1):
    for j in range(1,6,1):
        if j<=i:
            print('*',end=' ')
        else:pass
    print('\n')
"""
"""
# Fibonaaci Series
n=int(input("Enter any value of n:"))
i=0;j=1
for k in range(1,n):
    if k==1:
        result=i+j
        print(result,end=' ')
    else:
        i=j
        j=result
        result=i+j
        print(result,end=' ')
print()

#Fibonaaci Series
n=int(input("Enter any value of n:"))
m=1;i=0;j=1
while(m<n):
    if m==1:
        result=i+j
        print(result,end=' ')
    else:
        i=j
        j=result
        result=i+j
        print(result,end=' ')
    m=m+1
print()

#Factorial
n=int(input("Enter any value of n:"))
m=1;fact=1
while(n>=m):
    fact=fact*n
    n=n-1
print(f"Factorial of n: {fact}")
"""
# Print a 2-D array using list
list=[]
list1=[];list2=[];list3=[]
for i in range(0,3):
    for j in range(0,4):
        list=list+[i*j]
n=0;k=4
while(n<len(list)):
    if n<(len(list)-(k+4)):
        list1=list1+[list[n]]
    elif n<(len(list)-k):
        list2=list2+[list[n]]
    else:
        list3=list3+[list[n]]
    n=n+1
print([list1,list2,list3])
"""
Take numbers from 1 to 50 and if it is multiple of 3 then print "fizz" and if it is multiple of 5
then print "Buzz" if both then print "FizzBuzz" otherwise print that no.
"""
n=1
while(n<=50):
    if(n%3==0 and n%5!=0):
        print("fizz")
    elif(n%5==0 and n%3!=0):
        print("buzz")
    elif(n%3==0 and n%5==0):
        print("fizzbuzz")
    else:
        print(n)
    n=n+1






