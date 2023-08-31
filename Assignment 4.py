"""
Write a Program to calculate Simple Interest with all the inputted user values
"""
_P=input("Money Borrowed:")#2000
_R=input("Rate of Interest:")#4%
_T=input("Time Period:")#3
SI=((int(_P)*int(_R)*int(_T))/100)
print(SI)
"""
SI=((2000*4*3)/100)
SI=(24000/100)
SI=240.0
"""
"""
Write a small calculator program with all the inputted user values
"""
_num1=int(input("First no:"))#3
_num2=float(input("Second no:"))#6.0
_num3=int(input("Third no:"))#2
_num4=float(input("Fourth no:"))#2.4
calc_num=_num1+_num2%_num3*_num4
print(calc_num)
"""
calc_num=3+6.0%2*2.4
calc_num=3+0.0*2.4
calc_num=3+0.0
calc_num=3.0
"""
"""
Ask user's birth year and calculate his age
"""
birth_year=int(input("Person's Birth Year:"))
current_year=2023
persons_age=current_year - birth_year
print(persons_age)
