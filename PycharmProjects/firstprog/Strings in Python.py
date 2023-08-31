"""
String -
String is a combination or sequence of characters used to represent in single quote, double quote
and triple quotation
"""
company_name,organization,firm='DXC TECHNOLOGY',"DXC TECHNOLOGY","""DXC TECHNOLOGY"""
print(company_name,'\n',organization,'\n',firm)
"""
Single Line and Multiline Strings
Single Line String - 
Any particular value written in single or double quotes
Multi Line String -
Any paragraph written in triple quotes
"""
company_name="DXC TECHNOLOGY"
company_name="""DXC TECHNOLOGY contains CSC and ES legacy"""
print(company_name)
"""
"""
# Creation of multiple variables which contain number as a string and repeating them
_num1,_num2,num3=35,37,39
print((5*int(_num1),5*int(_num2),5*int(num3)))
print((5*str(_num1)+'\n'),(5*str(_num2)+'\n'+' '),(5*str(num3)+'\n'))
"""
Memory Allocation (Number vs String)
->
When a number is assigned in a variable then it get stored in some temporary memory 
as soon as number is been assigned to a variable, it gets start pointing to that temporary memory

In Case of String -> 
1.Since string is a sequence or combination of characters so here each character gets stored in a 
particular memory block.
2.So in string we can use the concept of Indexing and Slicing where Slicing will be used as 
positive and negative slicing and indexing will be used as positive and negative indexing.
"""
"""
Indexing of Strings ->
1. Indexing generally means to fetch the value of a string from a particular index.
Positive Indexing -
Which starts from 0 and here we fetch the value from left to right
Negative Indexing -
Which starts from -1 and here we fetch the value from right to left

2. Slicing generally means to get the substring or a part of string from a particular string
How we use to do Slicing -
starting index:ending index 
where ending index will be having one value greater than the last index value
for ex :-
name="ABC"
starting index -0
ending index - 3 # C having index as 2 so adding to 1 to it so it become 3
"""
company_name="HPE IT"
print(company_name[5],end='')
print(company_name[-4])
print(company_name[2:5])
print(company_name[:])
print(company_name[:3])
print(company_name[3:])
"""
Slicing of String using steps -
Here we use to perform the slicing in String with some step size
starting index:ending index:step size 
where default value of step is 1
"""
print(company_name[2:5:2])
print(company_name[:3:])
print(company_name[::2])
"""
Negative Slicing of a string -
It means that we are doing slicing in a string but with the help of negative indexes.
"""
company_name="DXC TECHNOLOGY"
print(company_name[:-6])
print(company_name[::-4])


