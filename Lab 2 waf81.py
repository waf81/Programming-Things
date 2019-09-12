# Name:  Andrew Ferguson    NetID:  waf81
# Date: 9-11-19             Due Date: 9-14-19
# Description: Which of two cars is better for a long trip.

from math import ceil
# Introduction.
print("Hello! Welcome to the mileage calculator!")
print()
# Identification information of first car.
makeA = input("What is the make of your first vehicle? ")
modelA = input("What is the model of your first vehicle? ")
yearA = input("What is the year of your first vehicle? ")
print()
# MPG and capacity of first car.
MPGA = int(input("What is the MPG (miles per gallon) of the first vehicle? "))
TCapA = float(input("What is the tank capacity of the first vehicle? "))
print()
# Identification information of second car.
makeB = input("What is the make of your second vehicle? ")
modelB = input("What is the model of your second vehicle? ")
yearB = input("What is the year of your second vehicle? ")
print()
# MPG and capacity of second car.
MPGB = int(input("What is the MPG (miles per gallon) of the second vehicle? "))
TCapB = float(input("What is the tank capacity of the second vehicle? "))
print()
# Distance and gas prices.
Dist = int(input("How far (in miles) will you be traveling? "))
GasPrice = float(input("What is the average gas price? "))
print()
# Amount of fuel tanks needed for distance.
TankA = Dist / (MPGA * TCapA)
TankB = Dist / (MPGB * TCapB)
# Price of tanks
PriceA = TankA * (TCapA * GasPrice)
PriceB = TankB * (TCapB * GasPrice)
# Comparison Info
print(format("Car","30s"),format("Tanks","<10s"),"Cost")
print(format(yearA +" "+ modelA +" "+ makeA ,"30s"),format(str(ceil(TankA)),"<10s"),"$" + format(PriceA , ".2f"))
print(format(yearB +" "+ modelB +" "+ makeB ,"30s"),format(str(ceil(TankB)),"<10s"),"$" + format(PriceB , ".2f"))

