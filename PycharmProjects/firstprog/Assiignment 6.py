pin=input("Enter your pin:")
pin1=''
if len(pin)>10:
    for i in pin:
        if i=='@' or i=='#' or i=='&' and i.isalpha()!=True:
            pin1=pin1+i
        elif i.isnumeric()==True and i.isalpha()!=True:
            pin1=pin1+i
        else: pass
    if pin==pin1:
        print(f"Pin is Valid: {pin}")
    else:
        print(f"Pin is not Valid: {pin}")
else:
    print(f"Pin is not Valid: {pin}")

mobile_no=input("Enter your mobile no:")
mobile_num=''
count=0
if mobile_no.startswith('+'):
    for i in mobile_no:
        if i==' ' or i=='-':
            mobile_num=mobile_num+i
        elif i.isnumeric()==True:
            mobile_num=mobile_num+i
            count+=1
        else: pass
    if count==12 and mobile_no[1:]==mobile_num:
        print(f"It is a valid number: {mobile_no}")
    else:
        print(f"It is not a valid number: {mobile_no}")
else:
    print(f"It is not a valid number: {mobile_no}")
