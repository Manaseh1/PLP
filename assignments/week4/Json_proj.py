import json

#json syntax

"""
key
{
"name":"John"
}
"""
#dump converts a python object to a json string (s) in dumps and loads means string
a_dict = {1:1,2:2,3:3}
print(type(a_dict),a_dict)
something_in_json = '{"Name" : "John"}'
data = json.loads(something_in_json)
data['school'] = "Doe"
new_data = json.dumps(data)
print(data)
print(type(data))