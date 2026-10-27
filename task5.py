distance = float(input("Enter journey distance in km: "))
mileage = float(input("Enter vehicle mileage in km/litre: "))
price = float(input("Enter fuel price per litre: "))

if distance > 0 and mileage > 0 and price > 0:
    fuel = distance / mileage
    cost = fuel * price

    print("Fuel Required:", round(fuel, 2), "litres")
    print("Total Fuel Cost: Rs.", round(cost, 2))
else:
    print("Invalid Input")