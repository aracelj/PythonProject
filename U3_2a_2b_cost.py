#Uppgift #3  by Araceli Jakobsson
# 2a Calculates total cost to pay for the jacket which cost 2000 kr with 75% discount
# 2b User is ask to enter the discount percentage and computes the final cost after the discount



# 2a Calculates total cost to pay for the jacket which cost 2000 kr with 75% discount
jacket_cost = 2000
discount_cost1 = 75
final_cost1 = int(jacket_cost -(jacket_cost*(discount_cost1 )/100))  #calculates the final cost after the fixed discount
print ("\nJacket's original price:",jacket_cost,"kr \nDiscount:",discount_cost1 ,"kr")
print ("Final jacket's cost after the", discount_cost1, "% discount is:", final_cost1, "kr")

#2b Enter the discount percentage and give the total cost after the discount
discount_input = int(input("\nEnter different discount percentage: "))
discount_cost2 = int(jacket_cost*(discount_input/100))            #calculates for the discount cost
final_cost2 = int(jacket_cost - discount_cost2)        #calculates the final cost after the applied discount
print (discount_input,"% Discount: ", discount_cost2, "kr")
print ("Final jacket's cost after the",discount_input,"% discount: ", final_cost2, "kr.")
