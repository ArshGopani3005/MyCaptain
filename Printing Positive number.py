'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# Sorry for submitting late
list1 = [12,-7,5,64,-14]
list2 = [12,14,-95,3]
num=0

print("For list1 before printing positve numbers")
print(list1)
while(num<len(list1)):
    if list1[num]>= 0:
        print(list1[num],end = " ")
    num +=1 

num=0
print("\n")
print("For list2 before printing positve numbers")
print(list2)
while(num<len(list2)):
    if list2[num]>= 0:
        print(list2[num], end = " ")
    num +=1 