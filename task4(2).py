#sugar level

sugar=int(input("Enter the sugar level:"))
if sugar>=100:
    print("high")
elif sugar<80:
    print("low")
else:
    print("normal")