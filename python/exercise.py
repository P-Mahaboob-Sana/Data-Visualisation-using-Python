def amounts(flight, hotel,rentCar):
   Flight=flight
   Hotel=hotel
   Car=rentCar
   total = Flight + Hotel*7+ Car
   return total


Countries = ["london", "new York", "us", "paris"]
min_cost = float("inf")
max_cost =float("-inf")
min_country=""
max_country = ""

i=1
for country in Countries:
   flight = float(input("enter flight charges" + str(i)))
   hotel = float(input("enter hotel charges" + str(i)))
   car = float(input("enter car charges" + str(i)))
   i +=1
   totalAmount = amounts(flight,hotel,car)

if totalAmount < min_cost:
   min_cost = totalAmount 
   min_country = country
if totalAmount> max_cost:
   max_cost = totalAmount
   max_country = country

i+=1 
print(f"country with minimum cost is {min_country}")
print(f"country with max cost is {max_country}")
  




