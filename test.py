# print("hi")
# num1 = int(input("1st num:"))
# num2 = int(input("2nd num:"))
#
# print(f"Addition {num1} and {num2} is {num1+ num2}")
# print(f"sub {num1} and {num2} is {num1 - num2}")
# print(f"mul {num1} and {num2} is {num1* num2}")
# print(f"div {num1} and {num2} is {num1/ num2}")
# print(f"power {num1} and {num2} is {num1 ** num2}")
# print(f"reminder {num1} and {num2} is {num1% num2}")
# print(f"quotionet {num1} and {num2} is {num1// num2}")
#map
# s=[1,2,3,4,5]
# result =list(map (lambda x:x*x ,s))
# print(result)
# animals = ["a", "b", "c", "d"]
# result = list(map(lambda x:len(x), animals))
# print(result)
# filter
# a=[1,2,34,55,5,7]
# result = list(filter (lambda x:x%2!=0 , a))
# print(result)
# reduce
from functools import reduce
# s=[1,2,3,4,5]
# result = reduce(lambda x,y:x*y , s)
# print(result)
# maximum number
s=[1,2,3,4,5]
result = (reduce(lambda x,y:x if x>y else y, s))
print(result)