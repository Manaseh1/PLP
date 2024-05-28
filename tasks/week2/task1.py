#1 .Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

#user input
#a List
#sum of the list

numbers = []
while True:
    num = input("enter a number (or 'done' to finish)")
    if num == 'done':
        break
    numbers.append(int(num))
    print(sum(numbers))

