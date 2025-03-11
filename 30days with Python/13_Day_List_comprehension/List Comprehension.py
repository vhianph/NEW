'''Example 1'''
language = "Python"
lst1 = list(language)
print(type(lst1))
print(lst1)

lst2 = [i for i in language]
print(lst2)


'''Example 2
For instance if you want to generate a list of numbers'''
numbers = [i for i in range(16)]
print(numbers)

square = [i * i for i in range(11)]
print(square)

numbers = [(i, i*i) for i in range(11)]
print(numbers)


'''Example 2
List comprehension can be combined with if expression'''
print("Even numbers")
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

print("Odd numbers")
odd_number = [i for i in range(21) if i % 2 != 0]
print(odd_number)

print("Positive even numbers")
number = [-8,-7,-3,-1,0,1,2,3,4,10]
positive_even_numbers = [i for i in number if i > 0 and i%2==0]
print(positive_even_numbers)

list_of_list = [[1,2,3], [4,5,6], [7,8,9]]
flattened_list = [ number for row in list_of_list for number in row]
print(flattened_list)