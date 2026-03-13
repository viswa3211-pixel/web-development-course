def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1, 'hasmi','X'], [2, 'zoya','X'], [3, 'kalamibka','X'],
            [4, 'marilyn','X'], [5, 'suthi','X'], [6,'mahi','X'],
            [7, 'hema', 'VII']]

print("\nOriginal List is : ")
print(students)
print("\nConvert the said List to Dictionary : ")
print(test(students))