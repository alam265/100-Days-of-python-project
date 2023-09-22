print("welcome to tip calculator")
bill = float(input('What was the total bill?\n'))

percentage = int(input('What percentage tip ypu like to give?\n'))

people = int(input('How many people to split the bill?\n'))

bill_with_tip = bill *(percentage/100) + bill

each_should_pay = bill_with_tip / people


print("Each one should pay:",round(each_should_pay,2)) 