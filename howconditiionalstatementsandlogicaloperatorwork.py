#COMPARISON OPERATORS LETS YOU COMAPARE TWO OR MORE VALUES AND RETURN A BOOLEAN VALUE [TRUE OR FALSE]
#(EQUAL) (==) CHECKS IF TWO VALUES ARE EQUAL
#(NOT EQUAL )(!=) CHECK IF TWO VALUES ARE NOT EQUAL
#(GREATER THAN[>]) CHECKS IF THE VALUE ON THE LEFT IS GREATER THAN THE VALUE ON THE RIGHT
#(LESS THAN [<]) CHECKS IF THE VALUE ON THE LEFT IS GREATER THAN THE VALUE ON THE RIGHT
#(GREATER THAN OR EQUAL [>=]) CHECKS IF THE VALUE ON THE LEFT IS GREATER THAN OR EQUAL TO THE VALUE ON THE RIGH
#(LESS THAN OR EQUAL TO [<=]) CHECK IF THE VALUE ON THE LEFT IS LESS THAN OR EQUAL TO THE VALUE ON THE RIGHT


print(3>4) #FALSE
print(4>3) # TRUE
print(3<4) # TRUE
print(4<3) # FALSE
print(3==4) # FALSE
print(4==4)# TRUE
print(3 != 4) # TRUE
print(4 != 4) # FALSE
print(3 >= 4) # FALSE
print(3<=4)# TRUE

#HOW TO USE CONDITIONS  TO COMPARE VALUES AND RUN CERTAIN CODES BASED ON WHETHER THE CONDITIONAL EVALUETS TO TRUE OR FALSE

age = 20

if age >= 18 :
    print('you are adult ') # You are adult


age = 25

if age >= 20:
    print('Am an adult ')

else:
    print('ooops! Am not an adult') # Ooops Am not an adult


age = 12

if age >= 18 :
    print('Am an adult ')
elif age >= 13:
    print('Am a teenager ')
else:
    print('Am a child ') # Am an child


age = 2

if age >= 65:
    print('Am a senior citizen ')
elif age >=30:
    print('Am an adult in my prime ')
elif age >= 18:
    print('Am a young adult ')
elif age >=13:
    print('Am a teenager ')
elif age >=3:
    print('Am a young child ')
else:
    print('Am a toddler or infant') # Am a toddler or infant








