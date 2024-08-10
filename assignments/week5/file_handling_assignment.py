file = open("my_file.txt",'a')

file.write(f'''
Whats up bros
Ooh its a good day
''')
content = file.read()
print(content)
file.close()
try:
    content = file.read()
    print(content)
except:
    print('Failed to read because of',PermissionError)
# file =open("my_file.txt",'r')
# content =file.read()
# print(content)