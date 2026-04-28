 # 1.To create odd and even list
list=[10,501,22,37,100,999,87,351]

evenlist=[]
oddlist=[]

for n in list:
   
    if n % 2 == 0:
       evenlist.append(n)

    else:
        oddlist.append(n)

print(evenlist)
print(oddlist)


# 2. To count prime numbers

list=[10,501,22,37,100,999,87,351]

primelist=[]

for i in list:
   
  if i > 1 : 
    for j in range(2,i):
      if i % j == 0:
       break
    else:
       primelist.append(i)
    
    
print(primelist)  
print(len(primelist))  


# 3. Happy numbers in the list

list=[10,501,22,37,100,999,87,351]

happycount=0

for n in list:
    i= n
    count=0
    calculation = 0

    while i !=1:
        if count == 10:
         break
         
        while i > 0:
            digit = i % 10
            calculation = calculation + digit * digit
            i = i // 10

        i = calculation
        count = count + 1

    if i == 1 :
        print("Happy number" ,n)
        happycount=happycount+1
        
    else:
        print("not happy number" , n)

print("No of Happy numbers in the list" , happycount)


# 4.sum of first and last integer

number = int(input("Enter number"))
first_num=int(str(number)[0])
last_num=int(str(number)[-1])
sum= first_num + last_num
print(sum)



# 5.To find possible ways to make Rs.10

list =[1,2,5,10]
value=10

n=len(list)
a=list[0]
b=list[1]
c=list[2]
d=list[3]
count =0

possible_way=[ a + 2*b + c,
                c+c,
                b*c,
                c*b,
                d*a]

for i in possible_way:
    if i == value:
        print("Rs 10 obtained")
        count += 1

print("Possible ways found" , count)


# 6. Duplicates in the list

list1=[10,501,22,37,100]
list2=[1,501,2,7,10]
list3=[100,52,10,307,20]

duplicate=[]

for i in range(len(list1)): 
  for j in range(len(list2)):
   if list1[i] == list2[j]:
       
     for k in range(len(list3)):
       if list1[i] == list3[k]:
        duplicate.append(list1[i])
        
print(duplicate)



# 7. First non repeating element in a given list of integers.

list=[100,501,22,87,100,999,87]

for i in list:
 if list.count(i) == 1:
    print(i)
    break  



# 8. To find minimum element and sorting list

list=[22,51,10,807,100,999,87]
n=list[0]
for i in list:
    if i <= n:
        n = i 
        
print(n)
     
list.sort() 
print(list)



# 9. To find the triplet in the list.

list=[10,20,30,9]

value=59
a=list[0]
b=list[1]
c=list[2]
d=list[3]

if a+b+c == value:
    print(a,b,c)

if a+b+d == value:
    print(a,b,d)

if a+c+d ==value:
    print(a,c,d)

if b+c+d ==value:
    print(b,c,d)



#10. To find sub-list 

list=[4,2,-3,1,6]

length=len(list)
sublist=[]

for i in range(length):
   add=0
   for j in range(i+1 , length+1):
      sublist=list[i:j]
      if sum(sublist) == 0:
       print(sublist)