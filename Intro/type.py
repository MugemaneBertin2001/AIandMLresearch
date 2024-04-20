from sys import getsizeof

y = 1
y1 = '1'
print(type(y))
print(type(y1))
print(getsizeof(y))
print(getsizeof(y1))



x = '2'
y  = 4

# print(x+y)


a = 9
if a % 2 == 0:
    print("Multiple of 2")
elif a % 5 == 0:
    print("multiple of 5")
elif a % 3 == 0:
    print("Multiple of 3")
else:
    print("none of them")
    
    
mine = "john doe"

for x in mine:
    print(x)
    
    
    
for x in range(0, 101, 25):
    print(x)
# lower_bound = 5
# upper_bound = 10

# for i in range(lower_bound, upper_bound + 1):
#     print(i)


lower_bound = 6
upper_bound = 10

if lower_bound >= upper_bound:
    print("Lower bound has exceeded the value of upper bound.")
else:
    print("Lower bound has not exceeded the value of upper bound.")
