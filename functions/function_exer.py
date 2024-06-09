# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d
#     return inner_fun(a, b)

# res = outer_fun(5, 10)
# print(res)

# def add(a, b):
#     return a+5, b+5

# result = add(3, 2)
# print(result)
# for num in range(1, 5):
#     print(num)

# x = 0
# for i in range(3):
#     x = x + i
# print(x)    

# for l in range(0,5,1):

#     print(l)

list1 = [3 , 2 , 5 , 6 , 0 , 7, 9]
sum = 0
sum1 = 0

for elem in list1:
    if (elem % 2 == 0):
        sum = sum + elem
        continue
if (elem % 3 == 0):
    sum1 = sum1 + elem
print(sum ,sum1)


for j in [0,1,2,3,4]:

    print(j)

for i in range(0,5):

    print(i)

for k in [0,1,2,3,4,5]:

    print(k)

# def isPalindrome(string):
#     if (string ==string[::-1]):
#         return "It is a palindrome"
#     else:
#         return "It is not a palindrome"
# string = input("Write something to see it if its a palindrome\n")    

# print(isPalindrome(string))