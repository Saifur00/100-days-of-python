""""two_digit_number = input() 

sum = int(two_digit_number[0]) + int(two_digit_number[1])

print(sum)"""


#Tip calculator

peopleAte = int(input("The number of people ate today: "))
bill = int(input("The damage you've made with the lavish meal today: "))
tipPercentage = int(input("What's the tip you want to give?: 12, 15 or 20 percent: "))

tip = (tipPercentage*bill)/100

eachPersonBillToPay = (bill+tip)/peopleAte

print(eachPersonBillToPay)



