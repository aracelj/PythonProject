# The program will do the following calculations

#1a ask for a whole number
tal1 = int(input("Enter a whole number: "))

#1b ask for another whole number and sum it up.
tal2 = int(input("Enter another whole number:"))
Total = tal1 + tal2
print ("Total for the two numbers: ",Total)

# 2a Calculates total cost to pay for the jacket which cost 2000 kronor with 75% rebates
jacket_cost = 2000
rebates = 75
final_cost = int(jacket_cost -(jacket_cost*(rebates)/100))
print ("\nJacket original price: 2000 kronor \nRebates: 75%")
print ("Total jacket cost after the", rebates, "% rebates is:", final_cost, "kronor.")

#2b Enter the rebates percentage and give the total cost after the rebates
rebates_input = int(input("Enter the rebates percentage: "))
rebates_cost = int(jacket_cost*(rebates_input/100))
final_cost_percentage = int(jacket_cost - rebates_cost)
print (rebates_input, "% rebates: ", rebates_cost, "kronor")
print ("Total cost of the jacket after the rebates is: ", final_cost_percentage, "kronor.")

