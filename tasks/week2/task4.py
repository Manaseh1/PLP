# Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

# list1 = []
# list2 = []
# while True:
#     input1 = input("Enter first input or done ")
#     list1.append(input1)
#     if input1 == "done":
#         break
# while True:
#     input2 = input("Enter second input or done ")
#     list2.append(input2)
#     if input2 == "done":
#         break
# print(list1)
# print(list2)

set1 = set()
set2 = set()

while True:
    input1 = input("Enter first input or done ")
    set1.add(input1)
    if input1 == "done":
        break
while True:
    input2 = input("Enter second input or done ")
    set2.add(input2)
    if input2 == "done":
        break

print(set1 & set2)