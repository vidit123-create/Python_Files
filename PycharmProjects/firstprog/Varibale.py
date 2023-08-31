"""
Variable - It is container which is used to store some value whereas in python while
defining a variable we don't provide any datatype because while python program gets
executed so at tht time only complier used to understand what should be the datatype on the
basis of value been passed to the variable
a=9;b=4;c="DXC TECHNOLOGY";d=True;e="HPE IT"
print(a+b)
DataTypes - Datatypes are generally used to check whether what type of data is been stored 
in the variable and operations performed on that variable 
Interger,Floating point,Strings - Advance data type in Python, boolean
Python does not support char and double as a datatype
TypeCasting and Type Conversion -
print(c+e)
If we want to convert one datatype into another data type then will use type conversion 
or type casting 
So for typecasting and typeconversion there are various predefined functions in python
str(),int(),float()
var1=88;var2="DXC TECHNOLOGY\n";var3=88.9
var4=str(var1);var5=str(var3)
print(str(var3),int(var1),float(var1))#String Conversion
print(var4+var5)#String Concatenation
Interger and Floating point value can be changed into string
String cannot be changed into Floating point and Integer
Want to print any string multiple times
print(10*var2)
Want to display the data multiple times after typecasting
var6=10*str(float(var1)*var3)
print(var6)
Type of Exercise in Python
1. Quiz
2. Exercise 
3. Project
Taking input from user - So to take input from user will always use input() in python
where input() in python is a predefined function
#var7="10" # Number passed as a string
#print(int(var7))
#String cannot be converted into integer
"""
print("Enter number as a string value")
var8=input()
#print(int(var8))
print(10+int(var8))
# Calculator to add two number
a=5;b=9
print(a+b)
"""
1. Variable name should always be unique so that it could represent some entity by it's value.
2. Variable are case sensitive in python.
3. Variable defines with lowercase and uppercase represent two different variables.
4. Variable name cannot start with a number but it can be start with a underscore.
"""
"""
How to assign multiple variables with different values 
"""
company_name,lanuched_year="DXC TECHNOLOGY",2017
print(lanuched_year,company_name)
"""
How to assign multiple variables with single value
"""
branch=Technology=_stream="B.TECH"
print(_stream,Technology,branch)
"""
How to change the value of a user defined variable
"""
City="Ranchi"
print(City)
City="Chandigarh"
print(City)

age,age,age=10,20,30
print(age)

age,age1,age2=10,20,30
print(age)

