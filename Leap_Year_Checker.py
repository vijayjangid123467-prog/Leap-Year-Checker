y=int(input("Enter year:"))

if y%400==0:
    print(f"{y} is leap year.")
elif y%100==0:
    print(f"{y} is leap year.")
elif y%4==0:
    print(f"{y} is leap year.")
else:
    print(f"{y} is not a leap year.")