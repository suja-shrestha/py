from array import array

#print 
print("hello world")

#voting age checking program with error handling
try:
    name = str(input("what is your name? "))
    age = int(input("what is your age? "))
    print(name)
    print(age)

    if age > 18:
        print("you can vote, " + name)
    elif age == 18:
        print("you can vote but you are still a minor, " + name)
    else:
        print("you are not old enough to vote, " + name + ". Your age is " + str(age))
except ValueError:
    print("Please enter a valid number for your age.")

#dynamic love you printing program with loop and error handling
try:
    n = int(input("Enter a number if time you want to print i love you: "))
    print("You entered: " + str(n))
    
    for i in range(n):
        print("I love you!")
    
except ValueError:
    print("Please enter a valid name or age.")

#Grade checking program with error handling and array of marks and students
Marks = [90, 80, 70, 45,]
Students = ["Alice", "Bob", "Charlie", "David"]
for i in range(len(Marks)):
    if Marks[i] >= 90:
        print(Students[i] + " scored an A grade.")  
    elif Marks[i] >= 80:
        print(Students[i] + " scored a B grade.")
    elif Marks[i] >= 70:
        print(Students[i] + " scored a C grade.")
    elif Marks[i] >= 60:
        print(Students[i] + " scored a D grade.")
    elif Marks[i] >= 50:
        print(Students[i] + " scored an E grade.")
    elif Marks[i] <=45:
        print(Students[i] + "Failed")
    print(Students[i] + " scored " + str(Marks[i]) + " marks.")

#dynamic grade checking program with error handling
try:
    sname = str(input('Enter your name to check grade: '))
    M = int(input('Enter your Marks obtain to check grade: '))
    
    if M >= 90:
        print(sname + " scored an A grade.")  
    elif M >= 80:
        print(sname + " scored a B grade.")
    elif M >= 70:
        print(sname + " scored a C grade.")
    elif M >= 60:
        print(sname + " scored a D grade.")
    elif M >= 50:
        print(sname + " scored an E grade.")
    elif M <=45:
        print(sname + " Failed")
    
    print(sname + " scored " + str(M) + " marks.")
    
except ValueError:
    print("Please enter a valid number for your marks.")

#while loop
i = 1
while i<=10:
    print(i)
    i+=1    

#for loop with array of strings
x = ['can','ban','cat','dog']
for i in x :
    print(i)    