# Continuation of list 
# Soo the slicing operator is used to access sections of items from the list an example is below
# x: from the index x on wards
# :x from x backwards without actually including the xth value
# x:y in the range of x and y without including the xth value and the yth value
# append()add items to a list
# extend() adds all items of one list to another and more so to the end of the list
# if you want to change the value of a list item use list_name[array_of_ the_values]
# del is used to remove one or more items
# the remove() can also be used to removee list items pop() does the same but it also returns
# clear() removes all items in a list
# count() returns the count of  specified item in the  list
# print(interests.index('Wisdom')) index returns the array index of the item
# sort() sorts the list in ascending order/descending order sort(reverse = True) descends dont put it in a print statement
# copy() returns the shallow copy of a list
hobbies =['chess','watching ','reading']
interests = ['God','power','knowledge','gratitude']
interests.append('Wisdom')
interests.extend(hobbies)
interests[6] ='reading and studying'
del interests[2]
interests.remove('reading')
interests.insert(5,1234)
interests.pop(5)

#print(interests[0:])
randomnum = [1,2,4,5,1231,5,6,7,423141]
interests.sort(reverse=True)
# print(interests.copy())
for interest in interests:
    print(interest)

### Tuples ###
# tuple declaration tup = ('name',) and tup = "name",
# indexing is the same as using lists
# negative indexing eg tup[-1] gives the last index value

tup = 1,
tup2 = 2,
print(type(tup2))

