print("Emter marks of five subjects")
mark1= int(input("Enter marks of subject 1\n"))
mark2= int(input("Enter marks of subject 2\n"))
mark3= int(input("Enter marks of subject 3\n"))
mark4= int(input("Enter marks of subject 4\n"))
mark5= int(input("Enter marks of subject 5\n"))

sum= mark1+mark2+mark3+mark4+mark5
percentage=(sum/500)*100
print(sum)
print(percentage)
if(percentage<=100 and percentage>=90):
    print("Grade A")

elif(percentage<90 and percentage>=80):
    print("Grade B")

elif(percentage<80 and percentage>=70):
    print("Grade C")

elif(percentage<70 and percentage>=60):
    print("Grade D")

elif(percentage<60 and percentage>=40):
    print("Grade E")

else:
    print("Fail")

