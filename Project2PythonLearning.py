
name_1 = input("What is the first person's name?\n")
name_2 = input("What is the second person's name?\n")
name_3 = input("What is the third person's name?\n")
slices_of_pizza = input("How many slices are there in the pizza?\n")
prize_of_pizza = input("How much did the pizza cost?\n")

percentage_eaten_by_name_1 = input(name_1 + ", how many slices did you eat?\n")
percentage_eaten_by_name_2 = input(name_2 + ", how many slices did you eat?\n")
percentage_eaten_by_name_3 = input(name_3 + ", how many slices did you eat?\n")

number_of_slices_eaten_by_name_1 = float(percentage_eaten_by_name_1) * float(slices_of_pizza)
number_of_slices_eaten_by_name_2 = float(percentage_eaten_by_name_2) * float(slices_of_pizza)
number_of_slices_eaten_by_name_3 = float(percentage_eaten_by_name_3) * float(slices_of_pizza)

how_much_money_did_name_1_spend = float(percentage_eaten_by_name_1) * float(slices_of_pizza)
how_much_money_did_name_2_spend = float(percentage_eaten_by_name_2) * float(slices_of_pizza)
how_much_money_did_name_3_spend = float(percentage_eaten_by_name_3) * float(slices_of_pizza)

print(name_1 + "has paid " + str(how_much_money_did_name_1_spend) + "$ for the pizza and ate " + str(number_of_slices_eaten_by_name_1)+
      " out of " + str(slices_of_pizza))
print(name_2 + "has paid " + str(how_much_money_did_name_2_spend) + "$ for the pizza and ate " + str(number_of_slices_eaten_by_name_2)+
      " out of " + str(slices_of_pizza))
print(name_3 + "has paid " + str(how_much_money_did_name_3_spend) + "$ for the pizza and ate " + str(number_of_slices_eaten_by_name_3)+
      " out of " + str(slices_of_pizza))
