# 1. Filter age below 18 and Map the remaining List
di=[
    {"name":"john","age":21},
    {"name":"Rythm","age":23},
    {"name":"Roshan","age":15},
    {"name":"Roshini","age":12},
    {"name":"Lahi","age":18},
    {"name":"Cintu","age":2}
    ]  

age_18=(list(filter(lambda person : person["age"] < 18, di)))
print(age_18)
remaining_people=(list(filter(lambda people_above_18 : people_above_18 ["age"] > 18, di)))
print(list(map(lambda namelist : namelist ,  remaining_people)))


# 2.Using reduce function product of all items in list  
from functools import reduce

list = [10,40,32,45,65]
product=reduce(lambda a,b : a*b, list)
print(product)


#3.Lambda function to check the even numbers

nums=[11,13,14,15,16,18,9,20]
even_numbers=list(filter(lambda x: x % 2 == 0,nums))
print(even_numbers)
square_even_numbs=list(map(lambda sqr_num : sqr_num * sqr_num, even_numbers))
print(square_even_numbs) 



# 4. To check given string is a number

string = lambda text : "Number" if str(text).isdigit() else "NotaNumber"
print(string(13212312))
print(string("Python"))
print(string(123123))
print(string("text123"))
print(string("12312387534"))

# 5. To extract datetime from datetime object

import datetime

date_time = datetime.datetime.now()
result = lambda value: (value.year, value.month, value.day) 
print(result(date_time))


# 6. To generate Fibonacci series

def fibonacci(n):
 seq=[0,1]
 list(map(lambda m: seq.append(sum(seq[-2 : ])), range(2,n)))
 return seq[ : n]
print(fibonacci(20))