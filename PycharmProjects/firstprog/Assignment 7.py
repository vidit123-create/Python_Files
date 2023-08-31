pin=input("Enter any pin for your machine:")
pin1=pin
if len(pin1)>10:
    pin1=pin1.replace('@','').replace('#','').replace('&','')
    if pin1.isnumeric()==True:
        print(f"Pin is valid pin for your machine: {pin}")
    else:
        print(f"Pin is not valid pin for your machine: {pin}")
else:
    print(f"Pin is not valid pin for your machine: {pin}")