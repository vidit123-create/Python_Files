"""
Python program to check whether the string is symmetrical or not
"""
str=input("Enter any string:")
str1=str[:len(str)//2]
str2=str[len(str)//2:]
if str1 == str2:
    print("String is symmetrical in nature")
else:
    print("String is not symmetrical in nature")
"""
Python Program to print even length words in a string
"""
company_name="Dxc Technology is a better than TCS"
company_name=company_name.split(" ")
for i in company_name:
    if len(i)%2 == 0:
        print(i)
"""
Python program to print half of the string in uppercase
"""
company_name="Dxc Technology"
company_name=company_name[:len(company_name)//2]
print(company_name.upper())
"""
Python program to capitalize the first and last character of each word in a string
"""
company_name="dxc technology is better than tcs"
company_name=company_name.split(" ")
for i in company_name:
    print(i[0].capitalize()+i[1:len(i)-1]+i[len(i)-1:].capitalize())
"""
Python program to check if a string has at least one letter and one number
"""
str=input("Enter any string:")
str1=''
count=0
for i in str:
    if (('a'<=i<='z' or 'A'<=i<='Z') and ('0'<=i<='9')):
        str1=str1+i
        count+=1
        i=len(str)
        if count == len(str1):
           print("String contains atleast one letter and one number")

