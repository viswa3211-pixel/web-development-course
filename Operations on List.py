lst=['Apple', 'guava', 'Banana', 'Grapes', 'Orange','Mango']

print("length of the list:-",len(lst))
print("First Element:-",lst[0])
print("Last Element:-",lst[-1])

lst.append('Kiwi')
print("Updated List:-",lst)

lst.remove('guava')
print("Updated List:-",lst)

lst.sort()
print("Sorted List:-",lst)

lst.pop()
print("Updated List:-",lst)

lst.reverse()
print('Reversed list:-',lst)

print("Multiplication on List:-",lst*2)

lst = lst[:4]
print("Sliced List:-",lst)

lst.clear()
print("Updated List:-",lst)