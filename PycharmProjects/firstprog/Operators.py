"""
Operators
1. Arithmetic Operator
2. Assignment Operator
3. Logical Operator
4. Relational or Comparison Operator
"""
# Arithmetic Operator
"""
+ - as a operator is also used to concatenate the two strings
+ - as a operator is also used to perform arithmetic operations
"""
# String concatenation using + operator
_company_name1='DXC TECHNOLOGY'
_company_name2='HPE IT'
company_name3=_company_name1 + _company_name2
print(company_name3)

# Want to print the string multiple times or want to repeat the string
_company_name="DXC TECHNOLOGY \n"
print(5*_company_name)
# Want to repeat any number multiple times
_age=38
_age1=42
_age2=46
print((5*(str(_age)+'\n')),(10*(str(_age1)+'\t')),'\n',(5*(str(_age2)+'\n')))
#print(10*(str(_age)+'\t'))
"""
Division by Operator 
1. Division by Operator after dividing two numbers always give the quotient in the form of 
floating type 
"""
num1=38
num2=8
print(num1/num2)
"""
Exponent by **
So if we want to find out the square root or power of any number thn will use exponent by 
"""
_num1=25
#Find the square root of 25
print(int(_num1**(1/2)))
#Find the power of any number
_num1=5
print(float(_num1**2))
"""
Floor division by //
Floor division is generally used to divide two numbers and it also return quotient but in an 
integer format
"""
_num1=29
_num2=5
print(_num1//_num2)
"""
Modulus by %
Modulus by is generally used to divide two numbers but it return remainder in an integer format
"""
_num1=54
_num2=7
print(_num1%_num2)
# Relational or Comparison Operators
"""
Greater by - >
If a number is greater thn another num it will always return boolean value
"""
_num1=8
_num2=5
print(_num1>_num2)
"""
Greater than or equal to by ->
If a number is greater than or equal to another number this will always also return boolean value
"""
_num1=88
_num2=3
print(_num1>=_num2)
"""
Smaller than by or Smaller than or equal to by->
If a number is smaller than another number thn this will always return boolean value
"""
_num1=_num2=99
print(_num1<=_num2)
print(_num1<_num2)
"""
Equals to by 
Equals to is always going to return boolean value on the basis of values present in the 
variables
if same will return True
else will return False
"""
_num1=_num2=87
print(_num1==_num2)
_num2=90
print(_num1==_num2)
"""
Not Equals to operator 
Not Equals to operator also return boolean value on the basis of comparison of two variables 
"""
_num1=_num2=90
print(_num1!=_num2)
"""
Assignment Operators
Assignment operators are nothing but it is generally used to assign the value of a variable
and thr r multiple assignment operators 
"""
_num1=67 # So here 67 is the value assign to _num1 as a variable
print(_num1)
# Want to add 10 to already defined variable
_num1+=10
print(_num1)
#Want to find the modulus of already defined variable
_num1%=2
print(_num1)
"""
Logical Operators 
There are three types of logical Operators
1. AND Operator
2. OR Operator
3. NOT Operator
"""
_age1=_age2=88
_age3=45
print((_age1==_age2)and(_age3>_age2))
print((_age1==_age2)or(_age3>=_age1))
print(not(_age2>_age3))
"""
Operator Precedence(How to decide the Priority of the Operators)
"""
_age1=_age2=_age3=_age4=2
calc_age=_age1-_age2*_age3**_age4
print(calc_age)
"""
According to Operator Precedence first it will do exponent of thn multiplication 
thn subtraction
calc_age=2-2*2**2
calc_age=2-2*4
calc_age=2-8
calc_age=-6
"""
"""
Priority Table of Python -
1. Paranthesis 
2. Exponent of
3. Multiplication,Division,FloorDivision,Modulus
4. Addition,Subtraction
5. All the Comparison Operators
6. Logical Operators

NOTE - 
If while solving an expression we got two operators with the same level of priority 
thn will always go left to right to solve the expression for the operators with the 
same level of priority.
"""



