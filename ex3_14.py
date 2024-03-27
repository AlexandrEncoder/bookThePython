kmTraveled = float(input("Enter with km traveled: "))
day = float(input("Enter day the travel: "))

timeCost = kmTraveled * 0.15
dayCost = day * 60
sumCost = timeCost + dayCost

print("You will pay at the end the travel: R$",sumCost)
print("Cost day: ",dayCost)
print("Cont for KM: ",timeCost)