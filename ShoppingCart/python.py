#Numeric Data
num = 3
print(type(num))

num  = 3.14

print(type(num))

#Variables
my_variables = 0 
total_count = 0
user = 'John'

#invalid
second_variable = 10
user_num = 20

#Operator

#addition(+)
#subtraction(-)
#multiplication(*)
#division(/)
#modulus(%)
#exponent(**)


x = 10
y = 2

print(x and y)

#Operators with strings

str1 = 'Hello'
str2 = 'World'

print(str1 +"" + str2 + "" +str2)
print(str1 * 3)

#Control Statement
num = 0

if num > 0 :
    print("This number is positive")
elif num == 0:
    print ("This number is zero")
else:
    print("This number is negative")
    
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    
    if num1 > num2:
        print(num1 , "is greater than", num2)
    elif num2 > num1:
        print(num2, "is geater than" , num1)
    else:
        print("Both numbers are equal")
        
        #Loops
        fruits = ["apple", "banana", "cherry"]
        
        for fruit in fruits:   
            print(fruit)
            
            
        
        numbers = [ 1, 2 ,3 ,5 ,7]
        for number in numbers:
            print(number)
            
            
            #using a while loop to count from 1 to 5
            count = 1
            
            while count <= 5:
                print(count)
                count +=1 #increment the count by 1
                
                
#Loop control statements
                fruits = ["apple", "banana", "cherry", "dates"]
                for fruit in fruits:
                    if fruit == "cherry":
                        break #Exits the loop if cherry is found
                    print(fruit)
                    
                    print()
                    
for fruit in fruits:
    if fruit == "cherry":
        continue  # skip cherry and move to the next
    print(fruit)

print()

for fruit in fruits:
    if fruit == "cherry":
        pass  # A placeholder, no action is  needed for cherry
    print(fruit)

print()

#Y-Loop

# Count from 0 to 4, but stop early at 3
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break  # Exit the loop when the count reaches 3
    
    