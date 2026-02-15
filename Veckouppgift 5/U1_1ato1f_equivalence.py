#1. Run the code by Araceli Jakobsson
"""
Original Code:
1a. x > 100                      #Error, must define x
1b. y == 42                      #Error, must define y
1c. len(text) >= 5               #Error, must define text
1d. z == True                    #Error, must define z
1e. 8 < v < 16                   #Error, must define v
1f. w == 32 or w == 64 or w == 128    #Error, must define w
1g. if x < 5: … elif x < 10: … elif x < 15: … else    #IndentationError:

"""

print(" ========= 1a ======== ")
x = int(input("Enter value x: "))
print((lambda x: x > 100)(x))                       #temporary function using lambda to check for x


print(" \n========= 1b ======== ")
y = input("Enter value y: ")
print((lambda y: y == 42 )(y=43))                   #temporary function using lambda to check for y


print(" \n========= 1c ======== ")
text = input("Enter a string: ")
text1 = text.replace(","," ").split()               #replace "," with space and remove space in the string input
print(len(text1) >= 5)                              #checks for length of string


print(" \n========= 1d ======== ")
z = input("Enter value z: ")
print((lambda z: z == True)(z))                     #check for z


print(" \n========= 1e ======== ")
v = int(input("Enter value v: "))
print((lambda v: 8 < v < 16)(v) )                   #check for v


print(" \n========= 1f ======== ")
w = int(input("Enter value w: "))
print((lambda w: w == 32 or w == 64 or w == 128)(w))  #check for w



print(" \n========= 1g ======== ")
x = int(input("Enter value x: "))
print((lambda x: "small" if x < 5 else "medium" if x < 10 else "large")(x=9))   #checks for value of x

