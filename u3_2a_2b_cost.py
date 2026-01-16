#Uppgift #3  by Araceli Jakobsson
# The program will do the following calculations of two numbers input
# Total cost of the jacket after the discount



# 2a Calculates total cost to pay for the jacket which cost 2000 kronor with 75% discount
jacket_cost = 2000
discount = 75
final_cost = int(jacket_cost -(jacket_cost*(discount)/100))  #calculates the final cost after the fixed discount
print ("\nJacket's original price:",jacket_cost,"kronor \nDiscount:",discount," kronor")
print ("Total jacket cost after the", discount, "% discount is:", final_cost, "kronor.")

#2b Enter the discount percentage and give the total cost after the discount
discount_input = int(input("\nEnter the discount percentage: "))
discount_cost = int(jacket_cost*(discount_input/100))            #calculates for the discount cost
final_cost_percentage = int(jacket_cost - discount_cost)        #calculates the final cost after the applied discount
print (discount_input,"% Discount: ", discount_cost, "kronor")
print ("Total cost of the jacket after the discount is: ", final_cost_percentage, "kronor.")
