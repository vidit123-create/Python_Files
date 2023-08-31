# 1. Area of Rectangle
length=input("Length of rectangle:")
breadth=input("Breadth of rectangle:")
area=float(length)*float(breadth)
print("Area of Rectangle:",area,'\n')

# 2. BMI
height=input("Height of user:")
weight=input("Weight of user:")
bmi=int(weight)/float(height)**2*10000
print("Body Mass Index:",bmi,'\n')

#3. Weight Status
if bmi < 18.5:
    print("User is Underweight",'\n')
elif bmi > 18.5 and bmi < 24.9:
    print("User is Normal Range",'\n')
elif bmi > 25.0 and bmi < 29.9:
    print("User is Overweight",'\n')
elif bmi >= 30:
    print("User is Obese",'\n')
else:
    print("Can't able to calculate the Weight Status",'\n')

# 4. Simple Interest
p=float(input("Enter Principle:"))
r=float(input("Enter rate:"))
t=int(input("Enter time:"))
S_I=(p*r*t)/100
print("Simple Interest:",S_I,'\n')

# 5. Name, Age and Location
name=input("Enter name of the person:")
age=int(input("Enter age of the person:"))
location=input("Enter location where the person stays:")
print("Hello Everyone",',',"I am",name,"and","i am",age,"years old","and","i live in",location,'\n')

# 6. How many are left
no_of_persons=input("Enter no of persons:")
no_of_groups=input("Enter no of groups:")
no_of_persons_left=int(no_of_persons)%int(no_of_groups)
print("No of the Perssons left:",no_of_persons_left,'\n')

# 7. Convert temp in fahreinheit to celsius
temp_in_f=float(input("Enter temp in fahreinheit:"))
temp_in_c=((temp_in_f-32)*(5/9))
print("Temp in celsius:",temp_in_c,'\n')




