#empty dictionary
my_dict={}

#dictionary with integer keys
my_dict={1: 'apple', 2:'hall'}

#dictionary with mixed keys
my_dict={'name' : ' zoya' , 1: [1,2,3,4]}

my_dict={'name' : ' zoya' , 'age' : 15}

#output : zoya
print(my_dict['name'])
print(my_dict['age'])

#Update the values
my_dict['age']=16
print(my_dict)

#add item
my_dict['address'] = 'xyz'

#remove particluar element
my_dict.pop('age')
print(my_dict)

#access a particluar element
print("Address : ",my_dict.get('address'))

#remove all the elements
my_dict.clear()
print(my_dict)
