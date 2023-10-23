#dictionary
dict_example = {'key', 'value', 'new key', 'new value'}

dict_type = {'pep id': ['name', 'address', 'phone number',
                       'last visit', 'age', 'gender'],
            'pep id new':[]} 
#print('dict keys:',dict_type.keys())

#debugging
#print(dict_type)

for all_keys in dict_type.values():
  pass
  #print('\nall keys ',all_keys)


#create empty list
#print('empty string',list())

#print('empty dict', dict())

x = []
di = {}

#add new items to dict
dict_type['new key'] = 'new value'
#print('updated dict',dict_type)

#length of dict
length_of_dict = len(dict_type)
#print('length of dict', length_of_dict)


#Task
#create an empty dictionary and print it
new_dict = {}
print(new_dict)
#add new items to your empty details below
new_item = {'Electronics':'fan','clippers':'tv','ups':'radio'}

new_dict['Electronics'] = 'fan'
new_dict['clippers'] = 'tv'
new_dict['ups'] = 'radio'
print(new_dict)



#print your new dictionary
#add anot#dictionary
#dict_example = {'key': 'value', 'new key': 'new value'}
dict_example = {}
dict_example['key'] = 'value'
dict_example['new key'] = 'new value'
print(dict_example)

dict_type = {}
#dict_type = {'pep id': ['name', 'address', 'phone number',
#                       'last visit', 'age', 'gender'],
#            'pep id new':[]} 
dict_type['pep id'] = ['name', 'address', 'phone number', 'last visit', 'age', 'gender'],
dict_type['pep id new'] = []
print(dict_type)

#Created an empty dict & added items to it
empty_dict = {}


#add another new item to your empty dictionary below
#{‘Electronics’:[‘fan’,’clippers’,’tv’,’ups’]}
items = ['fan', 'clippers','tv','ups']

empty_dict['Electronics'] = items
#print your new dictionary
print(empty_dict)

#remove the value 'tv' from the dictionary
isolate_dict_value = empty_dict['Electronics'] 
list_value = isolate_dict_value
list_value.remove('tv')
print('empty dict', empty_dict)

Category = ['fruit', 'sales', 'food', 'gadgets']

Miscelleneous = [
  'fruit orange', 'food Fried_rice', 'sales 34400', 'sales 56834',
  'gadgets PDA', 'fruit apple', 'fruit pear', 'food yam'
]

Categorised = {'fruit':['orange','pear'], 'sales':['56834']}


'''
Problem:
Use the Category and Miscelleneous list to categorise the items.
Hint:
Dictionary = {key:value}
Dict = {Category:[items]}
Categorised = {‘Electronics’:[‘fan’,’clippers’,’tv’,’ups’]}
'''



#remove the list  [‘fan’,’clippers’,’tv’,’ups’] from the dictionary here new item to your empty details below
#{'Electronics':['fan','clippers','tv',ups’]}
#print your new dictionary
#remove the value 'tv' from the dictionary
#remove the list  [‘fan’,’clippers’,’tv’,’ups’] from the dictionary




#print('dict keys:',dict_type.keys())

#debugging
#print(dict_type)

for all_keys in dict_type.values():
  pass
  #print('\nall keys ',all_keys)


#create empty list
#print('empty string',list())
#print('empty dict', dict())

x = []
di = {}

#add new items to dict
dict_type['new key'] = 'new value'
#print('updated dict',dict_type)

#length of dict
length_of_dict = len(dict_type)
#print('length of dict', length_of_dict)



#Task
#create an empty dictionary and print it
#add new items to your empty details below
#{‘Electronics’:‘fan’,’clippers’:’tv’,’ups’:'radio'}
#print your new dictionary
#add another new item to your empty details below
#{‘Electronics’:[‘fan’,’clippers’,’tv’,’ups’]}
#print your new dictionary
#remove the value 'tv' from the dictionary
#remove the list  [‘fan’,’clippers’,’tv’,’ups’] from the dictionary here new item to your empty details below
#{'Electronics':['fan','clippers','tv',ups’]}
#print your new dictionary
#remove the value 'tv' from the dictionary
#remove the list  [‘fan’,’clippers’,’tv’,’ups’] from the dictionary

#Created an empty dict & added items to it
new_dict = {}
#print('This is an empty dict', new_dict)
new_dict['Electronics'] = 'fan'
new_dict['clippers'] = 'tv'
new_dict['ups'] = 'radio'
#print('Items added to the empty dict are:',new_dict)

#add another list item to your empty dictionary details below
new_dict['Electronics'] = ['fan', 'clippers','tv','ups']
#print('Added list item to empty dictionary',new_dict)

#remove the value 'tv' from the dictionary
new_dict['Electronics'] = ['fan', 'clippers', 'ups']
#print('Remove the value tv from the list', new_dict)

#remove the list
del new_dict['Electronics']
#print('Results after removing the list',new_dict)