def liters_100km_to_miles_gallon(liters):
    miles = 100 * 1000/1609.344
    gallons = liters / 3.785411784
    return miles/gallons

def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784
    km = miles * 1609.344/1000
    km100 = km/100
    return liters/km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

'''
1. liters/gallons of fuel consumed per 100 km distance - Europe
2. Miles traveled with one gallon or fuel - USA

Note: litere/100km into mpg an vice versa

1 American mile = 1609.344 metres;
1 American gallon = 3.785411784 litres.
----
1 g = 3 l
L = 1g/3
----
we have liters and we have miles
literes/100
return new * (1/3.785411784)
'''
