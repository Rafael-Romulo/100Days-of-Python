price = float(input("\tWelcome to the tip calculator\nWhat was the total bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_in_the_table = int(input("How many people to split the bill? "))
individual_price = (price*(tip_percentage/100 + 1))/people_in_the_table
print(str(individual_price))
