# Uppgift3 Sports results by Araceli Jakobsson
# Version 1 Determines which team wins
# Version 2 Determines if it is a tie
# Version 3 Display how many goals more does the winner have than the losing team
# Program should be tested with Team 1 wins, Team 2 wins, and a Tie

#Version 1 Determines which team wins
winning_team = 0
goal_difference = 0
print("======== Version 1 Determines which team wins ========")
goal_tottenham = int(input("Enter goal made for Tottenham: "))
goal_liverpool = int(input("Enter goal made for Liverpool: "))
if goal_tottenham > goal_liverpool:                                   # checks if Tottenham wins over Liverpool
    winning_team = "Tottenham"
    goal_difference = goal_tottenham - goal_liverpool
    print(winning_team, "wins!")

elif goal_tottenham < goal_liverpool:                                 # checks if Liverpool wins over Tottenham
    winning_team = "Liverpool"
    goal_difference = goal_liverpool - goal_tottenham
    print(winning_team, "wins!")

#Version 2 Determines if it is a tie
else:                                                                 # checks if both team is a tie
    print("\n======== Version 2 Display if its a tie ========")
    print("It is a tie!")


#Version 3 Display how many goals more does the winner have than the losing team
print("\n======== Version 3 Display how may goals more does the winner have ========")
print(winning_team,"wins with", goal_difference, "more goal(s)!")




