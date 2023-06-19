mom_blood = input("Enter your Mother's blood type: ")
dad_blood = input("Enter your Father's blood type: ")

if(mom_blood == "A" and dad_blood == "A"):
    print("Your blood type can be A or O")
elif(mom_blood == "A" and dad_blood == "B"):
    print("Your blood type can be A, B, AB or O")
elif(mom_blood == "A" and dad_blood == "AB"):
    print("Your blood type can be A, B or AB")
elif(mom_blood == "A" and dad_blood == "O"):
    print("Your blood type can be A or O")
elif(mom_blood == "B" and dad_blood == "A"):
    print("Your blood type can be A, B, AB or O")
elif(mom_blood == "B" and dad_blood == "B"):
    print("Your blood type can be B or O")
elif(mom_blood == "B" and dad_blood == "AB"):
    print("Your blood type can be A, B or AB")
elif(mom_blood == "B" and dad_blood == "O"):
    print("Your blood type can be B or O")
elif(mom_blood == "AB" and dad_blood == "A"):
    print("Your blood type can be A, B or AB")
elif(mom_blood == "AB" and dad_blood == "B"):
    print("Your blood type can be A, B or AB")
elif(mom_blood == "AB" and dad_blood == "AB"):
    print("Your blood type can be A, B or AB")
elif(mom_blood == "AB" and dad_blood == "O"):
    print("Your blood type can be A or B")
elif(mom_blood == "O" and dad_blood == "A"):
    print("Your blood type can be A or O")
elif(mom_blood == "O" and dad_blood == "B"):
    print("Your blood type can be B or O")
elif(mom_blood == "O" and dad_blood == "AB"):
    print("Your blood type can be A or B")
elif(mom_blood == "O" and dad_blood == "O"):
    print("Your blood type can be O")
else:
    print("Invalid data")
