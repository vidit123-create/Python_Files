"""
String Functions in Python -
1. Len() - Len() is generally used to get the total count of the characters in a given string.
2. type() - type() is generally used to check whether value present in the given string is a
type of class<string> or not.
3. max() - max() is generally used to get the largest element i.e. number from a given string if
number is passed as a value to string and it is also used to get the maximum character on the basis of
ascii value of the given character present in tht string.
4. min() - min() is generally used to get the smallest element i.e. number from a given string if
number is passed as a value to string and it is also used to get the minimum character on the basis of
ascii value of the given character present in tht string.
"""
name="Rahul"
print(len(name))
print(type(name))
print(max(name))
print(min(name))
"""
String Methods -
1. String Methods are the functions used to perform operation only on certain type of data type i.e.
string
2. Means if we are performing any operation on string then we can use the string methods.
3. String methods are used to perform operations on string, handling the string and string manipulation.
4. Different String Methods -
i. lower() - lower() is used to return all the characters in a string in lowercase.
ii. upper() - upper() is used to return all the characters in a string in uppercase.
iii. swapcase() - If string will contain values in lower case thn swapcase() will convert all the 
lower case character into upper case character.
If string will contain values in upper case thn swapcase() will convert all the upper case character
into lower case character.
iv. title() - title() is used to convert the first letter into uppercase() of each word and rest all 
the letters of that word into lowercase().

Note :- title() and swapcase() both does not contain any parameters.
v. capaitalize() - capaitalize() is used to convert only the first letter of the string into uppercase
and rest all the letters use to be in lowercase.
vi. strip(),lstrip() and rstrip() -
strip() - strip method in string is used to remove all the whitespaces from left and right side of 
a string.
lstrip() - lstrip method in string is used to remove all the whitespaces from the left side of a
string.
rstrip() - rstrip method in string is used to remove all the whitespaces from the right side of a 
string.
vii. replace() - replace() returns a string where one specified value is replaced by another specified 
value.
replace() with count as a parameter -
So when will use count inside the replace() thn if suppose a string contain two occurrence of a word
thn first occurrence of tht word will be replace by another word.
viii. count() - count() returns the total count of tht word i.e. no of times tht word has occurred in
tht string.
count() contains two parameters - start and end
so how count() works with start and end as a parameter - here it will count all the occurrence 
of tht word between start and end value mention in tht count() and return tht value.
ix. find() - find() use to search for the specified value in the string and return the index when the 
first time tht value occurred in tht string.
find() with start and end as parameter- so how find() works with start and end as a parameter.
so here find() will search for tht specified value within tht range of start and end.
x. rfind() - So rfind() is similar to find() but it actually use to find the specified value in tht 
string from right to left.
"""
company_name="DXC Technology is an american MNC"
print(company_name.lower())
print(company_name.upper())
print(company_name.lower()+'\t'+company_name.upper())
"""
WAP to repeat the company_name in lower and upper in alternate order in single line 
and in multi line.
"""
company_name1="DXC Technology is an american MNC"
company_name_lower=company_name.lower()
company_name_upper=company_name.upper()
for i in range(0,5):
    if((i==0) or (i==2) or (i==4)):
        print(company_name_lower)
    else:
        print(company_name_upper)
print((2*(company_name_lower+' '+company_name_upper+' '))+company_name_lower)

new_company_name=1*(company_name_lower+' '+company_name_upper+' ')
print(new_company_name)
print(new_company_name.swapcase())
print(new_company_name.title())
print(new_company_name.capitalize())
"""
So here two concatenated strings are used as a single string and capitalize operation is 
been performed on that single string.
"""
company_name_first="DXC Technology"
company_name_second="HPE IT"
company_name_third='\t'+company_name_first+','+company_name_second+'\t'
print(company_name_third)
#strip,lstrip and rstrip string methods
print(company_name_third.strip())
print(company_name_third.lstrip())
print(company_name_third.rstrip())
print(company_name_third.strip()+'\t'+company_name_third.lstrip()+'\n'+company_name_third.rstrip())
# replace
# So here we want to replace the HPE IT with TCS in company_name_third variable
company_name_fourth=company_name_third.replace('HPE IT','TCS')
#But if suppose we want to replace DXC Technology with Infosys in company_name_third variable
company_name_fifth=company_name_third.replace('DXC Technology','Infosys')
company1=company_name_fourth
company2=company_name_fifth
company3=company1.strip()+','+company2.strip()
print(company3)
# Creating a list using split method in string by passing company3 as string value.
company4=company3.split(',')
print(company4)
# count method in string -
company_name="DXC Technology has less no of employees as compared to TCS"
print(company_name.count('o'))
# count method in string using start and end as a parameter
print(company_name.count('o',4,30))
# find method in string -
print(company_name.find('c'))
print(company_name.find('C'))
# find method in string using start and end as a parameter
print(company_name.find('l'),5,16)
# rfind method in string
print(company_name.rfind('c'))

str="dxc"
str1=""
for i in str:
    str1=i
    print(str1)













