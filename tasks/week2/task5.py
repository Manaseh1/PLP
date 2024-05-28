#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

list_o_words = []
while True:
    input_o_words = input('Enter word: ')
    if input_o_words == 'last':
        break
    list_o_words.append(input_o_words)

newlist = [words for words in list_o_words if len(words) % 2 != 0 ]    
print(newlist)