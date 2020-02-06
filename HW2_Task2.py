#Works only for 4 charackters
number = int(input('Number (4 charackers): '))
a = number % 10
b = (number // 10) % 10
c = ((number // 10) // 10) % 10
d = (((number // 10) // 10) // 10) % 10
mult = a * b * c * d
sortlist = [a, b , c, d]

print("Multiply:", mult)
print("Revers:", a,b,c,d)
print("Sorted list:", sorted(sortlist))